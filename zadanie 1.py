# Napisz, na przynajmniej cztery sposoby, funkcję zamieniającą listę liczb całkowitych w stringa odpowiadających im znaków unikodu. Przykładowo, lista [65, 66] powinna zostać zamieniona na AB.
# Wykorzystaj decorator do testów wydajności

from time import perf_counter
from reprlib import repr as REPR
from typing import List


def execution_time(function):  #dekorator
    def wrap(*args, **kwargs): #args to lista wartości, key word arguments to słownik argumentow
        name = function.__name__
        args_str = ', '.join(REPR(arg) for arg in args)
        kwargs_str = ', '.join('%r=%r'%(REPR(k),REPR(v)) for k,v in kwargs.items())
        t0 = perf_counter()
        value = function(*args, **kwargs)
        t1 = perf_counter()
        print('Czas:%.8f;%s(%s,%s)->%s'%(t1-t0,name,args_str,kwargs_str,REPR(value)))
        return value
    return wrap #dekorator powinien zwracać funkcje


@execution_time
def test_function_1(int_list: List[int]):
    unicode_list: str = ""
    for number in int_list:
        unicode_list = unicode_list + chr(number) + " "

    return unicode_list

@execution_time
def test_function_2(int_list: List[int]):
    chr_list = map(chr, int_list)
    return " ".join(chr_list)

@execution_time
def test_function_3(int_list: List[int]):
    chr_list = [chr(i) for i in int_list]
    return " ".join(chr_list)

@execution_time
def test_function_4(int_list: List[int]):
    unicode_list: str = ""
    chr_list = []
    for i in range(len(int_list)):
        chr_list.append(chr(int_list[i]))
    for word in chr_list:
        unicode_list = unicode_list + word + " "
    return unicode_list

test_function_1([124,68,43,164,122])
test_function_2([124,68,43,164,122])
test_function_3([124,68,43,164,122])
test_function_4([124,68,43,164,122])

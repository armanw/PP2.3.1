# Napisz, na przynajmniej cztery sposoby, funkcję zamieniającą listę liczb całkowitych na łańcuch odpowiadających im znaków unikodu. Przykładowo, lista [65, 66] powinna zostać zamieniona na AB.
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


    return unicode_list

test_function(5,10, c=4)

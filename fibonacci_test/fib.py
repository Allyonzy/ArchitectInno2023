from recur_cache import recur_cache

@recur_cache
def fib(n: int) -> int:
    '''
    basic solution
    Рекурсивная функция для вычисления числа 
    в последовательности Фибоначчи
    1, 1, 2, 3, 5, 8, 13, 21, ....
    @param int n - индекс в последовательности
    @returns int result число Фибоначчи по заданному индексу
    '''
    if n < 0 or n == None : 
        return None
    if n < 2: 
        return n
    else:
        '''
        1 1 2 3 5 8 13 21 ...

        n = 7 
        fib(n-1) - n = 6
        fib(n-2) - n = 5
        ----                                           ----
        n = 6                                          n = 5
        fib(n-1) - n = 5                               fib(n-1) - n = 4
        fib(n-2) - n = 4                               fib(n-2) - n = 3
        ----                 ----                      ----                  ----
        n = 5                n = 4                     n = 4                 n = 3
        fib(n-1) - n = 4     fib(n-1) - n = 3          fib(n-1) - n = 3      fib(n-1) - n = 2
        fib(n-2) - n = 3     fib(n-2) - n = 2          fib(n-2) - n = 2      fib(n-2) - n = 1 ->1
        --------------------------
        n = 0, n = 1
        '''
        return fib(n-1) + fib(n-2)
    
class Fibonacci():
    __number = 0

    def __init__(self, n):
        self.__n  = n
    
    @recur_cache
    def fib_recurs_by_index(self):
        '''
        basic solution
        Рекурсивная функция для вычисления числа 
        в последовательности Фибоначчи
        1, 1, 2, 3, 5, 8, 13, 21, ....
        @param int n - индекс в последовательности
        @returns int result число Фибоначчи по заданному индексу
        '''
        if self.__n < 0 or self.__n == None : 
            self.__number = None
            return self.__number
        if self.__n < 2: 
            return self.__n
        else:
            self.__number = fib(self.__n-1) + fib(self.__n-2)
            return self.__number
    
    def __str__(self):
        return f"{self.__number}"


if __name__ == '__main__':
    ind = 333
    output_string = "Число по индексу {0} в последовательности Фибоначчи - {1}"
    print(output_string.format(ind, fib(ind)))
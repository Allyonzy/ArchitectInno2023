import inspect

class InnerDataMixin:
    @property
    def inner_data(self):
        return inspect.getsource(self.__class__)
    
    @property
    def dict_data(self):
        return self.__dict__
    

class Fibonacci(InnerDataMixin):
    __number = 0

    def __init__(self, n = 0):
        self.__n  = n
    
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
    
class Person(InnerDataMixin):
    __age = 0

    def __init__(self, name: str = 'Noname'):
        self.name = name

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        self.__age = age

    @staticmethod
    def is_adult(age):
        print(age)
        if age > 18:
            return "Взрослый"
        else:
            return "Меньше 18 лет"
    
if __name__ == '__main__':
    fib = Fibonacci(2)
    print(fib.inner_data)
    print(fib.dict_data)

    person = Person()
    person.age = 15
    print(person.inner_data)
    print(person.dict_data)

from functools import wraps

CAN_RUN = True

def a_new_decorator(a_func):
    def wrapTheFunction():
        print("Я делаю что-то скучное перед исполнением a_func()")

        a_func()

        print("Я делаю что-то скучное после исполнения a_func()")

    return wrapTheFunction

@a_new_decorator
def a_function_requiring_decoration():
    print("Я функция, которая требует декорации")

def decorator_name(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        '''
        *args = (a, b, c)
        **kwargs = {'name': 'Altair', 'age': 54}
        __dict__
        '''
        if not CAN_RUN:
            return "Функция не будет исполнена"
        return f(*args, **kwargs)
    return decorated

@decorator_name
def func():
    return("Функция исполняется")


a_function_requiring_decoration()
print(func())





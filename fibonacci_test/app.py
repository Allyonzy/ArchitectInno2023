
from fib import fib, Fibonacci

OUT_TEXT = "Число по индексу {0} в последовательности Фибоначчи - {1}"
VALUE_ERROR_TEXT = "С заданным значением функция Фибоначчи рассчитана быть не может"

def print_result(out_text, index, result) -> None:
    print(out_text.format(index, result))

try: 
    #проверка функции Фибоначчи
    input_number = int(input("Введите число для теста "))
    func_fib_test = fib(input_number)
    print_result(OUT_TEXT, input_number, func_fib_test)

    #проверка класса Фибоначчи 
    fib_test = Fibonacci(input_number)
    print_result(OUT_TEXT, input_number, fib_test.fib_recurs_by_index())

except ValueError:
    print(VALUE_ERROR_TEXT)


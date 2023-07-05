def recur_cache(func):
    '''
    Функция рекурсивного кэша, декоратор
    Решает задачу мемоизации - запоминаем пройденные значения 
    по результату работы функции
    '''
    cache = {}
    def wrapper(*args, **kwargs):
        '''
        Обертка для запоминания в кэш
        @param tuple *args - кортеж из значений вида (a1, a2, ..., an)
        @params dict **kwargs - словарь значений функции вида {'some_key': 'some_value', 'some_key01': 0}
        @returns результат из кэш
        '''
        key = (args, frozenset(kwargs.items()))  # словари не кэшируются 
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper
import functools

def CachedFunction(func):
    @functools.wraps(func)
    def wrapper(*args):
        key = args[:]  # Создаем ключ из позиционных аргументов
        if key not in wrapper.cache:
            wrapper.cache[key] = func(*args)  # Вычисляем значение и сохраняем в кэше
        return wrapper.cache[key]
    
    wrapper.cache = {}  # Инициализируем кэш пустым словарем
    return wrapper

import time
from typing import Callable


def time_it(message: str | None = None):
    def inner(func: Callable):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            msg = message if message is not None else "Время выполнения функции составило:"
            print(f'{msg} {end_time - start_time:.4f} с.')
            return result
        return wrapper
    return inner

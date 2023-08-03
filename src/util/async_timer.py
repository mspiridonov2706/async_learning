import functools
import time
from typing import Callable, ParamSpec, TypeVar, Awaitable, Coroutine


P = ParamSpec("P")
R = TypeVar("R")


def async_timed():
    def wrapper(func: Callable[P, Awaitable[R]]) -> Callable[P, Coroutine[None, None, R]]:
        @functools.wraps(func)
        async def wrapped(*args: P.args, **kwargs: P.kwargs) -> R:
            print(f'выполняется {func} с аргументами {args} {kwargs}')
            start = time.time()
            try:
                return await func(*args, **kwargs)
            finally:
                end = time.time()
                total = end - start
                print(f'{func} завершилась за {total:.4f} с')
        return wrapped
    return wrapper

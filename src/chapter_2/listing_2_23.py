"""Выполнение счетного кода в отладочном режиме"""


import asyncio

from src.util import async_timed


@async_timed()
async def cpu_bound_work() -> int:
    counter = 0
    for i in range(100000000):
        counter = counter + 1
    return counter


@async_timed()
async def async_main():
    task_one = asyncio.create_task(cpu_bound_work())
    await task_one


def main():
    asyncio.run(async_main(), debug=True)

"""Простой асинхронный генератор"""


import asyncio
from src.util import delay, async_timed


async def positive_integers_async(until: int):
    for integer in range(1, until):
        await delay(integer)
        yield integer


@async_timed()
async def async_main():
    async_generator = positive_integers_async(5)
    print(type(async_generator))
    async for number in async_generator:
        print(f'Получено число {number}')


def main():
    asyncio.run(async_main())

"""Получение доступа к циклу событий"""


import asyncio

from src.util import delay, async_timed


def call_later():
    print("Меня вызовут в ближайшем будущем!")


@async_timed()
async def async_main():
    loop = asyncio.get_running_loop()
    loop.call_soon(call_later)
    await delay(1)


def main():
    asyncio.run(async_main())

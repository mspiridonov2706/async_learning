"""Создание цикла событий вручную"""


import asyncio

from src.util import async_timed


@async_timed()
async def async_main():
    await asyncio.sleep(1)


def main():
    loop = asyncio.new_event_loop()
    try:
        loop.run_until_complete(async_main())
    finally:
        loop.close()

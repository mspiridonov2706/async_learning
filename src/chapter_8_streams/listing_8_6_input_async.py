"""Использование потоковых читателей для ввода данных"""

import asyncio

from src.util import delay
from .listing_8_5_stdin_reader import create_stdin_reader


async def run():
    stdin_reader = await create_stdin_reader()
    while True:
        delay_time = await stdin_reader.readline()
        asyncio.create_task(delay(int(delay_time)))


def main():
    asyncio.run(run())


if __name__ == "__main__":
    main()

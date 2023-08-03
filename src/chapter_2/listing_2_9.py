"""Выполнение двух сопрограмм"""

import asyncio
from src.util import delay


async def async_main():
    sleep_for_three = asyncio.create_task(delay(3))
    sleep_again = asyncio.create_task(delay(3))
    sleep_once_more = asyncio.create_task(delay(3))

    await sleep_for_three
    await sleep_again
    await sleep_once_more


def main():
    asyncio.run(async_main())

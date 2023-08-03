"""Выполнение двух сопрограмм"""

import asyncio
from src.util import delay


async def async_main():
    sleep_for_three = asyncio.create_task(delay(3))
    print(type(sleep_for_three))
    result = await sleep_for_three
    print(result)


def main():
    asyncio.run(async_main())

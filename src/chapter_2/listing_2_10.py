"""Выполнение двух сопрограмм"""

import asyncio
from src.util import delay


async def hello_every_second():
    for i in range(2):
        await asyncio.sleep(1)
        print("пока я жду, исполняется другой код!")


async def async_main():
    first_delay = asyncio.create_task(delay(5))
    second_delay = asyncio.create_task(delay(5))
    await hello_every_second()
    await first_delay
    await second_delay
    print("hellow")


def main():
    asyncio.run(async_main())

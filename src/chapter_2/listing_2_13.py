"""Задание тайм-аута для задачи с помощью wait_for"""

import asyncio

from src.util import delay


async def async_main():
    task = asyncio.create_task(delay(10))
    try:
        result = await asyncio.wait_for(asyncio.shield(task), 5)
        print(result)
    except TimeoutError:
        print("Задача заняла более 5 с, скоро она закончится!")
        result = await task
        print(result)


def main():
    asyncio.run(async_main())

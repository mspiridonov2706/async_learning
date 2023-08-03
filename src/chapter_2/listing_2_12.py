"""Задание тайм-аута для задачи с помощью wait_for"""

import asyncio

from src.util import delay


async def async_main():
    delay_task = asyncio.create_task(delay(2))
    try:
        result = await asyncio.wait_for(delay_task, timeout=1)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print('Тайм-аут!')
        print(f'Задача была снята? {delay_task.cancelled()}')


def main():
    asyncio.run(async_main())

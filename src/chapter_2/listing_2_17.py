"""Хронометраж двух конкурентных задач с помощью декоратора"""


import asyncio

from src.util.async_timer import async_timed


@async_timed()
async def delay(delay_seconds: int) -> int:
    print(f'засыпаю на {delay_seconds} с')
    await asyncio.sleep(delay_seconds)
    print(f'сон в течение {delay_seconds} с закончился')
    return delay_seconds


@async_timed()
async def async_main():
    task_one = asyncio.create_task(delay(2))
    task_two = asyncio.create_task(delay(3))
    await task_one
    await task_two


def main():
    asyncio.run(async_main())

"""Неправильное использование блокирующего API как сопрограммы"""


import asyncio
import requests

from src.util import async_timed, delay


@async_timed()
async def get_example_status() -> int:
    return requests.get('http://www.example.com').status_code


@async_timed()
async def async_main():
    task_1 = asyncio.create_task(get_example_status())
    task_2 = asyncio.create_task(get_example_status())
    task_3 = asyncio.create_task(get_example_status())
    await task_1
    await task_2
    await task_3


def main():
    asyncio.run(async_main())

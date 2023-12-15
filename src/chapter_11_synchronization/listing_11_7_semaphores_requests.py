"""Ограничение числа запросов к API с помощью семафора"""

import asyncio
from asyncio import Semaphore
from aiohttp import ClientSession


async def get_url(url: str, session: ClientSession, semaphore: Semaphore):
    print("Жду возможности захватить семафор...")
    async with semaphore:
        print("Семафор захвачен, отправляется запрос...")
        response = await session.get(url)
        print("Запрос завершен")
        return response.status


async def main():
    semaphore = Semaphore(10)
    async with ClientSession() as session:
        tasks = [get_url("https://www.example.com", session, semaphore) for _ in range(1000)]
        await asyncio.gather(*tasks)


asyncio.run(main())

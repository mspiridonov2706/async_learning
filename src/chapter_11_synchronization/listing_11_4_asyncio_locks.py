"""Использование блокировки asyncio"""

import asyncio
from asyncio import Lock

from src.util import delay


async def a(lock: Lock):
    print("Сопрограмма a ждет возможности захватить блокировку")
    async with lock:
        print("Сопрограмма a находится в критической секции")
        await delay(2)
        print("Сопрограмма a освободила блокировку")


async def b(lock: Lock):
    print("Сопрограмма b ждет возможности захватить блокировку")
    async with lock:
        print("Сопрограмма b находится в критической секции")
        await delay(2)
        print("Сопрограмма b освободила блокировку")


async def async_main():
    lock = Lock()
    await asyncio.gather(a(lock), b(lock))


def main():
    asyncio.run(async_main())

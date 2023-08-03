"""Использование await для ожидания результата сопрограммы"""

import asyncio


async def add_one(number: int) -> int:
    return number + 1


async def async_run() -> None:
    one_plus_one = await add_one(1)
    two_plus_one = await add_one(2)
    print(one_plus_one)
    print(two_plus_one)


def main():
    asyncio.run(async_run())

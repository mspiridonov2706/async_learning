"""Выполнение сопрограммы"""

import asyncio


async def coroutine_add_one(number: int) -> int:
    return number + 1


def main():
    result = asyncio.run(coroutine_add_one(1))
    print(result)

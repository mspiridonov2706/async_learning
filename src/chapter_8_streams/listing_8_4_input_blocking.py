"""Попытка выполнения задач в фоновом режиме"""

import asyncio

from src.util import delay


async def run():
    while True:
        delay_time = input('Введите время сна:')
        asyncio.create_task(delay(int(delay_time)))


def main():
    asyncio.run(run())


if __name__ == "__main__":
    main()

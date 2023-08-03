"""Неправильное использование спискового включения для создания и ожидания задач"""

import asyncio
from src.util import async_timed, delay


@async_timed()
async def async_main() -> None:
    delay_times = [3, 3, 3]
    [await asyncio.create_task(delay(seconds)) for seconds in delay_times]


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()

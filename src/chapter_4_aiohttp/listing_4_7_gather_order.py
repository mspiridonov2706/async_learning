"""Завершение допускающих ожидание объектов не по порядку"""

import asyncio
from src.util import delay


async def async_main() -> None:
    results = await asyncio.gather(delay(3), delay(1))
    print(results)


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()

"""Использование сопрограммы to_thread"""

import requests
import asyncio

from src.util import async_timed


def get_status_code(url: str) -> int:
    response = requests.get(url)
    return response.status_code


@async_timed()
async def async_main():
    urls = ['https://www.example.com' for _ in range(1000)]
    tasks = [asyncio.to_thread(get_status_code, url) for url in urls]
    results = await asyncio.gather(*tasks)
    print(results)


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()

"""Конкурентное выполнение запросов с помощью gather"""

import asyncio
import aiohttp
from . import fetch_status
from src.util import async_timed


@async_timed()
async def async_main() -> None:
    async with aiohttp.ClientSession() as session:
        urls = ['https://example.com' for _ in range(10)]
        requests = [fetch_status(session, url) for url in urls]
        status_codes = await asyncio.gather(*requests)
        print(status_codes)


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()

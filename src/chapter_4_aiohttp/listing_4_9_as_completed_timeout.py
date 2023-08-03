"""Задание тайм-аута для as_completed"""

import asyncio
import aiohttp
from . import fetch_status
from src.util import async_timed


@async_timed()
async def async_main() -> None:
    async with aiohttp.ClientSession() as session:
        fetchers = [
            fetch_status(session, 'https://www.example.com', 1),
            fetch_status(session, 'https://www.example.com', 10),
            fetch_status(session, 'https://www.example.com', 10),
            fetch_status(session, 'https://www.example.com', 3),
        ]
        for finished_task in asyncio.as_completed(fetchers, timeout=4):
            try:
                result = await finished_task
                print(result)
            except asyncio.TimeoutError:
                print('Произошел тайм-аут!')


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()

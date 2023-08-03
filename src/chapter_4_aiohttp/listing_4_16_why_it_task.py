"""Отмена медленного запроса"""

import asyncio
import aiohttp

from . import fetch_status
from src.util import async_timed


@async_timed()
async def async_main() -> None:
    async with aiohttp.ClientSession() as session:
        api_a = fetch_status(session, 'https://www.example.com')
        api_b = fetch_status(session, 'https://www.example.com', delay=2)
        _, pending = await asyncio.wait([api_a, api_b], timeout=1)
        for task in pending:
            if task is api_b:
                print('API B слишком медленный, отмена')
                task.cancel()


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()

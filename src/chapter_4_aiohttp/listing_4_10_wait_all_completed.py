"""Изучение поведения wait по умолчанию"""

import asyncio
import aiohttp
from . import fetch_status
from src.util import async_timed


@async_timed()
async def async_main() -> None:
    async with aiohttp.ClientSession() as session:
        fetchers = [
            asyncio.create_task(fetch_status(session, 'https://example.com', 1)),
            asyncio.create_task(fetch_status(session, 'https://example.com', 4)),
        ]
        done, pending = await asyncio.wait(fetchers)

        print(f'Число завершившихся задач: {len(done)}')
        print(f'Число ожидающих задач: {len(pending)}')

        for done_task in done:
            result = await done_task
            print(result)


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()

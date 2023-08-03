"""Обработка всех результатов по мере поступления"""

import asyncio
import aiohttp

from . import fetch_status
from src.util import async_timed


@async_timed()
async def async_main() -> None:
    async with aiohttp.ClientSession() as session:
        url = 'https://www.example.com'
        pending = [
            asyncio.create_task(fetch_status(session, url)),
            asyncio.create_task(fetch_status(session, url)),
            asyncio.create_task(fetch_status(session, url)),
        ]
        while pending:
            done, pending = await asyncio.wait(pending, return_when=asyncio.FIRST_COMPLETED)

            print(f'Число завершившихся задач: {len(done)}')
            print(f'Число ожидающих задач: {len(pending)}')

            for done_task in done:
                print(await done_task)


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()

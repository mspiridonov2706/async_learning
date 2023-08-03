"""Обработка исключений при использовании wait"""

import asyncio
import aiohttp
import logging

from . import fetch_status
from src.util import async_timed


@async_timed()
async def async_main() -> None:
    async with aiohttp.ClientSession() as session:
        good_request = fetch_status(session, 'https://www.example.com', 4)
        bad_request = fetch_status(session, 'python://bad', 1)
        fetchers = [
            asyncio.create_task(good_request),
            asyncio.create_task(bad_request),
        ]
        done, pending = await asyncio.wait(fetchers)

        print(f'Число завершившихся задач: {len(done)}')
        print(f'Число ожидающих задач: {len(pending)}')

        for done_task in done:
            # result = await done_task возбудит исключение
            if done_task.exception() is None:
                print(done_task.result())
            else:
                logging.error("При выполнении запроса возникло исключение", exc_info=done_task.exception())


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()

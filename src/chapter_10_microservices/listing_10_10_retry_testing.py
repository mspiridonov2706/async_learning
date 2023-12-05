"""Сопрограмма retry"""

import asyncio
from src.chapter_10_microservices.listing_10_9_retry_coroutine import retry, TooManyRetries


async def async_main():
    async def always_fail():
        raise Exception("А я грохнулась!")

    async def always_timeout():
        await asyncio.sleep(0.5)

    try:
        await retry(always_fail, max_retries=3, timeout=0.1, retry_interval=0.1)
    except TooManyRetries:
        print("Слишком много попыток!")

    try:
        await retry(always_timeout, max_retries=3, timeout=0.1, retry_interval=0.1)
    except TooManyRetries:
        print("Слишком много попыток!")


def main():
    asyncio.run(async_main())

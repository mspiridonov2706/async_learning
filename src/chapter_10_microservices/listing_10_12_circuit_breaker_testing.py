"""Прерыватель в действии"""

import asyncio
from src.chapter_10_microservices.listing_10_11_circuit_breaker import CircuitBreaker


async def async_main():
    async def slow_callback():
        await asyncio.sleep(2)

    cb = CircuitBreaker(slow_callback, timeout=1.0, time_window=5, max_failures=2, reset_interval=5)

    for _ in range(4):
        try:
            await cb.request()
        except Exception as e:
            pass

    print("Засыпаю на 5 с, чтобы прерыватель замкнулся...")
    await asyncio.sleep(5)

    for _ in range(4):
        try:
            await cb.request()
        except Exception as e:
            pass


def main():
    asyncio.run(async_main())

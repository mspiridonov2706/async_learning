"""Изменение продолжительности медленного обратного вызова"""


import asyncio

from src.util import async_timed


@async_timed()
async def async_main():
    loop = asyncio.get_event_loop()
    loop.slow_callback_duration = .250


def main():
    asyncio.run(async_main(), debug=True)

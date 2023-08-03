"""Первое применение sleep"""

import asyncio


async def hello_world_message() -> str:
    await asyncio.sleep(2)
    return 'Hello World!'


async def async_main() -> None:
    message = await hello_world_message()
    print(message)


def main():
    asyncio.run(async_main())

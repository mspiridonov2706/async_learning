"""Повторно используемая сопрограмма delay"""

import asyncio


async def delay(delay_seconds: int) -> int:
    print(f'засыпаю на {delay_seconds} с')
    if delay_seconds == 1:
        raise Exception
    await asyncio.sleep(delay_seconds)
    print(f'сон в течение {delay_seconds} с закончился')
    return delay_seconds

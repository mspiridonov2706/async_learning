"""Сопрограммы на основе генераторов"""

import asyncio


@asyncio.coroutine  # deprecated after python 3.11
def my_coroutine():
    print("Засыпаю!")
    yield from asyncio.sleep(1)
    print("Проснулась!")


asyncio.run(my_coroutine())

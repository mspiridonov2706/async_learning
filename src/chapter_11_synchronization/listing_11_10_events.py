"""Операции с событиями"""

import asyncio
import functools
from asyncio import Event


def trigger_event(event: Event):
    print("Активируется событие!")
    event.set()


async def do_work_on_event(event: Event):
    print("Ожидаю события...")
    await event.wait()  # Ждать события
    print("Работаю!")
    await asyncio.sleep(1)  # Когда событие произойдет, блокировка снимается, и мы можем начать работу
    print("Работа закончена!")
    event.clear()  # Сбросить событие, в результате чего последующие обращения к wait блокируются


async def main():
    event = asyncio.Event()
    asyncio.get_running_loop().call_later(5.0, functools.partial(trigger_event, event))
    await asyncio.gather(do_work_on_event(event), do_work_on_event(event))


asyncio.run(main())

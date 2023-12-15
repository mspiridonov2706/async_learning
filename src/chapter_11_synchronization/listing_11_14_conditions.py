"""Иллюстрация условий"""

import asyncio
from asyncio import Condition


async def do_work(condition: Condition):
    while True:
        print("Ожидаю блокировки условия...")
        async with condition:
            print("Блокировка захвачена, освобождаю и жду выполнения условия...")
            await condition.wait()
            print("Условие выполнено, вновь захватываю блокировку и начинаю работать...")
            await asyncio.sleep(1)
        print("Работа закончена, блокировка освобождена.")


async def fire_event(condition: Condition):
    while True:
        await asyncio.sleep(5)
        print("Перед уведомлением, захватываю блокировку условия...")
        async with condition:
            print("Блокировка захвачена, уведомляю всех исполнителей.")
            condition.notify_all()
        print("Исполнители уведомлены, освобождаю блокировку.")


async def main():
    condition = Condition()
    asyncio.create_task(fire_event(condition))
    await asyncio.gather(do_work(condition), do_work(condition))


asyncio.run(main())

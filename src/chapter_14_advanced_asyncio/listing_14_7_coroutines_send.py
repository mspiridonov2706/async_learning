"""Использование send для сопрограмм"""


async def say_hello():
    print("Привет!")


async def say_goodbye():
    print("Пока!")


async def meet_and_greet():
    await say_hello()
    await say_goodbye()


coro = meet_and_greet()
coro.send(None)

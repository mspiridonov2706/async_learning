"""Инициализация пула процессов"""

from concurrent.futures import ProcessPoolExecutor
import asyncio
from multiprocessing import Value


shared_counter: Value


def init(counter: Value):
    global shared_counter
    shared_counter = counter


def increment():
    with shared_counter.get_lock():
        shared_counter.value += 1


async def async_main():
    counter = Value('d', 0)
    with ProcessPoolExecutor(initializer=init, initargs=(counter,)) as pool:
        await asyncio.get_running_loop().run_in_executor(pool, increment)
        print(counter.value)


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()

"""Асинхронное получение результатов от пула процессов"""

from multiprocessing import Pool
import time


def say_hello(name: str) -> str:
    time.sleep(5)
    return f'Привет, {name}'


def main():
    with Pool() as process_pool:
        hi_jeff = process_pool.apply_async(say_hello, args=('Jeff',))
        hi_john = process_pool.apply_async(say_hello, args=('John',))
        print(hi_jeff.get())
        print(hi_john.get())


if __name__ == "__main__":
    main()

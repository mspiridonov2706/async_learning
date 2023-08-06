"""Исполнители пула процессов"""

import time
from concurrent.futures import ProcessPoolExecutor


def count(count_to: int) -> int:
    start = time.time()
    counter = 0
    while counter < count_to:
        counter = counter + 1
    end = time.time()
    print(f'Закончен подсчет до {count_to} за время {end - start}')
    return counter


def main():
    with ProcessPoolExecutor() as process_pool:
        numbers = [1, 100, 1000, 100000, 100000000]
        for result in process_pool.map(count, numbers):
            print(result)


if __name__ == "__main__":
    main()

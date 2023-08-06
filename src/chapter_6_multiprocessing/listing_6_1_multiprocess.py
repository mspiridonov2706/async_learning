"""Два параллельных процесса"""

import time
from multiprocessing import Process


def count(count_to: int) -> int:
    start = time.time()
    counter = 0
    while counter < count_to:
        counter = counter + 1
    end = time.time()
    print(f'Закончен подсчет до {count_to} за время {end - start}')
    return counter


def main():
    start_time = time.time()
    to_one_hundred_million = Process(target=count, args=(100000000,))
    to_two_hundred_million = Process(target=count, args=(200000000,))

    to_one_hundred_million.start()
    to_two_hundred_million.start()

    to_one_hundred_million.join()
    to_two_hundred_million.join()
    end_time = time.time()

    print(f'Полное время работы {end_time-start_time}')


if __name__ == "__main__":
    main()

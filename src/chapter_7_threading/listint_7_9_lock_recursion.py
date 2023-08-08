"""Блокировки и рекурсия"""

from threading import Lock, Thread
from typing import List


list_lock = Lock()  # для корректной работы нудно использовать RLock вместо Lock


def sum_list(int_list: List[int]) -> int:
    print('Ожидание блокировки...')
    with list_lock:
        print('Блокировка захвачена.')
        if len(int_list) == 0:
            print('Суммирование завершено.')
            return 0
        else:
            head, *tail = int_list
            print('Суммируется остаток списка.')
            return head + sum_list(tail)


def main():
    thread = Thread(target=sum_list, args=([1, 2, 3, 4],))
    thread.start()
    thread.join()


if __name__ == "__main__":
    main()

"""Основы будущих объектов"""

from asyncio import Future


def main():
    my_future = Future()
    print(f'my_future готов? {my_future.done()}')
    my_future.set_result(42)
    print(f'my_future готов? {my_future.done()}')
    print(f'Какой результат хранится в my_future? {my_future.result()}')

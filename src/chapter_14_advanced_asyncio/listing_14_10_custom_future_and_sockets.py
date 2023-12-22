"""Сокеты и будущие объекты"""


import functools
import selectors
import socket
from selectors import BaseSelector

from src.chapter_14_advanced_asyncio.listing_14_8_custom_future import CustomFuture


def accept_connection(future: CustomFuture, connection: socket):
    print(f"Получен запрос на подключение от {connection}!")
    future.set_result(connection)


async def sock_accept(sel: BaseSelector, sock) -> socket:
    print("Регистрируется сокет для прослушивания подключений")
    future = CustomFuture()
    sel.register(sock, selectors.EVENT_READ, functools.partial(accept_connection, future))
    print("Прослушиваю запросы на подключение...")
    connection: socket = await future
    return connection


async def async_main(sel: BaseSelector):
    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(("127.0.0.1", 8000))
    sock.listen()
    sock.setblocking(False)
    print("Ожидаю подключения к сокету!")
    connection = await sock_accept(sel, sock)
    print(f"Получено подключение {connection}!")


def main():
    selector = selectors.DefaultSelector()
    coro = async_main(selector)

    while True:
        try:
            coro.send(None)
            events = selector.select()
            for key, _ in events:
                print("Обрабатываются события селектора...")
                callback = key.data
                callback(key.fileobj)
        except StopIteration as _:
            print("Приложение завершилось!")
            break

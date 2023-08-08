"""Многопоточный эхо-сервер"""

from threading import Thread
import socket


def echo(client: socket.socket):
    while True:
        data = client.recv(2048)
        print(f'Получно {data}, отправляю!')
        client.sendall(data)


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind(('127.0.0.1', 8000))
        server.listen()
        while True:
            connection, address = server.accept()
            print(f'Подключен {address}')
            thread = Thread(target=echo, args=(connection,))
            thread.start()


if __name__ == "__main__":
    main()

"""Подключение нескольких клиентов"""

import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ('127.0.0.1', 8000)
server_socket.bind(server_address)
server_socket.listen()
server_socket.setblocking(False)  # Пометить серверный сокет как неблокирующий

connections: list[socket.socket] = []
try:
    while True:
        connection, client_address = server_socket.accept()
        connection.setblocking(False)  # Пометить клиентский сокет как неблокирующий

        print(f'Получен запрос на подключение от {client_address}!')
        connections.append(connection)
        for connection in connections:
            print("lol")
            buffer = b''
            while buffer[-2:] != b'\r\n':
                data = connection.recv(2)
                if not data:
                    break
                else:
                    print(f'Получены данные: {data}!')
                    buffer = buffer + data
            print(f"Все данные: {buffer}")
            connection.send(buffer)
finally:
    server_socket.close()

"""Запуск сервера и прослушивание порта для подключения"""

import socket


# socket.AF_INET тип адреса, в данном случае адрес будет содержать имя хостаи номер порта
# socket.SOCK_STREAM, означает, что для взаимодействия будет использоваться протокол TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Это позволит повторно использовать номер порта, после того как мы остановим и заново запустим приложение,
# избегнув тем самым ошибки «Адрес уже используется».
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ('127.0.0.1', 8000)  # Задать адрес сокета, 127.0.0.1:8000
server_socket.bind(server_address)  # Прослушивать запросы на подключение, или «открыть почтовое отделение»
server_socket.listen()

connection, client_address = server_socket.accept()  # Дождаться подключения и выделить клиенту почтовый ящик
print(f'Получен запрос на подключение от {client_address}!')

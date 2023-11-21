"""Чат-сервер"""

import asyncio
import logging
from asyncio import StreamReader, StreamWriter


class ChatServer:
    def __init__(self):
        self._username_to_writer: dict[str, StreamWriter] = {}

    async def start_chat_server(self, host: str, port: int):
        server = await asyncio.start_server(self.client_connected, host, port)
        async with server:
            await server.serve_forever()

    async def client_connected(self, reader: StreamReader, writer: StreamWriter):
        "Ждать, пока клиент отправит допустимое имя пользователя; в противном случае отключить его"

        command = await reader.readline()
        print(f"CONNECTED {reader} {writer}")
        command, args = command.split(b" ")
        if command == b"CONNECT":
            username = args.replace(b"\n", b"").decode()
            self._add_user(username, reader, writer)
            await self._on_connect(username, writer)
        else:
            logging.error("Получена недопустимая команда от клиента, отключается.")
            writer.close()
            await writer.wait_closed()

    def _add_user(self, username: str, reader: StreamReader, writer: StreamWriter):
        """
        Сохранить экземпляр потокового писателя для данного пользователя и создать задачу,
        прослушивающую его сообщения
        """
        self._username_to_writer[username] = writer
        asyncio.create_task(self._listen_for_messages(username, reader))

    async def _on_connect(self, username: str, writer: StreamWriter):
        "После подключения пользователя уведомить об этом всех остальных"
        writer.write(f"Добро пожаловать! Подключено пользователей: {len(self._username_to_writer)}!\n".encode())
        await writer.drain()
        await self._notify_all(f"Подключился {username}!\n")

    async def _remove_user(self, username: str):
        writer = self._username_to_writer[username]
        del self._username_to_writer[username]
        try:
            writer.close()
            await writer.wait_closed()
        except Exception as e:
            logging.exception("Ошибка при закрытии клиентского писателя, игнорируется.", exc_info=e)

    async def _listen_for_messages(self, username: str, reader: StreamReader):
        "Прослушивать сообщения от клиента и рассылать их всем остальным клиентам. Ждать сообщения не более минуты"
        try:
            while (data := await asyncio.wait_for(reader.readline(), 60)) != b"":
                await self._notify_all(f"{username}: {data.decode()}")
            await self._notify_all(f"{username} has left the chat\n")
        except Exception as e:
            logging.exception("Ошибка при чтении данных от клиента.", exc_info=e)
            await self._remove_user(username)

    async def _notify_all(self, message: str):
        "Отправить сообщение всем подключенным клиентам и удалить отключившихся клиентов"
        inactive_users = []
        for username, writer in self._username_to_writer.items():
            try:
                writer.write(message.encode())
                await writer.drain()
            except ConnectionError as e:
                logging.exception("Ошибка при записи данных клиенту.", exc_info=e)
                inactive_users.append(username)
        [await self._remove_user(username) for username in inactive_users]


async def async_main():
    chat_server = ChatServer()
    await chat_server.start_chat_server("127.0.0.1", 8000)


def main() -> None:
    asyncio.run(async_main())


if __name__ == "__main__":
    main()

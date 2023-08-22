"""Выполнение HTTP-запроса с помощью транспортного механизма и протокола"""

import asyncio
from asyncio import Transport, Future, AbstractEventLoop


class HTTPGetClientProtocol(asyncio.Protocol):
    def __init__(self, host: str, loop: AbstractEventLoop):
        self._host: str = host
        self._future: Future = loop.create_future()
        self._transport: Transport | None = None
        self._response_buffer: bytes = b''

    # Ждать внутренний будущий объект, пока не будет получен ответ от сервера
    async def get_response(self):
        return await self._future

    # Создать РЕЕ-запрос
    def _get_request_bytes(self) -> bytes:
        request = f"GET / HTTP/1.1\r\n" \
                  f"Connection: close\r\n" \
                  f"Host: {self._host}\r\n\r\n"
        return request.encode()

    # После того как подключение установлено, использовать транспорт для отправки запроса
    def connection_made(self, transport: Transport):
        print(f'Создано подключение к {self._host}')
        self._transport = transport
        self._transport.write(self._get_request_bytes())

    # Получив данные, сохранить их во внутреннем буфере
    def data_received(self, data):
        print('Получены данные!')
        self._response_buffer = self._response_buffer + data

    # После закрытия подключения завершить будущий объект, скопировав в него данные из буфера
    def eof_received(self) -> bool | None:
        self._future.set_result(self._response_buffer.decode())
        return False

    # Если подключение было закрыто без ошибок, не делать ничего; иначе завершить будущий объект исключением
    def connection_lost(self, exc: Exception | None) -> None:
        if exc is None:
            print('Подключение закрыто без ошибок.')
        else:
            self._future.set_exception(exc)

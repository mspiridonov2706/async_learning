"""Использование разработанного API в сервере загрузки файлов"""

import asyncio
from asyncio import StreamReader, StreamWriter
from src.chapter_11_synchronization.listing_11_11_events_upload_files import FileUpload


class FileServer:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.upload_event = asyncio.Event()

    async def start_server(self):
        server = await asyncio.start_server(self._client_connected, self.host, self.port)
        await server.serve_forever()

    async def dump_contents_on_complete(self, upload: FileUpload):
        file_contents = await upload.get_contents()
        print(file_contents)

    def _client_connected(self, reader: StreamReader, writer: StreamWriter):
        upload = FileUpload(reader, writer)
        upload.listen_for_uploads()
        asyncio.create_task(self.dump_contents_on_complete(upload))


async def async_main():
    server = FileServer("127.0.0.1", 9000)
    await server.start_server()


def main():
    asyncio.run(async_main())

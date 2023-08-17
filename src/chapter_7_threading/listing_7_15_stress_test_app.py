"""Приложение для нагрузочного тестирования"""

import asyncio
from asyncio import AbstractEventLoop

from threading import Thread
from src.chapter_7_threading.listing_7_14_tkinter_gui import LoadTester


class ThreadedEventLoop(Thread):
    def __init__(self, loop: AbstractEventLoop):
        super().__init__()
        self._loop = loop
        self.daemon = True

    def run(self):
        self._loop.run_forever()


def main():
    loop = asyncio.new_event_loop()
    asyncio_thread = ThreadedEventLoop(loop)
    asyncio_thread.start()
    app = LoadTester(loop)
    app.mainloop()

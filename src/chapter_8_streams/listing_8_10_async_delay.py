"""Приложение для асинхронной задержки"""

import asyncio
import os
import tty
import sys
from collections import deque

from .listing_8_5_stdin_reader import create_stdin_reader
from .listing_8_7_input_utils import (
    move_to_bottom_of_screen,
    delete_line,
    restore_cursor_position,
    save_cursor_position,
    move_to_top_of_screen,
)
from .listing_8_8_read_stdin import read_line
from .listing_8_9_message_storage import MessageStore


async def sleep(delay: int, message_store: MessageStore):
    await message_store.append(f"Начало задержки {delay}")
    await asyncio.sleep(delay)
    await message_store.append(f"Конец задержки {delay}")


async def run():
    tty.setcbreak(sys.stdin)
    os.system("clear")

    rows = move_to_bottom_of_screen()

    async def redraw_output(items: deque):
        save_cursor_position()
        move_to_top_of_screen()
        for item in items:
            delete_line()
            print(item)
        restore_cursor_position()

    messages = MessageStore(redraw_output, rows - 1)
    stdin_reader = await create_stdin_reader()
    while True:
        line = await read_line(stdin_reader)
        print("lalal")
        delay_time = int(line)
        await asyncio.create_task(sleep(delay_time, messages))


def main():
    asyncio.run(run())

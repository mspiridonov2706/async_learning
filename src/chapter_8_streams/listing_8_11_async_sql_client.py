"""Асинхронный командный SQL-клиент"""

import asyncio
import asyncpg
import os
import tty
from collections import deque
from asyncpg.pool import Pool


from src.settings import settings
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


async def run_query(query: str, pool: Pool, message_store: MessageStore):
    async with pool.acquire() as connection:
        try:
            await asyncio.sleep(2)
            result = await connection.fetchrow(query)
            await message_store.append(f"Выбрано {len(result)} строк по запросу:{query}")
        except Exception as e:
            await message_store.append(f"Получено исключение {e} от: {query}")


async def async_main():
    tty.setcbreak(0)
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

    connection_pool = asyncpg.create_pool(
        host=settings.postgres.host,
        port=settings.postgres.port,
        user=settings.postgres.user,
        password=settings.postgres.password,
        database=settings.postgres.db,
        min_size=6,
        max_size=6,
    )

    async with connection_pool as pool:
        while True:
            # print("lol1")
            query = await read_line(stdin_reader)
            asyncio.create_task(run_query(query, pool, messages))
            print()


def main() -> None:
    asyncio.run(async_main())

"""Вложенная транзакция"""

from __future__ import annotations

import logging

import asyncio
import asyncpg

from src.settings import settings


async def async_main():
    connection = await asyncpg.connect(
        host=settings.postgres.host,
        port=settings.postgres.port,
        user=settings.postgres.user,
        password=settings.postgres.password,
        database=settings.postgres.db,
    )
    async with connection.transaction():
        await connection.execute("INSERT INTO brand VALUES(DEFAULT, 'my_new_brand')")
        try:
            async with connection.transaction():
                await connection.execute("INSERT INTO product_color VALUES(1, 'black')")
        except Exception as ex:
            logging.warning('Ошибка при вставке цвета товара игнорируется', exc_info=ex)
    await connection.close()


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()

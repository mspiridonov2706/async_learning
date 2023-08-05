"""Потоковая обработка результатов"""

from __future__ import annotations

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
    query = 'SELECT product_id, product_name FROM product'
    async with connection.transaction():
        async for product in connection.cursor(query):
            print(product)
    await connection.close()


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()

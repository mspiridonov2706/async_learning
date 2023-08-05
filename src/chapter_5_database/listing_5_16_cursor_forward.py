"""Перемещение по курсору и выборка записей"""

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
    async with connection.transaction():
        query = 'SELECT product_id, product_name from product'
        cursor = await connection.cursor(query)
        await cursor.forward(500)
        products = await cursor.fetch(100)
        for product in products:
            print(product)
    await connection.close()


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()

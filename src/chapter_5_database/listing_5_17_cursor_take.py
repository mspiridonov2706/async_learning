"""Получение заданного числа элементов с помощью асинхронного генератора"""

from __future__ import annotations

import asyncio
import asyncpg

from src.settings import settings


async def take(generator, to_take: int):
    item_count = 0
    async for item in generator:
        if item_count > to_take - 1:
            return
        item_count = item_count + 1
        yield item


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
        product_generator = connection.cursor(query)
        async for product in take(product_generator, 5):
            print(product)
        print('Получены первые пять товаров!')
    await connection.close()


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()

"""Создание пула подключений и конкурентное выполнение запросов"""

from __future__ import annotations

import asyncio
import asyncpg
from asyncpg import Pool, Record

from src.settings import settings


product_query = """
    SELECT
        p.product_id,
        p.product_name,
        p.brand_id,
        s.sku_id,
        pc.product_color_name,
        ps.product_size_name
    FROM product as p
        JOIN sku as s on s.product_id = p.product_id
        JOIN product_color as pc on pc.product_color_id = s.product_color_id
        JOIN product_size as ps on ps.product_size_id = s.product_size_id
    WHERE p.product_id = 100
"""


async def query_product(pool: Pool[Record]):
    async with pool.acquire() as connection:
        return await connection.fetchrow(product_query)


async def async_main():
    async with asyncpg.create_pool(
        host=settings.postgres.host,
        port=settings.postgres.port,
        user=settings.postgres.user,
        password=settings.postgres.password,
        database=settings.postgres.db,
        min_size=6,
        max_size=6,
    ) as pool:
        response = await asyncio.gather(query_product(pool), query_product(pool))
        print(response)


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()

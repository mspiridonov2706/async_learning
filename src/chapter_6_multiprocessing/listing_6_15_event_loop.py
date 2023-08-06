"""Цикл событий в каждом процессе"""

from __future__ import annotations

import asyncio
import asyncpg
from asyncpg import Pool, Record
from concurrent.futures.process import ProcessPoolExecutor

from src.settings import settings
from src.util import async_timed


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


@async_timed()
async def query_products_concurrently(pool: Pool[Record], query_amount: int):
    queries = [query_product(pool) for _ in range(query_amount)]
    return await asyncio.gather(*queries)


def run_in_new_loop(num_queries: int) -> list[dict]:
    async def run_queries():
        async with asyncpg.create_pool(
            host=settings.postgres.host,
            port=settings.postgres.port,
            user=settings.postgres.user,
            password=settings.postgres.password,
            database=settings.postgres.db,
            min_size=6,
            max_size=6,
        ) as pool:
            return await query_products_concurrently(pool, num_queries)

    results = [dict(result) for result in asyncio.run(run_queries())]
    return results


@async_timed()
async def async_main():
    loop = asyncio.get_running_loop()
    pool = ProcessPoolExecutor()
    tasks = [loop.run_in_executor(pool, run_in_new_loop, 10000) for _ in range(1)]
    all_results = await asyncio.gather(*tasks)
    total_queries = sum([len(result) for result in all_results])
    print(f'Извлечено товаров из базы данных: {total_queries}.')


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()

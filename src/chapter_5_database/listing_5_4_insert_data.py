"""Вставка и выборка марок"""

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

    await connection.execute("INSERT INTO brand VALUES(DEFAULT, 'Levis')")
    await connection.execute("INSERT INTO brand VALUES(DEFAULT, 'Seven')")

    brand_query = "SELECT brand_id, brand_name FROM brand"
    results = await connection.fetch(brand_query)
    for brand in results:
        print(f'id: {brand["brand_id"]}, name: {brand["brand_name"]}')
    await connection.close()


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()

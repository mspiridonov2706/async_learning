"""Ручное управление транзакцией"""

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
    transaction = connection.transaction()
    await transaction.start()
    try:
        await connection.execute("INSERT INTO brand VALUES(DEFAULT, 'brand_1')")
        await connection.execute("INSERT INTO brand VALUES(DEFAULT, 'brand_2')")
    except asyncpg.PostgresError:
        print('Ошибка, транзакция откатывается!')
        await transaction.rollback()
    else:
        print('Ошибки нет, транзакция фиксируется!')
        await transaction.commit()

    query = """SELECT brand_name FROM brand WHERE brand_name LIKE 'brand%'"""
    brands = await connection.fetch(query)
    print(brands)

    await connection.close()


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()

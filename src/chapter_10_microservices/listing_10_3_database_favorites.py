"""Таблица избранных товаров пользователя"""

import asyncio
import asyncpg

from src.settings import settings

CREATE_TABLE = """CREATE TABLE user_favorite (user_id INT NOT NULL, product_id INT NOT NULL);"""
INSERT_DATA = """INSERT INTO user_favorite VALUES (1, 1), (1, 2), (1, 3), (3, 1), (3, 2), (3, 3);"""


async def async_main():
    connection = await asyncpg.connect(
        host=settings.postgres.host,
        port=settings.postgres.port,
        user=settings.postgres.user,
        password=settings.postgres.password,
        database=settings.postgres.db_favorites,
    )
    statements = [
        CREATE_TABLE,
        INSERT_DATA,
    ]

    for statement in statements:
        print(statement)
        status = await connection.execute(statement)
        print(status)
    await connection.close()


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()

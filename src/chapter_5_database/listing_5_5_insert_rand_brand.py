"""Вставка и выборка марок"""

import asyncio
import asyncpg
from asyncpg import Connection
from random import sample

from src.settings import settings


def load_common_words() -> list[str]:
    with open('src/chapter_5_database/common_words.txt') as common_words:
        return common_words.readlines()


def generate_brand_names(words: list[str]) -> list[tuple[str]]:
    return [(words[index],) for index in sample(range(100), 100)]


async def insert_brands(common_words: list[str], connection: Connection) -> None:
    brands = generate_brand_names(common_words)
    insert_brands = "INSERT INTO brand VALUES(DEFAULT, $1)"
    await connection.executemany(insert_brands, brands)


async def async_main():
    connection = await asyncpg.connect(
        host=settings.postgres.host,
        port=settings.postgres.port,
        user=settings.postgres.user,
        password=settings.postgres.password,
        database=settings.postgres.db,
    )

    common_words = load_common_words()
    await insert_brands(common_words, connection)
    await connection.close()


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()

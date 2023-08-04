"""Асинхронный контекстный менеджер, ожидающий подключения клиента"""

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
    version = connection.get_server_version()
    print(f'Подключено! Версия Postgres равна {version}')
    await connection.close()


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()

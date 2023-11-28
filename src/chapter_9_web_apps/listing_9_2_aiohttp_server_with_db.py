"""Подключение к базе данных о товарах"""

import asyncpg
from aiohttp import web
from aiohttp.web_app import Application
from aiohttp.web_request import Request
from aiohttp.web_response import Response
from asyncpg import Record
from asyncpg.pool import Pool
from typing import List, Dict

from src.settings import settings


routes = web.RouteTableDef()
DB_KEY = "database"


async def create_database_pool(app: Application):
    print("Создается пул подключений.")
    pool = await asyncpg.create_pool(
        host=settings.postgres.host,
        port=settings.postgres.port,
        user=settings.postgres.user,
        password=settings.postgres.password,
        database=settings.postgres.db,
        min_size=6,
        max_size=6,
    )
    app[DB_KEY] = pool


async def destroy_database_pool(app: Application):
    print("Уничтожается пул подключений.")
    pool: Pool = app[DB_KEY]
    await pool.close()


@routes.get("/brands")
async def brands(request: Request) -> Response:
    pool: Pool = request.app[DB_KEY]

    async with pool.acquire() as connection:
        brand_query = "SELECT brand_id, brand_name FROM brand"
        results: List[Record] = await connection.fetch(brand_query)
        result_as_dict: List[Dict] = [dict(brand) for brand in results]

    return web.json_response(result_as_dict)


def main():
    app = web.Application()
    app.on_startup.append(create_database_pool)
    app.on_cleanup.append(destroy_database_pool)

    app.add_routes(routes)
    # web.run_app(app)
    return app


app = main()

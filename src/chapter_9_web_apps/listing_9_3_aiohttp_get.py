"""Получение конкретного товара"""

from aiohttp import web
from aiohttp.web_request import Request
from aiohttp.web_response import Response
from asyncpg import Record
from asyncpg.pool import Pool

from .listing_9_2_aiohttp_server_with_db import create_database_pool, destroy_database_pool, DB_KEY


routes = web.RouteTableDef()


@routes.get("/products/{id}")
async def get_product(request: Request) -> Response:
    try:
        str_id = request.match_info["id"]
        product_id = int(str_id)

        query = """SELECT product_id, product_name, brand_id FROM product WHERE product_id = $1"""

        pool: Pool = request.app[DB_KEY]
        async with pool.acquire() as connection:
            result: Record | None = await connection.fetchrow(query, product_id)
            if not result:
                raise web.HTTPNotFound()
            return web.json_response(dict(result))
    except ValueError:
        raise web.HTTPBadRequest()


def main():
    app = web.Application()
    app.on_startup.append(create_database_pool)
    app.on_cleanup.append(destroy_database_pool)

    app.add_routes(routes)
    web.run_app(app)

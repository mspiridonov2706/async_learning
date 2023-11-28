"""Оконечная точка для создания товара"""

from aiohttp import web
from aiohttp.web_request import Request
from aiohttp.web_response import Response

from .listing_9_2_aiohttp_server_with_db import create_database_pool, destroy_database_pool, DB_KEY


routes = web.RouteTableDef()


@routes.post("/product")
async def create_product(request: Request) -> Response:
    PRODUCT_NAME = "product_name"
    BRAND_ID = "brand_id"

    if not request.can_read_body:
        raise web.HTTPBadGateway()

    body = await request.json()

    if PRODUCT_NAME in body and BRAND_ID in body:
        db = request.app[DB_KEY]
        await db.execute(
            """INSERT INTO product(product_id, product_name, brand_id) VALUES(DEFAULT, $1, $2)""",
            body[PRODUCT_NAME],
            int(body[BRAND_ID]),
        )

        return web.Response(status=201)
    else:
        raise web.HTTPBadRequest()


def main():
    app = web.Application()
    app.on_startup.append(create_database_pool)
    app.on_cleanup.append(destroy_database_pool)

    app.add_routes(routes)
    web.run_app(app)

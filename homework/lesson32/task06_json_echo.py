from aiohttp import web


async def echo(request: web.Request) -> web.Response:
    data = await request.json()

    return web.json_response(data)


app = web.Application()
app.router.add_post("/api/echo", echo)


if __name__ == "__main__":
    web.run_app(app)
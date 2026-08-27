from aiohttp import web


async def welcome(request: web.Request):
    return web.Response(
        text="<h1>Witaj na mojej stronie!</h1>",
        content_type="text/html",
    )


app = web.Application()
app.router.add_get("/", welcome)


if __name__ == "__main__":
    web.run_app(app)
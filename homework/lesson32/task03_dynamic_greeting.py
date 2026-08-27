from aiohttp import web


async def welcome(request: web.Request):
    return web.Response(
        text="<h1>Witaj na mojej stronie!</h1>",
        content_type="text/html",
    )


async def greet(request: web.Request):
    name = request.match_info["imie"]

    return web.Response(
        text=f"Witaj, {name}!",
        content_type="text/html",
    )


app = web.Application()
app.router.add_get("/", welcome)
app.router.add_get("/witaj/{imie}", greet)


if __name__ == "__main__":
    web.run_app(app)
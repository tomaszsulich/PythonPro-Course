from aiohttp import web


async def search(request: web.Request) -> web.Response:
    query = request.query.get("q")

    if query is None:
        return web.json_response(
            {"błąd": "Brak parametru q"}
        )

    if not query.strip():
        return web.json_response(
            {"błąd": "Parametr q nie może być pusty"}
        )

    return web.json_response(
        {"szukana_fraza": query}
    )


app = web.Application()
app.router.add_get("/api/search", search)


if __name__ == "__main__":
    web.run_app(app)
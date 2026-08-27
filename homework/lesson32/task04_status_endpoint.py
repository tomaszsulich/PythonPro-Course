from aiohttp import web
from datetime import datetime


async def get_status(request: web.Request) -> web.Response:
    return web.json_response(
        {
            "status": "OK",
            "server_time": datetime.now().isoformat(),
        }
    )


app = web.Application()
app.router.add_get("/api/status", get_status)


if __name__ == "__main__":
    web.run_app(app)
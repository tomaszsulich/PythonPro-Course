import random
from datetime import datetime
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Hello"}


@app.get("/time")
async def get_time() -> dict[str, str]:
    return {"time": datetime.now().isoformat()}


@app.get("/random")
async def get_random() -> dict[str, int]:
    return {"number": random.randint(1, 100)}
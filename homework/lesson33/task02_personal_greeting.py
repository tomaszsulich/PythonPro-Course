from fastapi import FastAPI, Path


app = FastAPI()


@app.get("/greet/{name}")
async def greet(name: str = Path(min_length=2)) -> dict[str, str]:
    return {"message": f"Cześć, {name}!"}
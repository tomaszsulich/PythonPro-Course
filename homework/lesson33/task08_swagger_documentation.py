from fastapi import FastAPI, Path


app = FastAPI(
    title="Simple Greeting API",
    description="Proste API demonstracyjne dla dokumentacji FastAPI."
)


@app.get("/greet/{name}", tags=["Greetings"])
async def greet(name: str = Path(min_length=2)) -> dict[str, str]:
    """
    Zwraca powitanie dla podanej osoby.

    Przykład:
    GET /greet/Tomek

    Odpowiedź:
    {"message": "Cześć, Tomek!"}
    """
    return {"message": f"Cześć, {name}!"}
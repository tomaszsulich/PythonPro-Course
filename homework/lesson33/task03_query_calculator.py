from fastapi import FastAPI, HTTPException


app = FastAPI()


@app.get("/calculate")
async def calculate(a: int, b: int, operation: str = "add") -> dict[str, int | float]:
    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    elif operation == "multiply":
        result = a * b
    elif operation == "divide":
        if b == 0:
            raise HTTPException(
                status_code=400,
                detail="Nie można dzielić przez zero."
            )
        result = a / b
    else:
        raise HTTPException(
            status_code=400,
            detail="Nieobsługiwana operacja."
        )

    return {"result": result}
from fastapi import Depends, FastAPI, Header, HTTPException, status


app = FastAPI()


async def verify_api_key(x_api_key: str = Header()) -> None:
    if x_api_key != "secret-key":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Nieprawidłowy klucz API."
        )


@app.get("/profile", dependencies=[Depends(verify_api_key)])
async def get_profile() -> dict[str, str]:
    return {"message": "Dostęp do profilu."}


@app.get("/settings", dependencies=[Depends(verify_api_key)])
async def get_settings() -> dict[str, str]:
    return {"message": "Dostęp do ustawień."}


@app.get("/reports", dependencies=[Depends(verify_api_key)])
async def get_reports() -> dict[str, str]:
    return {"message": "Dostęp do raportów."}
from fastapi import APIRouter


router = APIRouter(prefix="/authors", tags=["Authors"])


@router.get("")
async def get_authors() -> list[str]:
    return ["Adam Mickiewicz", "Wisława Szymborska"]
from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

cats = {1: {"id": 1, "name": "Filemon", "age": 3, "color": "black"},
        2: {"id": 2, "name": "Meow-tzun", "age": 2, "color": "black"}}


class Cat(BaseModel):
    id: int
    name: str
    age: int
    color: str


class CatPatch(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    color: Optional[str] = None


@app.get("/cats")
def get_cats():
    return list(cats.values())


@app.get("/cats/{cat_id}")
def get_cat(cat_id: int):
    if cat_id not in cats:
        raise HTTPException(status_code=404, detail="Cat not found")

    return cats[cat_id]


@app.post("/cats")
def create_cat(cat: Cat):
    cats[cat.id] = cat.dict()
    return cats[cat.id]


@app.put("/cats/{cat_id}")
def replace_cat(cat_id: int, cat: Cat):
    if cat_id not in cats:
        raise HTTPException(status_code=404, detail="Cat not found")

    cats[cat_id] = cat.dict()
    return cats[cat_id]


@app.patch("/cats/{cat_id}")
def update_cat(cat_id: int, cat_patch: CatPatch):
    if cat_id not in cats:
        raise HTTPException(status_code=404, detail="Cat not found")

    current = cats[cat_id]

    updates = cat_patch.dict(exclude_unset=True)

    current.update(updates)

    cats[cat_id] = current

    return current


@app.delete("/cats/{cat_id}")
def delete_cat(cat_id: int):
    if cat_id not in cats:
        raise HTTPException(status_code=404, detail="Cat not found")

    deleted = cats.pop(cat_id)

    return deleted

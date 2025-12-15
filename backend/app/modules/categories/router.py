from fastapi import APIRouter, HTTPException
from .schema import CategoryCreate, CategoryUpdate
from .service import *

router = APIRouter(prefix="/categories", tags=["Categories"])

@router.post("/")
def create(data: CategoryCreate):
    res = create_category(data.dict())
    if res.error:
        raise HTTPException(400, res.error.message)
    return res.data

@router.get("/")
def get_all():
    res = get_all_categories()
    return res.data

@router.put("/{category_id}")
def update(category_id: str, data: CategoryUpdate):
    res = update_category(category_id, data.dict())
    if res.error:
        raise HTTPException(400, res.error.message)
    return res.data

@router.delete("/{category_id}")
def delete(category_id: str):
    res = delete_category(category_id)
    if res.error:
        raise HTTPException(400, res.error.message)
    return {"message": "Category deleted"}

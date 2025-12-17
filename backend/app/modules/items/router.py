from fastapi import APIRouter, HTTPException
from .schema import ProductItemCreate, ProductItemUpdate
from .service import *

router = APIRouter(prefix="/items", tags=["Product Items"])

@router.post("/")
def create(data: ProductItemCreate):
    if not model_exists(str(data.model)):
        raise HTTPException(400, "Product model does not exist")

    payload = data.dict()
    payload["model"] = str(payload["model"])
    payload["sku"] = generate_sku(payload["model"])

    res = create_item(payload)
    if res.error:
        raise HTTPException(400, res.error.message)

    return res.data


@router.get("/")
def get_all():
    res = get_all_items()
    return res.data


@router.put("/{product_id}")
def update(product_id: str, data: ProductItemUpdate):
    res = update_item(product_id, data.dict(exclude_unset=True))
    if res.error:
        raise HTTPException(400, res.error.message)

    return res.data


@router.delete("/{product_id}")
def delete(product_id: str):
    res = delete_item(product_id)
    if res.error:
        raise HTTPException(400, res.error.message)

    return {"message": "Product item deleted"}

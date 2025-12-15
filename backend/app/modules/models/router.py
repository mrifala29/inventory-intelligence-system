from fastapi import APIRouter, HTTPException
from .schema import ProductModelCreate, ProductModelUpdate
from .service import *
from uuid import UUID

router = APIRouter(prefix="/models", tags=["Product Models"])

@router.post("/")
def create(data: ProductModelCreate):
    if not category_exists(data.category_id):
        raise HTTPException(
            status_code=400,
            detail="Category ID does not exist"
        )

    res = create_model(data.dict())
    if res.error:
        raise HTTPException(400, res.error.message)

    return res.data


@router.get("/")
def get_all():
    res = get_all_models()
    return res.data


@router.put("/{model_id}")
def update(model_id: UUID, data: ProductModelUpdate):
    res = update_model(model_id, data.dict(exclude_unset=True))
    if res.error:
        raise HTTPException(400, res.error.message)

    return res.data


@router.delete("/{model_id}")
def delete(model_id: UUID):
    res = delete_model(model_id)
    if res.error:
        raise HTTPException(400, res.error.message)

    return {"message": "Product model deleted"}

from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from uuid import UUID
from .service import *

router = APIRouter(prefix="/images", tags=["Product Images"])


@router.post("/")
def upload_image(
    product_id: UUID = Form(...),
    order_index: int | None = Form(None),
    file: UploadFile = File(...)
):
    product_id_str = str(product_id)

    if not product_exists(product_id_str):
        raise HTTPException(400, "Product item does not exist")

    image_url = upload_to_s3(file, product_id_str)

    payload = {
        "product_id": product_id_str,
        "image_url": image_url,
        "order_index": order_index
    }

    res = save_image(payload)
    if res.error:
        raise HTTPException(400, res.error.message)

    return res.data

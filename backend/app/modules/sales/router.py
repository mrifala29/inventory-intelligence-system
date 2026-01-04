from fastapi import APIRouter, HTTPException
from .schema import SalesCreate, SalesItemCreate
from .service import *

router = APIRouter(prefix="/sales", tags=["Sales"])


@router.post("/")
def create_sales_header(data: SalesCreate):
    customer_id = str(data.customer_id)

    if not customer_exists(customer_id):
        raise HTTPException(400, "Customer does not exist")

    payload = data.dict()
    payload["customer_id"] = customer_id

    res = create_sales(payload)
    if res.error:
        raise HTTPException(400, res.error.message)

    return res.data[0]


@router.post("/{sales_id}/items")
def add_sales_item(sales_id: str, data: SalesItemCreate):
    product_id = str(data.product_id)

    if not product_exists(product_id):
        raise HTTPException(400, "Product item does not exist")

    payload = data.dict()
    payload["sales_id"] = sales_id
    payload["product_id"] = product_id

    res = create_sales_item(payload)
    if res.error:
        raise HTTPException(400, res.error.message)

    return res.data

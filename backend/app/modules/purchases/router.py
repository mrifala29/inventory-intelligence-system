from fastapi import APIRouter, HTTPException
from .schema import PurchaseCreate, PurchaseItemCreate
from .service import *

router = APIRouter(prefix="/purchases", tags=["Purchases"])


@router.post("/")
def create_purchase_header(data: PurchaseCreate):
    customer_id = str(data.customer_id)
    
    if not customer_exists(customer_id):
        raise HTTPException(400, "Customer does not exist")
    
    payload = data.dict()
    payload["customer_id"] = customer_id
    
    res = create_purchase(payload)
    if res.error:
        raise HTTPException(400, res.error.message)
    
    return res.data[0]


@router.post("/{purchase_id}/items")
def add_purchase_item(purchase_id: str, data: PurchaseItemCreate):
    product_id = str(data.product_id)
    
    if not product_exists(product_id):
        raise HTTPException(400, "Product item does not exist")
    
    payload = data.dict()
    payload["purchase_id"] = purchase_id
    payload["product_id"] = product_id
    
    res = create_purchase_item(payload)
    if res.error:
        raise HTTPException(400, res.error.message)

    return res.data
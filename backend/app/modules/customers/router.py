from fastapi import APIRouter, HTTPException
from .schema import CustomerCreate, CustomerUpdate
from .service import *

router = APIRouter(prefix="/customers", tags=["Customers"])


@router.post("/")
def create(data: CustomerCreate):
    res = create_customer(data.dict())
    if res.error:
        raise HTTPException(400, res.error.message)
    return res.data


@router.get("/")
def get_all():
    res = get_all_customers()
    return res.data


@router.get("/{customer_id}")
def get_by_id(customer_id: str):
    res = get_customer_by_id(customer_id)
    if not res.data:
        raise HTTPException(404, "Customer not found")
    return res.data[0]


@router.put("/{customer_id}")
def update(customer_id: str, data: CustomerUpdate):
    res = update_customer(customer_id, data.dict(exclude_unset=True))
    if res.error:
        raise HTTPException(400, res.error.message)
    return res.data


@router.delete("/{customer_id}")
def delete(customer_id: str):
    res = delete_customer(customer_id)
    if res.error:
        raise HTTPException(400, res.error.message)
    return {"message": "Customer deleted"}

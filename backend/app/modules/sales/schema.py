from pydantic import BaseModel
from datetime import date, datetime
from uuid import UUID

class SalesCreate(BaseModel):
    customer_id: UUID
    date: date
    location: str
    transportation_cost: int
    bonus: str | None = None

class SalesItemCreate(BaseModel):
    product_id: UUID
    price: int
    additional_cost: int
    description_cost: str

class SalesResponse(BaseModel):
    sales_id: UUID
    customer_id: UUID
    date: date
    location: str
    transportation_cost: int
    bonus: str | None
    created_at: datetime

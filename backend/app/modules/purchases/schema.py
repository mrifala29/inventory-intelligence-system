from pydantic import BaseModel
from datetime import date, datetime
from uuid import UUID

class PurchaseCreate(BaseModel):
    customer_id: UUID
    date: date
    location: str
    transportation_cost: int
    bonus: str | None = None
    
class PurchaseItemCreate(BaseModel):
    product_id: UUID
    price: int
    additional_cost: int
    cost_description: str
    
class PurchaseResponse(BaseModel):
    purchase_id: UUID
    customer_id: UUID
    date: date
    location: str
    transportation_cost: int
    bonus: str | None = None
    created_at: datetime
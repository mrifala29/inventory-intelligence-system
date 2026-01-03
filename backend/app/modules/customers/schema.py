from pydantic import BaseModel
from datetime import datetime
from uuid import UUID

class CustomerCreate(BaseModel):
    name: str
    phone: str
    category: str
    address: str

class CustomerUpdate(BaseModel):
    name: str | None = None
    phone: str | None = None
    category: str | None = None
    address: str | None = None

class CustomerResponse(BaseModel):
    customer_id: UUID
    name: str
    phone: str
    category: str
    address: str
    created_at: datetime
    updated_at: datetime

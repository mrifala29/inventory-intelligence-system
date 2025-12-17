from pydantic import BaseModel
from datetime import datetime
from uuid import UUID

class ProductItemCreate(BaseModel):
    model: UUID
    state: str
    storage: int | None = None
    colour: str | None = None
    physical: str
    warranty_type: str | None = None
    warranty_state: str
    package: str
    condition: str
    defect: str

class ProductItemUpdate(BaseModel):
    state: str | None = None
    storage: int | None = None
    colour: str | None = None
    physical: str | None = None
    warranty_type: str | None = None
    warranty_state: str | None = None
    package: str | None = None
    condition: str | None = None
    defect: str | None = None

class ProductItemResponse(BaseModel):
    product_id: UUID
    model: UUID
    sku: str
    state: str
    storage: int | None
    condition: str
    created_at: datetime

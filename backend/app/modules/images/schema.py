from pydantic import BaseModel
from datetime import datetime
from uuid import UUID

class ProductImageCreate(BaseModel):
    product_id: UUID
    order_index: int | None = None

class ProductImageResponse(BaseModel):
    image_id: UUID
    product_id: UUID
    image_url: str
    order_index: int | None
    created_at: datetime

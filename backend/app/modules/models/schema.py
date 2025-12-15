from pydantic import BaseModel
from datetime import datetime
from uuid import UUID

class ProductModelCreate(BaseModel):
    category_id: str
    brand: str
    model_name: str
    production_year: int

class ProductModelUpdate(BaseModel):
    brand: str | None = None
    model_name: str | None = None
    production_year: int | None = None

class ProductModelResponse(BaseModel):
    product_model_id: UUID
    category_id: str
    brand: str
    model_name: str
    production_year: int
    created_at: datetime
    updated_at: datetime

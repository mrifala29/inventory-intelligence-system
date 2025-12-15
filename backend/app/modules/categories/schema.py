from pydantic import BaseModel
from datetime import datetime

class CategoryCreate(BaseModel):
    category_id: str
    category_name: str

class CategoryUpdate(BaseModel):
    category_name: str

class CategoryResponse(BaseModel):
    category_id: str
    category_name: str
    created_at: datetime
    updated_at: datetime

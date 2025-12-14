from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    description: str | None = None
    price: int

class ProductResponse(ProductCreate):
    id: str
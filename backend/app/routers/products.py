from fastapi import APIRouter, UploadFile, File
from app.schemas.product import ProductCreate
from app.services.supabase_service import create_product, get_products
from app.services.s3_service import upload_image
import uuid

router = APIRouter()

@router.post("/")
def create(product: ProductCreate):
    result = create_product(product.dict())
    return result.data

@router.get("/")
def list_products():
    result = get_products()
    return result.data

@router.post("/upload-image")
def upload_product_image(file: UploadFile = File(...)):
    filename = f"products/{uuid.uuid4()}-{file.filename}"
    url = upload_image(file, filename)
    return {"image_url": url}

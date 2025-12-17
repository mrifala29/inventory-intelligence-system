import uuid
from app.core.supabase import supabase
from app.core.s3 import s3_client
from app.core.config import AWS_S3_BUCKET

IMAGE_TABLE = "product_images"
ITEM_TABLE = "product_items"


def product_exists(product_id: str) -> bool:
    res = (
        supabase
        .table(ITEM_TABLE)
        .select("product_id")
        .eq("product_id", product_id)
        .execute()
    )
    return len(res.data) > 0


def upload_to_s3(file, product_id: str) -> str:
    file_ext = file.filename.split(".")[-1]
    object_name = f"products/{product_id}/{uuid.uuid4()}.{file_ext}"

    s3_client.upload_fileobj(
        file.file,
        AWS_S3_BUCKET,
        object_name,
        ExtraArgs={"ContentType": file.content_type}
    )

    return f"https://{AWS_S3_BUCKET}.s3.amazonaws.com/{object_name}"


def save_image(data: dict):
    return supabase.table(IMAGE_TABLE).insert(data).execute()

import boto3
from app.config import (
    AWS_ACCESS_KEY_ID,
    AWS_SECRET_ACCESS_KEY,
    AWS_REGION,
    AWS_S3_BUCKET
)

s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)

def upload_image(file, filename):
    s3.upload_fileobj(
        file,
        AWS_S3_BUCKET,
        filename,
        ExtraArgs={"ContentType": file.content_type}
    )
    return f"https://{AWS_S3_BUCKET}.s3.{AWS_REGION}.amazonaws.com/{filename}"

def test_s3_connection():
    s3.list_objects_v2(
        Bucket=AWS_S3_BUCKET,
        MaxKeys=1
    )

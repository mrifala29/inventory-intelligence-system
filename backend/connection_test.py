from app.services.supabase_service import supabase
from app.services.s3_service import test_s3_connection

def test_supabase():
    print("Testing Supabase connection...")
    try:
        result = supabase.table("product_items").select("*").limit(1).execute()
        print("✅ Supabase CONNECTED")
        print(f"Rows fetched: {len(result.data)}")
    except Exception as e:
        print("❌ Supabase FAILED")
        print(str(e))

def test_s3():
    print("\nTesting AWS S3 connection...")
    try:
        test_s3_connection()
        print("✅ S3 CONNECTED")
    except Exception as e:
        print("❌ S3 FAILED")
        print(str(e))

if __name__ == "__main__":
    test_supabase()
    test_s3()

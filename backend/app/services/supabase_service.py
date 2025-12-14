from supabase import create_client
from app.config import SUPABASE_URL, SUPABASE_KEY

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def create_product(data: dict):
    return supabase.table("products").insert(data).execute()

def get_products():
    return supabase.table("products").select("*").execute()

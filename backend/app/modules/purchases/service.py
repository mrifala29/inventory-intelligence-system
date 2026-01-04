from app.core.supabase import supabase

PURCHASE_TABLE = "purchases"
PURCHASE_ITEM_TABLE = "purchases_items"
CUSTOMER_TABLE = "customers"
PRODUCT_TABLE = "product_items"


def customer_exists(customer_id: str) -> bool:
    res = (
        supabase.table(CUSTOMER_TABLE)
        .select("customer_id")
        .eq("customer_id", customer_id)
        .execute()
    )
    return len(res.data) > 0

def product_exists(product_id: str) -> bool:
    res = (
        supabase.table(PRODUCT_TABLE)
        .select("product_id")
        .eq("product_id", product_id)
        .execute()
    )
    return len(res.data) > 0

def create_purchase(data: dict):
    return supabase.table(PURCHASE_TABLE).insert(data).execute()

def create_purchase_item(data: dict):
    return supabase.table(PURCHASE_ITEM_TABLE).insert(data).execute()

def get_all_purchases():
    return(
        supabase
        .table(PURCHASE_TABLE)
        .select("*")
        .order("date", desc=True)
        .execute()
    )
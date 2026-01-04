from app.core.supabase import supabase

SALES_TABLE = "sales"
SALES_ITEM_TABLE = "sales_items"
CUSTOMER_TABLE = "customers"
PRODUCT_TABLE = "product_items"


def customer_exists(customer_id: str) -> bool:
    res = (
        supabase
        .table(CUSTOMER_TABLE)
        .select("customer_id")
        .eq("customer_id", customer_id)
        .execute()
    )
    return len(res.data) > 0


def product_exists(product_id: str) -> bool:
    res = (
        supabase
        .table(PRODUCT_TABLE)
        .select("product_id")
        .eq("product_id", product_id)
        .execute()
    )
    return len(res.data) > 0


def create_sales(data: dict):
    return supabase.table(SALES_TABLE).insert(data).execute()


def create_sales_item(data: dict):
    return supabase.table(SALES_ITEM_TABLE).insert(data).execute()


def get_all_sales():
    return (
        supabase
        .table(SALES_TABLE)
        .select("*")
        .order("date", desc=True)
        .execute()
    )

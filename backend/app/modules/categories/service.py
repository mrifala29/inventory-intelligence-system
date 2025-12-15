from app.core.supabase import supabase

TABLE = "product_categories"

def create_category(data: dict):
    return supabase.table(TABLE).insert(data).execute()

def get_all_categories():
    return supabase.table(TABLE).select("*").order("created_at").execute()

def update_category(category_id: str, data: dict):
    return (
        supabase
        .table(TABLE)
        .update(data)
        .eq("category_id", category_id)
        .execute()
    )

def delete_category(category_id: str):
    return (
        supabase
        .table(TABLE)
        .delete()
        .eq("category_id", category_id)
        .execute()
    )

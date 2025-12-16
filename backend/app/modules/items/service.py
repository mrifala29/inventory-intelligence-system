from app.core.supabase import supabase

ITEM_TABLE = "product_items"
MODEL_TABLE = "product_models"

def model_exists(model_id: str) -> bool:
    res = (
        supabase
        .table(MODEL_TABLE)
        .select("product_model_id")
        .eq("product_model_id", model_id)
        .execute()
    )
    return len(res.data) > 0


def create_item(data: dict):
    return supabase.table(ITEM_TABLE).insert(data).execute()


def get_all_items():
    return (
        supabase
        .table(ITEM_TABLE)
        .select("*")
        .order("created_at", desc=True)
        .execute()
    )


def update_item(product_id: str, data: dict):
    return (
        supabase
        .table(ITEM_TABLE)
        .update(data)
        .eq("product_id", product_id)
        .execute()
    )


def delete_item(product_id: str):
    return (
        supabase
        .table(ITEM_TABLE)
        .delete()
        .eq("product_id", product_id)
        .execute()
    )

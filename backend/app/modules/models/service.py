from app.core.supabase import supabase

MODEL_TABLE = "product_models"
CATEGORY_TABLE = "product_categories"

def category_exists(category_id: str) -> bool:
    res = (
        supabase
        .table(CATEGORY_TABLE)
        .select("category_id")
        .eq("category_id", category_id)
        .execute()
    )
    return len(res.data) > 0


def create_model(data: dict):
    return supabase.table(MODEL_TABLE).insert(data).execute()


def get_all_models():
    return (
        supabase
        .table(MODEL_TABLE)
        .select(
            "product_model_id, category_id, brand, model_name, production_year, created_at, updated_at"
        )
        .order("created_at")
        .execute()
    )


def update_model(model_id: str, data: dict):
    return (
        supabase
        .table(MODEL_TABLE)
        .update(data)
        .eq("product_model_id", model_id)
        .execute()
    )


def delete_model(model_id: str):
    return (
        supabase
        .table(MODEL_TABLE)
        .delete()
        .eq("product_model_id", model_id)
        .execute()
    )

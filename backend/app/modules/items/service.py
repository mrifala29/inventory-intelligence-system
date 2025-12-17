from app.core.supabase import supabase

ITEM_TABLE = "product_items"
MODEL_TABLE = "product_models"


def generate_sku(model_id: str) -> str:
    # Ambil category_id dari model
    model = (
        supabase
        .table("product_models")
        .select("category_id")
        .eq("product_model_id", model_id)
        .single()
        .execute()
    )

    category_id = model.data["category_id"].upper()

    # Ambil SKU terakhir
    last_item = (
        supabase
        .table("product_items")
        .select("sku")
        .ilike("sku", f"{category_id}-%")
        .order("created_at", desc=True)
        .limit(1)
        .execute()
    )

    if last_item.data:
        last_sku = last_item.data[0]["sku"]
        last_number = int(last_sku.split("-")[1])
        next_number = last_number + 1
    else:
        next_number = 1

    return f"{category_id}-{next_number:04d}"


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

from app.core.supabase import supabase

TABLE = "customers"

def create_customer(data: dict):
    return supabase.table(TABLE).insert(data).execute()


def get_all_customers():
    return (
        supabase
        .table(TABLE)
        .select("*")
        .order("created_at", desc=True)
        .execute()
    )


def get_customer_by_id(customer_id: str):
    return (
        supabase
        .table(TABLE)
        .select("*")
        .eq("customer_id", customer_id)
        .execute()
    )


def update_customer(customer_id: str, data: dict):
    return (
        supabase
        .table(TABLE)
        .update(data)
        .eq("customer_id", customer_id)
        .execute()
    )


def delete_customer(customer_id: str):
    return (
        supabase
        .table(TABLE)
        .delete()
        .eq("customer_id", customer_id)
        .execute()
    )

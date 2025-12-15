from supabase import create_client, Client
from app.core.config import SUPABASE_URL, SUPABASE_KEY

if not SUPABASE_URL or not SUPABASE_KEY:
    raise RuntimeError("Supabase environment variables not set")

supabase: Client = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)
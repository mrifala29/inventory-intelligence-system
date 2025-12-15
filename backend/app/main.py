from fastapi import FastAPI
from app.modules.categories.router import router as category_router

app = FastAPI(title="Inventory Intelligence API")

app.include_router(category_router)

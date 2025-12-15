from fastapi import FastAPI
from app.modules.categories.router import router as category_router
from app.modules.models.router import router as model_router

app = FastAPI(title="Inventory Intelligence API")

app.include_router(category_router)
app.include_router(model_router)
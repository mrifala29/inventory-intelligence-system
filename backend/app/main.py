from fastapi import FastAPI
from app.modules.categories.router import router as category_router
from app.modules.models.router import router as model_router
from app.modules.items.router import router as item_router
from app.modules.images.router import router as image_router
from app.modules.customers.router import router as customer_router
from app.modules.purchases.router import router as purchase_router

app = FastAPI(title="Inventory Intelligence API")

app.include_router(category_router)
app.include_router(model_router)
app.include_router(item_router)
app.include_router(image_router)
app.include_router(customer_router)
app.include_router(purchase_router)

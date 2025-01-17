from fastapi import FastAPI
from app.database import engine, Base
from app.routes import routes

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include the item routes
app.include_router(routes.router)

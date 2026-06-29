from fastapi import FastAPI

from app.routes.shorten import router as shorten_router
from app.routes.redirect import router as redirect_router
from app.database.connection import test_connection

# app = FastAPI(
#     title="Short.ly API",
#     version="1.0.0"
# )
#
#
# app.include_router(shorten_router)
# app.include_router(shorten_router)
# app.include_router(redirect_router)
#
#
# @app.get("/")
# def home():
#     return {
#         "message": "Welcome to Short.ly 🚀"
#     }

from contextlib import asynccontextmanager
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting Short.ly...")
    test_connection()
    yield
    print("Shutting down Short.ly...")


app = FastAPI(
    title="Short.ly API",
    version="1.0.0",
    lifespan=lifespan
)
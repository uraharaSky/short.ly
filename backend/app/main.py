from fastapi import FastAPI

from app.routes.shorten import router as shorten_router
from app.routes.redirect import router as redirect_router

app = FastAPI(
    title="Short.ly API",
    version="1.0.0"
)


app.include_router(shorten_router)
app.include_router(shorten_router)
app.include_router(redirect_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to Short.ly 🚀"
    }
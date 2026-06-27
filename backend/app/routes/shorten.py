from fastapi import APIRouter
from pydantic import BaseModel

from app.services.shortener import create_short_url


router = APIRouter()


class URLRequest(BaseModel):
    url: str


@router.post("/shorten")
def shorten_url(request: URLRequest):

    short_code = create_short_url(request.url)

    return {
        "original_url": request.url,
        "short_url": f"http://127.0.0.1:8000/{short_code}"
    }
from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse

from app.services.shortener import get_original_url

router = APIRouter()


@router.get("/{short_code}")
def redirect(short_code: str):

    original_url = get_original_url(short_code)

    if original_url is None:
        raise HTTPException(
            status_code=404,
            detail="Short URL not found."
        )

    return RedirectResponse(url=original_url)
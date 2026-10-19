import os

from fastapi import Depends, HTTPException
from fastapi.security import APIKeyHeader


API_KEY = os.getenv("GAUNTLET_API_KEY", "gauntlet-local-key")

api_key_header = APIKeyHeader(
    name="X-API-Key",
    auto_error=False
)


def verify_api_key(
    x_api_key: str | None = Depends(api_key_header)
):
    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Invalid or missing API key."
        )

    return True
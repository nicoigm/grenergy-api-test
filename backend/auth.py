from fastapi import HTTPException, Security
from fastapi.security.api_key import APIKeyHeader
from config import MY_API_KEY

api_key_header = APIKeyHeader(name="X-API-Key")


def verify_api_key(key: str = Security(api_key_header)):
    if key != MY_API_KEY:
        raise HTTPException(status_code=403, detail="API Key inválida")
    return key
import jwt
from datetime import datetime, timedelta
from typing import Dict, Any, Optional
from shared.configs.settings import BaseAppSettings

settings = BaseAppSettings()

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.jwt_secret, algorithm=settings.jwt_algorithm)
    return encoded_jwt

def verify_token(token: str) -> Dict[str, Any]:
    try:
        payload = jwt.decode(token, settings.jwt_secret, algorithms=[settings.jwt_algorithm])
        return payload
    except jwt.ExpiredSignatureError:
        from shared.exceptions import UnauthorizedError
        raise UnauthorizedError("Token has expired")
    except jwt.PyJWTError:
        from shared.exceptions import UnauthorizedError
        raise UnauthorizedError("Could not validate credentials")

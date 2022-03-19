from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from typing import Dict
from passlib.context import CryptContext
import jwt
from time import time

JWT_SECRET = "secret"
JWT_ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def token_response(token: str):
    return {
        "access_token": token
    }


# function used for signing the JWT string
def sign_jwt(user_id: str) -> Dict[str, str]:
    payload = {
        "user_id": user_id,
        "expires": time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token_response(token)


def decode_jwt(token: str) -> dict:

    decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    return decoded_token if decoded_token["expires"] >= time() else None


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
            if not self.verify_jwt(credentials.credentials):
                # TODO make expired and invalid token errors separated
                raise HTTPException(status_code=403, detail="Invalid token or expired token.")
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

    def verify_jwt(self, jwtoken: str) -> bool:
        is_token_valid: bool = False

        try:
            payload = decode_jwt(jwtoken)
        except jwt.ExpiredSignatureError:
            raise HTTPException(401, 'Signature has expired')
        except jwt.InvalidTokenError as e:
            raise HTTPException(401, 'Invalid token')

        if payload:
            is_token_valid = True
        return is_token_valid


class Hasher:
    @staticmethod
    def verify_password(plain_password, hashed_password): return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def get_password_hash(password): return pwd_context.hash(password)

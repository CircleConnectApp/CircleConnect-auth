from jose import jwt
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone
import os
load_dotenv()

def JWTCreation(data: dict):
    expirationTime = datetime.now(timezone.utc) + timedelta(minutes=60)
    payload = { **data, "expiration": expirationTime }
    encoded_jwt = jwt.encode(payload, os.getenv("JWT_SECRET_KEY"), algorithm=os.getenv("JWT_Algorithm"))    
    return encoded_jwt

def token_Verification(token: str):
    try:
        decoded_jwt = jwt.decode(token, os.getenv("JWT_SECRET_KEY"), algorithms=[os.getenv("JWT_Algorithm")])
        return decoded_jwt
    except jwt.JWTError:
        return None
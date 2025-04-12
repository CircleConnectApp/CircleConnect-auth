from .security import JWTCreation
from fastapi import APIRouter, HTTPException, requests
from fastapi.security import OAuth2AuthorizationCodeBearer
import httpx
from .models import Token
import os 

router = APIRouter(prefix="/auth")
OAuthInstance = OAuth2AuthorizationCodeBearer(
    authorizationUrl= "https://accounts.google.com/o/oauth2/auth", tokenUrl= "https://oauth2.googleapis.com/token"
)

@router.get("/login")
async def login_redirect():
    ClientID = os.getenv('GOOGLE_CLIENT_ID')     
    redirecturl = os.getenv('REDIRECT_URI') 
    googleLoginurl = (
        "https://accounts.google.com/o/oauth2/auth?"
        f"response_type=code&"
        f"client_id={ClientID}&"
        f"redirect_uri={redirecturl}&"
        "scope=openid%20profile%20email" 
    )

    return {
        "login_url": googleLoginurl
        }

@router.get("/callback", response_model=Token)
async def callback(code: str):
    async with httpx.AsyncClient() as client:
        tokenResponse= await client.post(
            "https://oauth2.googleapis.com/token",
            data = {
                "code": code,
                "client_id": os.getenv("GOOGLE_CLIENT_ID"),
                "client_secret": os.getenv("GOOGLE_CLIENT_SECRET"),
                "redirect_uri": os.getenv("REDIRECT_URI"),
                "grant_type": "authorization_code"
            }
        )
        userResponse = await client.get(
            "https://www.googleapis.com/oauth2/v3/userinfo",
            headers={"Authorization": f"Bearer {tokenResponse.json()['access_token']}"}

        )

        DataOfUser = userResponse.json()
        JWTToken = JWTCreation({
            "sub": DataOfUser["sub"],
            "email": DataOfUser["email"],
            "name": DataOfUser.get("name", "")
        })

        return {"access_token": JWTToken, "token_type": "bearer"}

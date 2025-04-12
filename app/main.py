from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .auth import router as auth_router
import uvicorn
import os

app = FastAPI(title="CircleConnect Auth Service")



app.include_router(auth_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
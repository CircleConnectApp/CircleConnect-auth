from pydantic import BaseModel

class User(BaseModel):
    id: int
    email: str
    google_id: str
    role: str

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str
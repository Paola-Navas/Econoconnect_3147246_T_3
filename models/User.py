from pydantic import BaseModel, Field

class user(BaseModel):
    username : str
    password : str = Field(..., min_length=8, max_length=12)

class RegisterUser(BaseModel):
    id: int
    username : str
    password : str = Field(..., min_length=8, max_length=12)
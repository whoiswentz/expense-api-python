from pydantic import BaseModel, Field, EmailStr


class UserCreation(BaseModel):
    email: EmailStr = Field(..., description="User's email address")
    username: str = Field(..., description="User's username")
    password: str = Field(..., description="Password for the user account")

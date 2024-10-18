from pydantic import BaseModel, Field, EmailStr


class UserCreation(BaseModel):
    email: EmailStr = Field(..., description="User's email address")
    username: str = Field(..., description="User's username")
    password: str = Field(..., description="Password for the user account")


class UserCreationResponse(BaseModel):
    id: int = Field(..., description="Unique identifier for the user")
    email: EmailStr = Field(..., description="User's email address")
    username: str = Field(..., description="User's username")

    class Config:
        populate_by_name = True
        from_attributes = True

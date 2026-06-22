
from typing import Literal
from pydantic import BaseModel, Field, ConfigDict 
from uuid import UUID

class TokenResponse(BaseModel): 
    model_config = ConfigDict(extra="forbid")
    access_token: str = Field(min_length=1)
    refresh_token: str = Field(description="Токен для обновления access_token")
    token_type: Literal["bearer", "Bearer"] = "bearer" 
    




class UserResponsepart2(BaseModel):
    id: str
    username: str
    display_name: str | None = None
    avatar_url: str | None = None
    is_verified: bool


class UserPaginatedResponse(BaseModel):
    items: list[UserResponsepart2]
    total: int
    page: int
    per_page: int
    pages: int
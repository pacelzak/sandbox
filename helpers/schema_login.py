
from typing import Literal
from pydantic import BaseModel, Field, ConfigDict 
from uuid import UUID
from datetime import datetime 

class SchemaAuth(BaseModel): 
    model_config = ConfigDict(extra="forbid")
    access_token: str = Field(min_length=1)
    refresh_token: str = Field(description="Токен для обновления access_token")
    token_type: Literal["bearer", "Bearer"] = "bearer" 

class SchemaReg(BaseModel): 
    model_config = ConfigDict(extra="forbid")
    
    id: str
    email: str
    username: str
    display_name: str
    bio: str|None
    avatar_url: str|None
    cover_url: str|None
    role: str
    is_active: bool
    is_verified: bool
    is_private: bool
    created_at: datetime
    updated_at: datetime
    followers_count: int
    following_count: int
    posts_count: int
    is_following: bool
    is_followed_by: bool



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
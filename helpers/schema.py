
from typing import Literal
from pydantic import BaseModel, Field, ConfigDict

class TokenResponse(BaseModel): 
    model_config = ConfigDict(extra="forbid")
    access_token: str = Field(min_length=1)
    refresh_token: str = Field(description="Токен для обновления access_token")
    # Используем Literal, чтобы жестко зафиксировать допустимое значение
    token_type: Literal["bearer", "Bearer"] = "bearer" 
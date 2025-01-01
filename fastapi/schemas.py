from typing import Any, Optional
from pydantic import BaseModel


class ResponseModel(BaseModel):
    code: int = 200
    msg: str = "成功"
    data: Optional[Any] = None

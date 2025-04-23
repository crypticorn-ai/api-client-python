from typing import Optional, Dict
from pydantic import BaseModel
from fastapi import HTTPException as FastAPIHTTPException
from crypticorn.common import ApiError

class ExceptionDetail(BaseModel):
    message: str
    error: ApiError

class HTTPException(FastAPIHTTPException):
    def __init__(
        self,
        status_code: int,
        detail: ExceptionDetail,
        headers: Optional[Dict[str, str]] = None,
    ):
        exc = ExceptionDetail(**detail) if not isinstance(detail, ExceptionDetail) else detail
        super().__init__(status_code=status_code, detail=exc.model_dump(), headers=headers)
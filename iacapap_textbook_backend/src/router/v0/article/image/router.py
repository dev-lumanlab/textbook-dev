from typing import Annotated

from fastapi import APIRouter, status, HTTPException, Depends, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from sqlalchemy.orm import Session

from src.database import get_db
from src.router.v0.user.crud import get_auth

from .crud import *
from .response import *

from src.model import User

router = APIRouter()


@router.post(
    "/image",
    response_model=ImageUploadResponse,
    status_code=status.HTTP_201_CREATED,
)
async def UploadImage(
    request: Request,
    upload: UploadFile = File(...),
    db: Session = Depends(get_db),
    cur_user: User = Depends(get_auth),
):
    """
    Upload image
    """
    try:
        # 관리자만 이미지 업로드 가능
        if cur_user.level not in [1, 2]:
            raise HTTPException(
                status_code=403,
                detail={"msg": "권한이 없습니다."},
            )

        url = await upload_image(upload)
        response = ImageUploadResponse.create(request, url)
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content=response.model_dump(),
        )
    except Exception as e:
        if isinstance(e, HTTPException):
            raise e
        raise HTTPException(
            status_code=500,
            detail={"msg": "이미지 업로드 실패"},
        )

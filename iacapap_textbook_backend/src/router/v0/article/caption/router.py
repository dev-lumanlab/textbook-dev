from typing import Annotated

from fastapi import APIRouter, status, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from sqlalchemy.orm import Session

from src.database import get_db
from src.router.v0.user.crud import get_auth

from .schema import *
from .crud import *
from .response import *

from src.model import User

router = APIRouter()


@router.post(
    "",
    response_model=CreateCaptionResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_caption(
    request: Request,
    article_id: int,
    caption: CreateCaptionSchema,
    cur_user: User = Depends(get_auth),
    db: Session = Depends(get_db),
):
    """
    캡션 생성
    """
    try:
        # 캡션 생성
        caption_id = db_create_caption(
            db=db,
            article_id=article_id,
            user_id=cur_user.id,
            content=caption.content,
        )

        # 응답 생성
        response = CreateCaptionResponse.create(request=request, caption_id=caption_id)
        db.commit()
        return JSONResponse(
            status_code=response.meta.status,
            content=response.model_dump(),
        )
    except Exception as e:
        db.rollback()
        if isinstance(e, HTTPException):
            raise e
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e),
        )


@router.get(
    "",
    response_model=GetCaptionResponse,
    status_code=status.HTTP_200_OK,
)
def get_caption(
    request: Request,
    article_id: int,
    cur_user: User = Depends(get_auth),
    db: Session = Depends(get_db),
):
    """
    캡션 조회
    """
    try:
        # 캡션 가져오기
        db_captions = db_get_captions(db=db, user_id=cur_user.id, article_id=article_id)

        # 캡션 모델 생성
        captions = []
        for db_caption in db_captions:
            caption = CaptionResponseModel(
                id=db_caption.id,
                article_id=db_caption.article_id,
                content=db_caption.content,
            )
            captions.append(caption)

        # 응답 생성
        response = GetCaptionResponse.create(request=request, captions=captions)
        return JSONResponse(
            status_code=response.meta.status,
            content=response.model_dump(),
        )
    except Exception as e:
        if isinstance(e, HTTPException):
            raise e
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e),
        )


@router.delete(
    "",
    response_model=DeleteCaptionResponse,
    status_code=status.HTTP_200_OK,
)
def delete_caption(
    request: Request,
    caption_id: int,
    cur_user: User = Depends(get_auth),
    db: Session = Depends(get_db),
):
    """
    캡션 삭제
    """
    try:
        # 캡션 삭제
        db_delete_caption(db=db, caption_id=caption_id)

        # 응답 생성
        response = DeleteCaptionResponse.create(request=request)
        db.commit()
        return JSONResponse(
            status_code=response.meta.status,
            content=response.model_dump(),
        )
    except Exception as e:
        db.rollback()
        if isinstance(e, HTTPException):
            raise e
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e),
        )

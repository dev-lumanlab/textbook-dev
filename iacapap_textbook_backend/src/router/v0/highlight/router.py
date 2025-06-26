from typing import Annotated

from fastapi import APIRouter, status, HTTPException, Depends, Query
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from sqlalchemy.orm import Session

from src.database import get_db
from src.router.v0.user.crud import get_auth

from .schema import *
from .crud import *
from .response import *

from ..article.crud import db_get_article

from src.model import User

router = APIRouter()


@router.post(
    "",
    response_model=CreateHighlightResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_highlight(
    request: Request,
    article_id: int,
    create_highlight_schema: CreateHighlightSchema,
    cur_user: User = Depends(get_auth),
    db: Session = Depends(get_db),
):
    """
    하이라이트 생성
    """
    try:
        # article_id로 article을 가져오기
        db_article = db_get_article(db=db, article_id=article_id)

        # 하이라이트 생성
        highlight_id = db_create_highlight(
            db=db,
            article_id=article_id,
            user_id=cur_user.id,
            block=create_highlight_schema.block,
            start=create_highlight_schema.start,
            end=create_highlight_schema.end,
            text=create_highlight_schema.text,
        )

        # 응답 모델 생성
        response = CreateHighlightResponse.create(
            request=request,
            highlight_id=highlight_id,
        )
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
    response_model=GetHighlightsResponse,
    status_code=status.HTTP_200_OK,
)
def get_highlights_from_article(
    request: Request,
    article_id: Optional[int] = Query(None),
    page: Optional[int] = Query(1),
    limit: Optional[int] = Query(10),
    cur_user: User = Depends(get_auth),
    db: Session = Depends(get_db),
):
    """
    하이라이트 목록 조회
    """

    try:
        # 아티클 내 검색의 경우
        if article_id:
            # user_id, article_id로 하이라이트 목록 가져오기
            db_highlights = db_get_highlights_from_article(
                db=db, user_id=cur_user.id, article_id=article_id
            )

            # 하이라이트 목록 생성
            highlights = []
            for db_highlight in db_highlights:
                highlight = HighlightResponseModel(
                    id=db_highlight.id,
                    article_id=db_highlight.article_id,
                    book=db_highlight.article.book,
                    chapter=db_highlight.article.chapter,
                    user_id=db_highlight.user_id,
                    block=db_highlight.block,
                    start=db_highlight.start,
                    end=db_highlight.end,
                    text=db_highlight.text,
                    created_at=db_highlight.created_at.isoformat(),
                )
                highlights.append(highlight)

            total = len(highlights)

            # 응답 모델 생성
            response = GetHighlightsResponse.create(
                request=request,
                highlights=highlights,
                total=total,
            )
            return JSONResponse(
                status_code=response.meta.status,
                content=response.model_dump(),
            )

        # 하이라이트 검색의 경우 (페이지네이션)
        else:
            db_highlights = db_get_highlights_from_user(
                db=db, user_id=cur_user.id, skip=(page - 1) * limit, limit=limit
            )
            highlights = []
            for db_highlight in db_highlights:
                highlight = HighlightResponseModel(
                    id=db_highlight.id,
                    article_id=db_highlight.article_id,
                    book=db_highlight.article.book,
                    chapter=db_highlight.article.chapter,
                    user_id=db_highlight.user_id,
                    block=db_highlight.block,
                    start=db_highlight.start,
                    end=db_highlight.end,
                    text=db_highlight.text,
                    created_at=db_highlight.created_at.isoformat(),
                )
                highlights.append(highlight)

            total = db_count_highlights_from_user(db=db, user_id=cur_user.id)
            response = GetHighlightsResponse.create(
                request=request,
                highlights=highlights,
                total=total,
            )
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
    response_model=DeleteHighlightResponse,
    status_code=status.HTTP_200_OK,
)
def delete_highlight(
    request: Request,
    highlight_id: int,
    cur_user: User = Depends(get_auth),
    db: Session = Depends(get_db),
):
    try:
        # 하이라이트 가져오기
        db_highlight = db_get_highlight(db=db, highlight_id=highlight_id)

        # 권한 확인
        if db_highlight.user_id != cur_user.id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="권한이 없습니다.",
            )

        # 하이라이트 삭제
        highlight_id = db_delete_highlight(db=db, highlight_id=highlight_id)

        # 응답 모델 생성
        response = DeleteHighlightResponse.create(
            request=request,
        )
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

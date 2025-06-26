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
from .image.crud import parse_html, get_thumbnail, get_text

from src.model import User

router = APIRouter()


@router.post(
    "",
    response_model=CreateArticleResponse,
    status_code=status.HTTP_201_CREATED,
)
def CreateArticle(
    request: Request,
    create_article_schema: CreateArticleSchema,
    cur_user: User = Depends(get_auth),
    db: Session = Depends(get_db),
):
    try:
        # 관리자만 아티클 등록 가능
        if cur_user.level == 0:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="No permission. Call the administrator.",
            )

        # 아티클 파싱, 바이너리 이미지를 저장 후 url로 변환
        parsed_content = parse_html(create_article_schema.content)

        # 파싱된 아티클에서 썸네일 추출
        thumbnail = get_thumbnail(parsed_content)

        # 검색을 위한 텍스트만 추출
        content_textonly = get_text(parsed_content)

        # 아티클 등록
        article_id = db_create_article(
            db,
            book=create_article_schema.book,
            title=create_article_schema.title,
            content=parsed_content,
            content_textonly=content_textonly,
            chapter=create_article_schema.chapter,
            user_id=cur_user.id,
            thumbnail=thumbnail,
        )

        # 응답 생성
        response = CreateArticleResponse.create(
            request=request,
            article_id=article_id,
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
    response_model=GetArticlesResponse,
    status_code=status.HTTP_200_OK,
)
def GetArticles(
    request: Request,
    page: int = 1,
    limit: int = 10,
    published: bool = True,
    cur_user: User = Depends(get_auth),
    db: Session = Depends(get_db),
):
    try:
        # 관리자가 아닌 경우, published가 False인 아티클은 가져올 수 없음
        if cur_user.level == 0 and published is False:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="No permission. Call the administrator.",
            )

        # 페이지네이션으로 아티클 리스트 가져오기, published 여부에 따라 가져오기
        db_articles = db_get_articles(
            db, skip=(page - 1) * limit, limit=limit, published=published
        )
        articles = []

        # 아티클 리스트를 응답 모델로 변환
        for db_article in db_articles:
            article = ArticlesResponseModel(
                id=db_article.id,
                published=db_article.published,
                book=db_article.book,
                chapter=db_article.chapter,
                title=db_article.title,
                creator_id=db_article.creator_id,
                last_update=(
                    db_article.last_update.isoformat()
                    if db_article.last_update
                    else None
                ),
                last_publish=(
                    db_article.last_publish.isoformat()
                    if db_article.last_publish
                    else None
                ),
                thumbnail=db_article.thumbnail,
            )
            articles.append(article)

        # 전체 아티클 개수 가져오기
        total = db_count_articles(db, published=published)

        # 응답 생성
        response = GetArticlesResponse.create(
            request=request,
            articles=articles,
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


@router.get(
    "/search",
    response_model=SearchArticleResponse,
    status_code=status.HTTP_200_OK,
)
def SearchArticle(
    request: Request,
    keyword: str,
    page: int = 1,
    limit: int = 10,
    published: bool = True,
    cur_user: User = Depends(get_auth),
    db: Session = Depends(get_db),
):
    # 관리자가 아닌 경우, published가 False인 아티클은 검색할 수 없음
    if cur_user.level == 0 and published is False:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No permission. Call the administrator.",
        )

    try:
        db_articles = db_search_articles(
            db,
            keyword=keyword,
            skip=(page - 1) * limit,
            limit=limit,
            published=published,
        )
        articles = []
        for db_article in db_articles:
            keyword_idx = db_article.content_textonly.find(keyword)
            searched_content = db_article.content_textonly[
                keyword_idx : min(keyword_idx + 450, len(db_article.content_textonly))
            ]
            article = SearchedArticlesResponseModel(
                id=db_article.id,
                published=db_article.published,
                book=db_article.book,
                chapter=db_article.chapter,
                title=db_article.title,
                searched_content=searched_content,
            )
            articles.append(article)

        total = db_count_search_articles(db, published=published, keyword=keyword)

        response = SearchArticleResponse.create(
            request=request,
            articles=articles,
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


@router.get(
    "/{article_id}",
    response_model=GetArticleResponse,
    status_code=status.HTTP_200_OK,
)
def GetArticle(
    request: Request,
    article_id: int,
    cur_user: User = Depends(get_auth),
    db: Session = Depends(get_db),
):
    try:
        # 아티클 한개 가져오기
        db_article = db_get_article(db, article_id)

        # 관리자가 아닌 경우, unpublished 아티클은 가져올 수 없음
        if cur_user.level == 0 and db_article.published is False:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="No permission. Call the administrator.",
            )

        # 아티클을 응답 모델로 변환
        article = ArticleResponseModel(
            id=db_article.id,
            published=db_article.published,
            book=db_article.book,
            chapter=db_article.chapter,
            title=db_article.title,
            content=db_article.content,
            creator_id=db_article.creator_id,
            last_update=(
                db_article.last_update.isoformat() if db_article.last_update else None
            ),
            last_publish=(
                db_article.last_publish.isoformat() if db_article.last_publish else None
            ),
            thumbnail=db_article.thumbnail,
        )

        # 응답 생성
        response = GetArticleResponse.create(
            request=request,
            article=article,
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


@router.patch(
    "/{article_id}",
    response_model=PatchArticleResponse,
    status_code=status.HTTP_200_OK,
)
def PatchArticle(
    request: Request,
    article_id: int,
    patch_article_schema: CreateArticleSchema,
    cur_user: User = Depends(get_auth),
    db: Session = Depends(get_db),
):
    try:
        # 관리자만 아티클 수정 가능
        if cur_user.level == 0:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="No permission. Call the administrator.",
            )
        
        db_article = db_get_article(db, article_id)
        if db_article.published == True:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Published article cannot be modified.",
            )

        # 아티클 파싱, 바이너리 이미지를 저장 후 url로 변환
        parsed_content = parse_html(patch_article_schema.content)

        # 파싱된 아티클에서 썸네일 추출
        thumbnail = get_thumbnail(parsed_content)

        # 검색을 위한 텍스트만 추출
        content_textonly = get_text(parsed_content)

        # 아티클 수정
        article_id = db_update_article(
            db,
            article_id=article_id,
            book=patch_article_schema.book,
            title=patch_article_schema.title,
            content=parsed_content,
            content_textonly=content_textonly,
            chapter=patch_article_schema.chapter,
            thumbnail=thumbnail,
        )

        # 응답 생성
        response = PatchArticleResponse.create(
            request=request,
            article_id=article_id,
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


@router.delete(
    "/{article_id}",
    response_model=DeleteArticleResponse,
    status_code=status.HTTP_200_OK,
)
def DeleteArticle(
    request: Request,
    article_id: int,
    cur_user: User = Depends(get_auth),
    db: Session = Depends(get_db),
):
    try:
        # 관리자만 아티클 삭제 가능
        if cur_user.level == 0:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="No permission. Call the administrator.",
            )

        # 아티클 삭제
        article_id = db_delete_article(db, article_id)

        # 응답 생성
        response = DeleteArticleResponse.create(
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
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(e),
            )


@router.patch(
    "/{article_id}/publish",
    response_model=PublishArticleResponse,
    status_code=status.HTTP_200_OK,
)
def PublishArticle(
    request: Request,
    article_id: int,
    query: bool,
    cur_user: User = Depends(get_auth),
    db: Session = Depends(get_db),
):
    try:
        # 관리자만 아티클 퍼블리시 가능
        if cur_user.level == 0:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="No permission. Call the administrator.",
            )

        # 아티클 퍼블리시하기 / 해제하기
        article_id = db_publish_article(db, article_id, query=query)

        # 응답 생성
        response = PublishArticleResponse.create(
            request=request,
            article_id=article_id,
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
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(e),
            )


@router.get(
    "/{article_id}/duplicate",
    response_model=DuplicateArticleResponse,
    status_code=status.HTTP_200_OK,
)
def DuplicateArticle(
    request: Request,
    article_id: int,
    cur_user: User = Depends(get_auth),
    db: Session = Depends(get_db),
):
    try:
        # 관리자만 아티클 복사 가능
        if cur_user.level == 0:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="No permission. Call the administrator.",
            )

        # 아티클 복사하기
        article_id = db_duplicate_article(db, article_id, cur_user.id)

        # 응답 생성
        response = DuplicateArticleResponse.create(
            request=request,
            article_id=article_id,
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
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(e),
            )

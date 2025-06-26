from fastapi import Request
from time import time
from urllib.parse import urlparse
from typing import List
import os
from pydantic import BaseModel
from typing import Optional

from src.schema.response.common import Meta, Content, Links, CommonResponseModel

URL = os.getenv("DOMAIN_URL", "http://localhost:8000")


class CreateArticleResponse(CommonResponseModel):
    @classmethod
    def create(
        cls,
        request: Request,
        article_id: int,
    ):
        meta = Meta(
            status=201,
            message=f"Article created successfully.",
            location=["Article", "create"],
            processing_time=time() - request.scope.get("start_time"),
        )

        content = Content(article_id=article_id)

        path = urlparse(str(request.url.path)).path
        links = Links(
            self=f"{URL}{path}",
            docs=f"{URL}/docs",
            article=f"{URL}/v0/article/{article_id}",
        )

        return cls(
            meta=meta,
            content=content,
            links=links,
        )


class ArticleResponseModel(BaseModel):
    id: int
    published: bool
    book: str
    chapter: str
    title: str
    content: str
    creator_id: int
    last_update: Optional[str] = None
    last_publish: Optional[str] = None
    thumbnail: Optional[str] = None


class ArticlesResponseModel(BaseModel):
    id: int
    published: bool
    book: str
    chapter: str
    title: str
    creator_id: int
    last_update: Optional[str] = None
    last_publish: Optional[str] = None
    thumbnail: Optional[str] = None


class SearchedArticlesResponseModel(BaseModel):
    id: int
    published: bool
    book: str
    chapter: str
    title: str
    searched_content: str


class GetArticleResponse(CommonResponseModel):
    @classmethod
    def create(
        cls,
        request: Request,
        article: ArticleResponseModel,
    ):
        meta = Meta(
            status=200,
            message=f"Article retrieved successfully.",
            location=["Article", "retrieve"],
            processing_time=time() - request.scope.get("start_time"),
        )

        content = Content(article=article)

        path = urlparse(str(request.url.path)).path
        links = Links(
            self=f"{URL}{path}",
            docs=f"{URL}/docs",
            articles=f"{URL}/v0/article",
        )

        return cls(
            meta=meta,
            content=content,
            links=links,
        )


class GetArticlesResponse(CommonResponseModel):
    @classmethod
    def create(
        cls,
        request: Request,
        articles: List[ArticlesResponseModel],
        total: int,
    ):
        meta = Meta(
            status=200,
            message=f"Articles retrieved successfully.",
            location=["Article", "retrieve"],
            processing_time=time() - request.scope.get("start_time"),
        )

        content = Content(articles=articles, total=total)

        path = urlparse(str(request.url.path)).path
        links = Links(
            self=f"{URL}{path}",
            docs=f"{URL}/docs",
            article=f"{URL}/v0/article",
        )

        return cls(
            meta=meta,
            content=content,
            links=links,
        )


class PatchArticleResponse(CommonResponseModel):
    @classmethod
    def create(
        cls,
        request: Request,
        article_id: int,
    ):
        meta = Meta(
            status=200,
            message=f"Article updated successfully.",
            location=["Article", "update"],
            processing_time=time() - request.scope.get("start_time"),
        )

        content = Content(article_id=article_id)

        path = urlparse(str(request.url.path)).path
        links = Links(
            self=f"{URL}{path}",
            docs=f"{URL}/docs",
            article=f"{URL}/v0/article/{article_id}",
        )

        return cls(
            meta=meta,
            content=content,
            links=links,
        )


class DeleteArticleResponse(CommonResponseModel):
    @classmethod
    def create(
        cls,
        request: Request,
    ):
        meta = Meta(
            status=200,
            message=f"Article deleted successfully.",
            location=["Article", "delete"],
            processing_time=time() - request.scope.get("start_time"),
        )

        content = Content()

        path = urlparse(str(request.url.path)).path
        links = Links(
            self=f"{URL}{path}",
            docs=f"{URL}/docs",
        )

        return cls(
            meta=meta,
            content=content,
            links=links,
        )


class PublishArticleResponse(CommonResponseModel):
    @classmethod
    def create(
        cls,
        request: Request,
        article_id: int,
    ):
        meta = Meta(
            status=200,
            message=f"Article published successfully.",
            location=["Article", "publish"],
            processing_time=time() - request.scope.get("start_time"),
        )

        content = Content(article_id=article_id)

        path = urlparse(str(request.url.path)).path
        links = Links(
            self=f"{URL}{path}",
            docs=f"{URL}/docs",
            article=f"{URL}/v0/article/{article_id}",
        )

        return cls(
            meta=meta,
            content=content,
            links=links,
        )


class SearchArticleResponse(CommonResponseModel):
    @classmethod
    def create(
        cls,
        request: Request,
        articles: List[SearchedArticlesResponseModel],
        total: int,
    ):
        meta = Meta(
            status=200,
            message=f"Articles retrieved successfully.",
            location=["Article", "search"],
            processing_time=time() - request.scope.get("start_time"),
        )

        content = Content(articles=articles, total=total)

        path = urlparse(str(request.url.path)).path
        links = Links(
            self=f"{URL}{path}",
            docs=f"{URL}/docs",
            article=f"{URL}/v0/article",
        )

        return cls(
            meta=meta,
            content=content,
            links=links,
        )


class DuplicateArticleResponse(CommonResponseModel):
    @classmethod
    def create(
        cls,
        request: Request,
        article_id: int,
    ):
        meta = Meta(
            status=201,
            message=f"Article duplicated successfully.",
            location=["Article", "duplicate"],
            processing_time=time() - request.scope.get("start_time"),
        )

        content = Content(article_id=article_id)

        path = urlparse(str(request.url.path)).path
        links = Links(
            self=f"{URL}{path}",
            docs=f"{URL}/docs",
            article=f"{URL}/v0/article/{article_id}",
        )

        return cls(
            meta=meta,
            content=content,
            links=links,
        )

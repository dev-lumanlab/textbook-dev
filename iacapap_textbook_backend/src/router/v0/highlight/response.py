from fastapi import Request
from time import time
from urllib.parse import urlparse
from typing import List, Optional
import os
from pydantic import BaseModel

from src.schema.response.common import Meta, Content, Links, CommonResponseModel

URL = os.getenv("DOMAIN_URL", "http://localhost:8000")


class HighlightResponseModel(BaseModel):
    id: int
    article_id: int
    book: str
    chapter: str
    user_id: int
    block: int
    start: int
    end: int
    text: Optional[str] = None
    created_at: str


class CreateHighlightResponse(CommonResponseModel):
    @classmethod
    def create(
        cls,
        request: Request,
        highlight_id: int,
    ):
        meta = Meta(
            status=201,
            message=f"Highlight created successfully.",
            location=["Highlight", "create"],
            processing_time=time() - request.scope.get("start_time"),
        )

        content = Content(highlight_id=highlight_id)

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


class GetHighlightResponse(CommonResponseModel):
    @classmethod
    def create(
        cls,
        request: Request,
        highlight: HighlightResponseModel,
    ):
        meta = Meta(
            status=200,
            message=f"Highlight retrieved successfully.",
            location=["Highlight", "retrieve"],
            processing_time=time() - request.scope.get("start_time"),
        )

        content = Content(highlight=highlight)

        path = urlparse(str(request.url.path)).path
        links = Links(
            self=f"{URL}{path}",
            docs=f"{URL}/docs",
            article=f"{URL}/v0/article/{highlight.article_id}",
        )

        return cls(
            meta=meta,
            content=content,
            links=links,
        )


class GetHighlightsResponse(CommonResponseModel):
    @classmethod
    def create(
        cls,
        request: Request,
        highlights: List[HighlightResponseModel],
        total: int,
    ):
        meta = Meta(
            status=200,
            message=f"Highlights retrieved successfully.",
            location=["Highlight", "retrieve"],
            processing_time=time() - request.scope.get("start_time"),
        )

        content = Content(
            highlights=highlights,
            total=total,
        )

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


class DeleteHighlightResponse(CommonResponseModel):
    @classmethod
    def create(
        cls,
        request: Request,
    ):
        meta = Meta(
            status=200,
            message=f"Highlight deleted successfully.",
            location=["Highlight", "delete"],
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

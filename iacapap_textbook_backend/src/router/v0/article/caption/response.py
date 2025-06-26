from fastapi import Request
from time import time
from urllib.parse import urlparse
from typing import List
import os
from pydantic import BaseModel

from src.schema.response.common import Meta, Content, Links, CommonResponseModel

URL = os.getenv("DOMAIN_URL", "http://localhost:8000")


class CaptionResponseModel(BaseModel):
    id: int
    article_id: int
    content: str


class CreateCaptionResponse(CommonResponseModel):
    @classmethod
    def create(
        cls,
        request: Request,
        caption_id: int,
    ):
        meta = Meta(
            status=201,
            message=f"Caption created successfully.",
            location=["Caption", "create"],
            processing_time=time() - request.scope.get("start_time"),
        )

        content = Content(caption_id=caption_id)

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


class GetCaptionResponse(CommonResponseModel):
    @classmethod
    def create(
        cls,
        request: Request,
        captions: List[CaptionResponseModel],
    ):
        meta = Meta(
            status=200,
            message=f"Caption retrieved successfully.",
            location=["Caption", "retrieve"],
            processing_time=time() - request.scope.get("start_time"),
        )

        content = Content(captions=captions)

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


class DeleteCaptionResponse(CommonResponseModel):
    @classmethod
    def create(
        cls,
        request: Request,
    ):
        meta = Meta(
            status=200,
            message=f"Caption deleted successfully.",
            location=["Caption", "delete"],
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

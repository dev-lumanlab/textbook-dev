from fastapi import Request
from time import time
from urllib.parse import urlparse
import os

from src.schema.response.common import Meta, Content, Links, CommonResponseModel
from pydantic import BaseModel
from typing import Optional

URL = os.getenv("DOMAIN_URL", "http://localhost:8000")


class ImageUploadResponse(CommonResponseModel):
    @classmethod
    def create(cls, request: Request, url: str):
        meta = Meta(
            status=201,
            message=f"Image uploaded successfully.",
            location=["Article", "Image", "upload"],
            processing_time=time() - request.scope.get("start_time"),
        )

        content = Content(
            url=url,
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

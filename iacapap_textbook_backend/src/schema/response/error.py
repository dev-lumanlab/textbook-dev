from fastapi import FastAPI, Request, status, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from pydantic import ValidationError

import os
from dotenv import load_dotenv
from urllib.parse import urlparse

from typing import Union, List
from time import time

from .common import CommonResponseModel, Meta, Content, Links

load_dotenv("/Users/dang-geun/Programming/PlayIdeaLab_service/SLAM/backend/.env")
DOMAIN_URL = os.getenv("DOMAIN_URL", "http://127.0.0.1:8000")


class ErrorResponse(CommonResponseModel):
    """
    422 에러를 제외한 모든 에러를 처리하기 위한 Response
    """

    @classmethod
    def create(
        cls,
        status_code: int,
        message: str,
        location: List[str],
        processing_time: float,
        request_path: str,
        additional_api: dict = None,
    ):
        meta = Meta(
            status=status_code,
            message=message,
            location=location,
            processing_time=processing_time,
        )

        content = Content()

        links = {
            "self": f"{DOMAIN_URL}{request_path}",
            "docs": f"{DOMAIN_URL}/docs",
        }

        if additional_api:
            additional_links = {
                k: f"{DOMAIN_URL}{v}" for k, v in additional_api.items()
            }
            links.update(additional_links)

        return cls(meta=meta, content=content, links=links)

    # 응답 예시
    class Config:
        json_schema_extra = {
            "examples": [
                {
                    "meta": {
                        "status": "401~422",
                        "message": "오류 메시지",
                        "location": ["body", "email"],
                        "processing_time": 0.0041959285736083984,
                    },
                    "content": {},
                    "links": {
                        "self": "http://127.0.0.1:8000/v1/user/login",
                        "docs": "http://127.0.0.1:8000/v1/docs",
                    },
                },
            ]
        }


class UnprocessableEntityResponse(CommonResponseModel):
    """HTTP_422 UNPROCESSABLE ENTITY 에러를 처리하기 위한 Response"""

    @classmethod
    def create(
        cls,
        message: str,
        location: List[str],
        processing_time: float,
        request_path: str,
        additional_api: dict = None,
    ):
        links = {
            "self": f"{DOMAIN_URL}{request_path}",
            "docs": f"{DOMAIN_URL}/docs",
        }
        if additional_api:
            additional_links = {
                k: f"{DOMAIN_URL}{v}" for k, v in additional_api.items()
            }
            links.update(additional_links)
        meta = Meta(
            status=status.HTTP_422_UNPROCESSABLE_ENTITY,
            message=message,
            location=location,
            processing_time=processing_time,
        )
        content = Content()

        return cls(meta=meta, content=content, links=links)

    class Config:
        json_schema_extra = {
            "examples": [
                {
                    "meta": {
                        "status": status.HTTP_422_UNPROCESSABLE_ENTITY,
                        "message": "unprocesable entity.",
                        "location": ["body", "age"],
                        "processing_time": 0.42,
                    },
                    "content": {},
                    "links": {
                        "self": f"{DOMAIN_URL}/v1/user",
                        "docs": f"{DOMAIN_URL}/v1/docs",
                        "main": f"{DOMAIN_URL}/",
                    },
                }
            ]
        }


async def HTTP_handler(request: Request, exception: HTTPException):
    """ "
    HTTPException을 처리하기 위한 핸들러"""
    try:
        print(exception)
        status_code = exception.status_code
        message = str(exception.detail)  # 예외의 detail을 직접 사용
        path = urlparse(str(request.url)).path  # url이 아니라 url.path

        _response = ErrorResponse.create(
            status_code=status_code,
            message=message,
            location=["Exception Handler"],  # 수정된 위치 정보
            processing_time=time()
            - request.scope.get("start_time", time()),  # 예외 처리
            request_path=path,
        )
        return JSONResponse(status_code=status_code, content=_response.model_dump())
    except Exception as e:
        return JSONResponse(
            status_code=500, content={"detail": "Internal Server Error"}
        )


async def validation_exception_handler(
    request: Request, exc: Union[RequestValidationError, ValidationError]
):
    """
    RequestValidationError, ValidationError을 처리하기 위한 핸들러"""
    error = exc.errors()
    print(error)
    if isinstance(error, str):
        raise HTTPException(status_code=400, detail=error)

    error = error[0]
    path = urlparse(str(request.url.path)).path
    _response = UnprocessableEntityResponse.create(
        message=error.get("msg", "Unknown :("),
        location=[*error.get("loc")],
        processing_time=time() - request.scope.get("start_time"),
        request_path=path,
    )
    return JSONResponse(status_code=422, content=_response.model_dump())


async def type_error_handler(request: Request, exc: TypeError):
    """
    TypeError를 처리하기 위한 핸들러"""
    path = urlparse(str(request.url.path)).path
    _response = UnprocessableEntityResponse.create(
        message=str(exc),
        location=["TypeError"],
        processing_time=time() - request.scope.get("start_time"),
        request_path=path,
    )
    return JSONResponse(status_code=422, content=_response.model_dump())


def error_handler(app: FastAPI):
    """
    FastAPI 인스턴스에 에러 핸들러를 등록하는 함수
    """
    app.add_exception_handler(HTTPException, HTTP_handler)
    app.add_exception_handler(RequestValidationError, validation_exception_handler)
    app.add_exception_handler(ValidationError, validation_exception_handler)
    app.add_exception_handler(TypeError, type_error_handler)

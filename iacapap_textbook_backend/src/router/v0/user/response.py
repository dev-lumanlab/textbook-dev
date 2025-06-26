from fastapi import Request
from time import time
from urllib.parse import urlparse
import os

from src.schema.response.common import Meta, Content, Links, CommonResponseModel
from pydantic import BaseModel
from typing import Optional

URL = os.getenv("DOMAIN_URL", "http://localhost:8000")


# USER RESPONSE
class UserResponseModel(BaseModel):
    id: int
    email: str
    name: Optional[str] = None
    level: int


class RegisterResponse(CommonResponseModel):
    @classmethod
    def create(
        cls,
        request: Request,
    ):
        meta = Meta(
            status=201,
            message=f"succesfully registeres.",
            location=["User", "register"],
            processing_time=time() - request.scope.get("start_time"),
        )

        content = Content()

        path = urlparse(str(request.url.path)).path
        links = Links(
            self=f"{URL}{path}",
            docs=f"{URL}/docs",
            login=f"{URL}/v1/user/login",
        )

        return cls(
            meta=meta,
            content=content,
            links=links,
        )

    class Config:
        json_schema_extra = {
            "examples": [
                {
                    "meta": {
                        "status": 201,
                        "message": "succesfully registered. Plz valid your email.",
                        "location": ["User", "register"],
                        "processing_time": 0.38141798973083496,
                    },
                    "content": {},
                    "links": {
                        "self": "http://127.0.0.1:8000/v1/user",
                        "docs": "http://127.0.0.1:8000/v1/docs#/User/register_user_post",
                        "login": "http://127.0.0.1:8000/v1/user/login",
                    },
                }
            ]
        }


class LoginResponse(CommonResponseModel):
    @classmethod
    def create(
        cls,
        request: Request,
        user_id: int,
        access_token: str,
        refresh_token: str,
    ):
        meta = Meta(
            status=200,
            message=f"succesfully signed in",
            location=[],
            processing_time=time() - request.scope.get("start_time"),
        )

        content = Content(
            user_id=user_id, access_token=access_token, refresh_token=refresh_token
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

    class Config:
        json_schema_extra = {
            "examples": [
                {
                    "meta": {
                        "status": 200,
                        "message": "succesfully signed in",
                        "location": ["User", "login"],
                        "processing_time": 0.324937105178833,
                    },
                    "content": {
                        "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJleGFtcGxlQHBsYXlpZGVhbGFiLmNvbSIsImV4cCI6MTcxMjEyNTI1MH0.ZjDjLpJoDsMryPEBZBg8YNICSA_4HEO5ULfutbAgo3U",
                        "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJleGFtcGxlQHBsYXlpZGVhbGFiLmNvbSIsImV4cCI6MTcxMzMyNDA1MH0.uxAImz1lijJumHNC4htEuHHg_CPgOvlt6NTFn8oKyag",
                    },
                    "links": {
                        "self": "http://127.0.0.1:8000/v1/user/login",
                        "docs": "http://127.0.0.1:8000/v1/docs#/User/login_user_login_post",
                    },
                },
            ]
        }


class ChangePasswordResponse(CommonResponseModel):
    @classmethod
    def create(
        cls,
        request: Request,
    ):
        meta = Meta(
            status=200,
            message=f"Password Changed",
            location=[],
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


class GetUserResponse(CommonResponseModel):
    @classmethod
    def create(
        cls,
        request: Request,
        user: UserResponseModel,
    ):
        meta = Meta(
            status=200,
            message=f"",
            location=[],
            processing_time=time() - request.scope.get("start_time"),
        )

        content = Content(user=user)

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


class GetUsersResponse(CommonResponseModel):
    @classmethod
    def create(
        cls,
        request: Request,
        users: list[UserResponseModel],
        total: int,
    ):
        meta = Meta(
            status=200,
            message=f"",
            location=[],
            processing_time=time() - request.scope.get("start_time"),
        )

        content = Content(users=users, total=total)

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


class PatchAuthResponse(CommonResponseModel):
    @classmethod
    def create(
        cls,
        request: Request,
    ):
        meta = Meta(
            status=200,
            message=f"Auth Patched",
            location=[],
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


class DeleteUserResponse(CommonResponseModel):
    @classmethod
    def create(
        cls,
        request: Request,
    ):
        meta = Meta(
            status=200,
            message=f"User Deleted",
            location=[],
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

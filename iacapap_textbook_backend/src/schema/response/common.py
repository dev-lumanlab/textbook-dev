from typing import Annotated, Sequence, List
from pydantic import BaseModel, Field
from starlette import status
import os

URL = os.getenv("DOMAIN_URL", "DOMAIN_URL")


class Meta(BaseModel):
    status: Annotated[
        int,
        Field(
            default=...,
            description="status code of the error",
            examples=[status.HTTP_401_UNAUTHORIZED, status.HTTP_404_NOT_FOUND],
        ),
    ]
    message: Annotated[
        str,
        Field(
            default=...,
            description="A message of the error",
            examples=["user is unauthorized", "entity is not found"],
        ),
    ]
    location: Annotated[
        List,
        Field(
            default=...,
            description="A location where the error occured",
            examples=["server", "body"],
        ),
    ]
    processing_time: Annotated[
        float,
        Field(
            default=...,
            description="Spent time to process request",
            examples=[0.4, 1, 3.5],
        ),
    ]


class Content(BaseModel):
    class Config:
        extra = "allow"


class Links(BaseModel):
    self: Annotated[
        str,
        Field(
            default=...,
            description="requested link",
            examples=[f"{URL}/v1/user"],
        ),
    ]
    docs: Annotated[
        str,
        Field(
            default=...,
            description="documentation link",
            examples=[
                f"{URL}/docs#/v1/register",
            ],
        ),
    ]

    class Config:
        extra = "allow"


class CommonResponseModel(BaseModel):
    """
    기본적인 응답을 위한 모델
    """

    meta: Meta = Field(
        default=...,
        description="Meta data of response",
        examples=[
            {
                "status": 200,
                "message": "",
                "location": ["server"],
                "processing_time": 0.4,
            },
        ],
    )
    content: Content = Field(
        default=...,
        description="Data returned by request",
        examples=[
            {"access_token": "string", "token_type": "string", "username": "string"},
            {},
        ],
    )
    links: Links = Field(
        default=...,
        description="available links according to request",
        examples=[
            {
                "self": f"{URL}/v1/user",
                "docs": f"{URL}#/v1/register",
                "main": f"{URL}",
            },
        ],
    )

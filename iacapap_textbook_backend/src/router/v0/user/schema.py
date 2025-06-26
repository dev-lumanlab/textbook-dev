from typing import Annotated

from pydantic import BaseModel, EmailStr, Field, field_validator, ValidationInfo


class RegisterSchema(BaseModel):
    email: Annotated[
        EmailStr,
        Field(
            default=...,
            serialization_alias="email",
            description="Existing Email",
            examples=[
                "wlgh7407@playidealab.com",
            ],
        ),
    ]
    password1: Annotated[
        str,
        Field(
            default=...,
            serialization_alias="password",
            description="Your Password",
            examples=[
                "password1234",
            ],
        ),
    ]
    password2: Annotated[
        str,
        Field(
            default=...,
            serialization_alias="password check",
            description="type same password again",
            examples=[
                "password1234",
            ],
        ),
    ]
    name: Annotated[
        str,
        Field(
            default=None,
            serialization_alias="name",
            description="Your Name",
            examples=[
                "지호",
            ],
        ),
    ]

    @field_validator("email", "password1", "password2", "name")
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError("빈 값은 허용되지 않습니다.")
        return v

    @field_validator("password2")
    def passwords_match(cls, v, info: ValidationInfo):
        if "password1" in info.data and v != info.data["password1"]:
            raise ValueError("비밀번호가 일치하지 않습니다.")
        return v


class LoginSchema(BaseModel):
    email: Annotated[
        EmailStr,
        Field(
            default=...,
            serialization_alias="email",
            description="Existing Email",
            examples=[
                "wlgh7407@playidealab.com",
            ],
        ),
    ]
    password: Annotated[
        str,
        Field(
            default=...,
            serialization_alias="password",
            description="Your Password",
            examples=[
                "password1234",
            ],
        ),
    ]

    @field_validator("email", "password")
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError("빈 값은 허용되지 않습니다.")
        return v


class ChangePasswordSchema(BaseModel):
    email: Annotated[
        EmailStr,
        Field(
            default=...,
            serialization_alias="email",
            description="Existing Email",
            examples=["wlgh7407@playidealab.com"],
        ),
    ]
    new_password1: Annotated[
        str,
        Field(
            default=...,
            serialization_alias="password",
            description="Your Password",
            examples=[
                "password1234",
            ],
        ),
    ]
    new_password2: Annotated[
        str,
        Field(
            default=...,
            serialization_alias="password check",
            description="type same password again",
            examples=[
                "password1234",
            ],
        ),
    ]

    @field_validator("new_password1", "new_password2")
    def passwords_match(cls, v, info: ValidationInfo):
        if "new_password1" in info.data and v != info.data["new_password1"]:
            raise ValueError("비밀번호가 일치하지 않습니다.")
        return v

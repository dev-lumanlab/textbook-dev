from typing import Annotated

from pydantic import BaseModel, EmailStr, Field, field_validator, ValidationInfo


class CreateCaptionSchema(BaseModel):
    content: Annotated[
        str,
        Field(
            default=...,
            serialization_alias="content",
            description="Caption Content",
            examples=[
                "I'll try next time.",
            ],
        ),
    ]

    @field_validator("content")
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError("빈 값은 허용되지 않습니다.")
        return v

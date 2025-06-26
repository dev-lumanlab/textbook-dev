from typing import Annotated

from pydantic import BaseModel, EmailStr, Field, field_validator, ValidationInfo


class CreateArticleSchema(BaseModel):
    book: Annotated[
        str,
        Field(
            default=...,
            serialization_alias="book",
            description="Article Book",
            examples=[
                "Cooking",
            ],
        ),
    ]
    chapter: Annotated[
        str,
        Field(
            default=...,
            serialization_alias="chapter",
            description="Article Chapter",
            examples=[
                "Chapter 1",
            ],
        ),
    ]
    title: Annotated[
        str,
        Field(
            default=...,
            serialization_alias="title",
            description="Article Title",
            examples=[
                "How to make a cake",
            ],
        ),
    ]
    content: Annotated[
        str,
        Field(
            default=...,
            serialization_alias="content",
            description="Article Content",
            examples=[
                "First, you need to prepare the ingredients.",
            ],
        ),
    ]

    @field_validator("book", "title", "chapter", "content")
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError("빈 값은 허용되지 않습니다.")
        return v

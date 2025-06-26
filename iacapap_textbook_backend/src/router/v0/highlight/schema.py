from typing import Annotated, Optional

from pydantic import BaseModel, EmailStr, Field, field_validator, ValidationInfo


class CreateHighlightSchema(BaseModel):
    block: Annotated[
        int,
        Field(
            ...,
            description="Block number of the highlight",
            example=0,
            ge=0,
        ),
    ]
    start: Annotated[
        int,
        Field(
            ...,
            description="Start position of the highlight",
            example=0,
            ge=0,
        ),
    ]
    end: Annotated[
        int,
        Field(
            ...,
            description="End position of the highlight",
            example=0,
            ge=0,
        ),
    ]
    text: Optional[str] = None

    @field_validator("block", "start", "end")
    def check_none(cls, v, info: ValidationInfo):
        if v is None:
            raise ValueError("Cannot be None")
        return v

    @field_validator("end")
    def validate_start_end(cls, v, info: ValidationInfo):
        if "start" in info.data and v <= info.data["start"]:
            raise ValueError("End position must be greater than start position")
        return v

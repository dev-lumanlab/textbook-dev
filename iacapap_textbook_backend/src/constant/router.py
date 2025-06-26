from enum import StrEnum


class APIPath(StrEnum):
    DOCUMENTATIONS: str = "/docs"
    USER: str = "/user"
    ARTICLE: str = "/article"


class APIBoundary(StrEnum):
    V1: str = "/v1"

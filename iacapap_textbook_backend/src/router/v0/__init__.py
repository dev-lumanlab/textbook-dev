from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from src.constant import APIPath, APIBoundary

# FastAPI 객체 생성
app = FastAPI(
    title="webwork v1 API",
    description="First version of webwork 1",
    version="0.1.0",
    contact={"email": "wlgh7407@playidealab.com"},
    # openapi_url=None
)


from .user import router as user_router
from .article import router as article_router
from .highlight import router as highlight_router

# 라우터 등록
app.include_router(user_router, prefix=APIPath.USER, tags=["USER"])
app.include_router(article_router, prefix=APIPath.ARTICLE, tags=["ARTICLE"])
app.include_router(highlight_router, prefix="/highlight", tags=["HIGHLIGHT"])


from src.middleware.utils import ProcessTimeHeaderMiddleware
from fastapi.middleware.cors import CORSMiddleware

# 미들웨어 등록
origins = [
    "https://iacapaptextbook2.com",
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(ProcessTimeHeaderMiddleware)

from src.schema.response.error import error_handler

# 에러 핸들러 등록
error_handler(app)

from typing import Annotated, Optional

from fastapi import APIRouter, status, HTTPException
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from src.database import get_db

from .schema import RegisterSchema, ChangePasswordSchema
from .response import (
    RegisterResponse,
    LoginResponse,
    ChangePasswordResponse,
    GetUserResponse,
    GetUsersResponse,
    UserResponseModel,
    PatchAuthResponse,
    DeleteUserResponse,
)
from .crud import *

router = APIRouter()


@router.post(
    "",
    response_model=RegisterResponse,
    status_code=status.HTTP_201_CREATED,
)
def register(
    register_schema: RegisterSchema, request: Request, db: Session = Depends(get_db)
):
    """
    Description \n
        1. Create an User.
        2. Send a validation mail to written email.
    """
    try:
        # 중복 검사
        if db_check_email_exist(db=db, email=register_schema.email):
            raise HTTPException(
                status_code=409,
                detail={"msg": "이미 가입된 이메일입니다.", "loc": ["email"]},
            )

        # User 테이블에 유저 추가
        user_id = db_create_user(db=db, register_schema=register_schema)

        # UserData 테이블에 유저 추가
        db_create_user_data(db=db, user_id=user_id, name=register_schema.name)

        # 응답 모델 생성
        res = RegisterResponse.create(request)
        db.commit()
        return JSONResponse(
            status_code=status.HTTP_201_CREATED, content=res.model_dump()
        )
    except Exception as e:
        db.rollback()
        if isinstance(e, HTTPException):
            raise e
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={"msg": str(e), "loc": ["server"]},
        )


@router.post(
    "/login",
    response_model=LoginResponse,
    status_code=status.HTTP_200_OK,
)
def login(login_schema: LoginSchema, request: Request, db: Session = Depends(get_db)):
    """
    Description \n
        1. Login
        2. Return access_token and refresh_token
    """
    try:
        # 로그인
        db_user = db_get_user_by_email(db=db, email=login_schema.email)
        if not db_login_user(db=db, db_user=db_user, password=login_schema.password):
            raise HTTPException(
                status_code=401,
                detail={"msg": "비밀번호가 일치하지 않습니다.", "loc": ["password"]},
            )

        # 토큰 생성
        access_token = db_generate_token(email=login_schema.email, token_type="ACCESS")
        refresh_token = db_generate_token(
            email=login_schema.email, token_type="REFRESH"
        )

        # 응답 모델 생성
        res = LoginResponse.create(
            request=request,
            user_id=db_user.id,
            access_token=access_token,
            refresh_token=refresh_token,
        )
        return JSONResponse(status_code=status.HTTP_200_OK, content=res.model_dump())
    except Exception as e:
        db.rollback()
        if isinstance(e, HTTPException):
            raise e
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={"msg": str(e), "loc": ["server"]},
        )


@router.patch(
    "/password",
    response_model=ChangePasswordResponse,
    status_code=status.HTTP_200_OK,
)
def change_password(
    change_password_schema: ChangePasswordSchema,
    request: Request,
    db: Session = Depends(get_db),
):
    """
    Description \n
        1. Change Password
    """
    try:
        # 현재 유저 정보 가져오기
        db_user = db_get_user_by_email(db=db, email=change_password_schema.email)

        # 비밀번호 변경
        db_change_password(
            db=db,
            user_id=db_user.id,
            new_password=change_password_schema.new_password1,
        )

        # 응답 모델 생성
        response = ChangePasswordResponse.create(request=request)
        db.commit()
        return JSONResponse(
            status_code=response.meta.status,
            content=response.model_dump(),
        )
    except Exception as e:
        db.rollback()
        if isinstance(e, HTTPException):
            raise e
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e),
        )


@router.get(
    "",
    response_model=GetUserResponse,
    status_code=status.HTTP_200_OK,
)
def get_user(
    request: Request,
    email: Optional[str] = None,
    page: int = 1,
    limit: int = 10,
    db: Session = Depends(get_db),
):
    """
    Description \n
        1. Get User Information
    """
    try:
        if email:
            # 유저 정보 가져오기
            db_user = db_get_user_by_email(db=db, email=email)

            # 해당 유저가 없으면 404 에러
            if db_user is None:
                raise HTTPException(
                    status_code=404,
                    detail={"msg": "User not found", "loc": ["email"]},
                )

            # 응답 모델 생성
            response = GetUserResponse.create(
                request=request,
                user=UserResponseModel(
                    id=db_user.id,
                    email=db_user.email,
                    name=db_user.user_data.name,
                    level=db_user.level,
                ),
            )
            return JSONResponse(
                status_code=response.meta.status,
                content=response.model_dump(),
            )
        else:
            authorization = request.headers.get("Authorization")
            if not authorization:
                raise HTTPException(
                    status_code=401,
                    detail={"msg": "인증이 필요합니다.", "loc": ["Authorization"]},
                )
            authorization = authorization.split(" ")
            credentials = HTTPAuthorizationCredentials(
                scheme=authorization[0], credentials=authorization[1]
            )
            cur_user = get_auth(credentials=credentials, db=db)
            if cur_user.level != 2:
                raise HTTPException(
                    status_code=403,
                    detail={"msg": "권한이 없습니다.", "loc": ["User", "Get"]},
                )

            # 유저 리스트 가져오기
            db_users = db_get_users(db=db, skip=(page - 1) * limit, limit=limit)
            total = db_count_users(db=db)

            # 응답 모델 생성
            response = GetUsersResponse.create(
                request=request,
                users=[
                    UserResponseModel(
                        id=db_user.id,
                        email=db_user.email,
                        name=db_user.user_data.name,
                        level=db_user.level,
                    )
                    for db_user in db_users
                ],
                total=total,
            )
            return JSONResponse(
                status_code=response.meta.status,
                content=response.model_dump(),
            )
    except Exception as e:
        db.rollback()
        if isinstance(e, HTTPException):
            raise e
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e),
        )


@router.get(
    "/auth",
    response_model=GetUserResponse,
    status_code=status.HTTP_200_OK,
)
def get_user_by_token(
    request: Request,
    user: User = Depends(get_auth),
    db: Session = Depends(get_db),
):
    """
    Description \n
        1. Get User Information by Token
    """
    try:
        # 응답 모델 생성
        response = GetUserResponse.create(
            request=request,
            user=UserResponseModel(
                id=user.id,
                email=user.email,
                name=user.user_data.name,
                level=user.level,
            ),
        )
        return JSONResponse(
            status_code=response.meta.status,
            content=response.model_dump(),
        )
    except Exception as e:
        db.rollback()
        if isinstance(e, HTTPException):
            raise e
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e),
        )


@router.patch(
    "/auth",
    response_model=PatchAuthResponse,
    status_code=status.HTTP_200_OK,
)
def patch_auth(
    request: Request,
    user: User = Depends(get_auth),
    email: str = None,
    level: int = 0,
    db: Session = Depends(get_db),
):
    """
    Description \n
        1. Patch Auth
    """
    try:
        # 관리자만 권한 부여 가능
        if user.level != 2:
            raise HTTPException(
                status_code=403,
                detail={"msg": "권한이 없습니다.", "loc": ["admin"]},
            )

        if level not in [0, 1]:
            raise HTTPException(
                status_code=400,
                detail={"msg": "level은 0 또는 1이어야 합니다.", "loc": ["level"]},
            )

        # 권한 부여
        db_patch_auth(db=db, email=email, level=level)

        # 응답 모델 생성
        response = PatchAuthResponse.create(
            request=request,
        )
        db.commit()
        return JSONResponse(
            status_code=response.meta.status,
            content=response.model_dump(),
        )
    except Exception as e:
        db.rollback()
        if isinstance(e, HTTPException):
            raise e
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e),
        )


@router.delete(
    "",
    response_model=DeleteUserResponse,
    status_code=status.HTTP_200_OK,
)
def delete_user(
    request: Request,
    user_id: int,
    cur_user: User = Depends(get_auth),
    db: Session = Depends(get_db),
):
    """
    Description \n
        1. Delete User
    """
    try:
        # Manater만 삭제 가능
        if cur_user.level != 2:
            raise HTTPException(
                status_code=403,
                detail={"msg": "권한이 없습니다.", "loc": ["User", "Delete"]},
            )

        # 유저 삭제
        db_delete_user(db=db, user_id=user_id)

        # 응답 모델 생성
        response = DeleteUserResponse.create(
            request=request,
        )
        db.commit()
        return JSONResponse(
            status_code=response.meta.status,
            content=response.model_dump(),
        )
    except Exception as e:
        db.rollback()
        if isinstance(e, HTTPException):
            raise e
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e),
        )

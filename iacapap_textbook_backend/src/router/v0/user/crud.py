from typing import List

from fastapi import status, HTTPException, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from passlib.context import CryptContext
from sqlalchemy.orm import Session
from jose import jwt, JWTError
from datetime import timedelta, datetime, timezone
import os

from src.model import *
from src.database import get_db
from .schema import RegisterSchema, LoginSchema

ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 3  # 3 days
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 3
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

"""
Functions of Auth
"""

access_oauth2_scheme = HTTPBearer()


def get_auth(
    credentials: HTTPAuthorizationCredentials = Depends(access_oauth2_scheme),
    db: Session = Depends(get_db),
):
    try:
        # 액세스 토큰 가져오기
        access_token = credentials.credentials

        # 토큰 디코딩
        payload = jwt.decode(access_token, SECRET_KEY, algorithms=[ALGORITHM])

        # 토큰 타입 검사
        if payload.get("token_type") != "ACCESS":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token is not valid",
            )

        # 페이로드에서 이메일 가져오기
        email: str = payload.get("sub")

        # 이메일로 유저 가져오기
        db_user = db_get_user_by_email(db=db, email=email)

        return db_user
    except:
        # 토큰이 유효하지 않을 때 (토큰이 없거나, 만료되었거나, 잘못된 토큰일 때)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token is not valid",
        )


"""
Functions that Controls "User"
"""


def db_create_user(db: Session, register_schema: RegisterSchema) -> int:
    """
    user_id 반환
    """

    db_user = User(
        email=register_schema.email,
        password=pwd_context.hash(register_schema.password1),  # 비밀번호 암호화
    )
    db.add(db_user)
    db.flush()
    return db_user.id


def db_check_email_exist(db: Session, email: str) -> bool:
    """
    True -> 해당 이메일을 가진 사람이 존재함
    """
    result = db.query(User).filter(User.email == email).first()
    if result:
        return True


def db_get_users(db: Session, skip: int, limit: int) -> List[User]:
    return db.query(User).order_by(User.level.desc()).offset(skip).limit(limit).all()


def db_count_users(db: Session) -> int:
    return db.query(User).count()


def db_get_user_by_email(db: Session, email: str) -> User:
    db_user = db.query(User).filter(User.email == email).first()
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="해당 이메일을 가진 사용자가 존재하지 않습니다.",
        )
    return db_user


def db_get_user_by_id(db: Session, user_id: int) -> User:
    db_user = db.query(User).filter(User.id == user_id).first()
    return db_user


def db_login_user(db: Session, db_user: User, password: str) -> bool:
    # 비밀번호 검증
    result = pwd_context.verify(password, db_user.password)
    return result


def db_generate_token(email: str, token_type: str) -> jwt:
    if token_type == "ACCESS":
        EXPIRE_MINIUTES = ACCESS_TOKEN_EXPIRE_MINUTES
    elif token_type == "REFRESH":
        EXPIRE_MINIUTES = REFRESH_TOKEN_EXPIRE_MINUTES
    else:
        raise ValueError("토큰 타입이 잘못되었습니다.")

    access_data = {
        "sub": email,
        "exp": datetime.now(timezone.utc) + timedelta(minutes=EXPIRE_MINIUTES),
        "token_type": token_type,
    }

    return jwt.encode(access_data, SECRET_KEY, algorithm=ALGORITHM)


def db_change_password(db: Session, user_id: int, new_password: str) -> None:
    db_user = db_get_user_by_id(db=db, user_id=user_id)
    db_user.password = pwd_context.hash(new_password)


def db_delete_user(db: Session, user_id: int) -> None:
    db_user = db_get_user_by_id(db=db, user_id=user_id)
    db.delete(db_user)


def db_patch_auth(db: Session, email: str, level: int):
    db_user = db_get_user_by_email(db=db, email=email)
    db_user.level = level


"""
Functions that controls "UserData"
"""


def db_create_user_data(db: Session, user_id: int, name: str) -> None:
    db_user_data = UserData(user_id=user_id, name=name)
    db.add(db_user_data)

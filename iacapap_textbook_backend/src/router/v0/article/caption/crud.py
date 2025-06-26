from fastapi import status, HTTPException, UploadFile
from sqlalchemy.orm import Session

from src.model import Caption
from datetime import datetime


def db_create_caption(db: Session, article_id: int, user_id: int, content: str) -> int:
    # 캡션 생성
    db_caption = Caption(
        article_id=article_id,
        content=content,
    )
    db.add(db_caption)
    db.flush()
    return db_caption.id


def db_get_captions(db: Session, user_id: int, article_id: int) -> Caption:
    # 캡션 가져오기
    db_caption = db.query(Caption).filter(Caption.article_id == article_id)
    if not db_caption:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Caption not found",
        )
    return db_caption


def db_delete_caption(db: Session, caption_id: int):
    # 캡션 삭제
    db_caption = db.query(Caption).filter(Caption.id == caption_id).first()
    db.delete(db_caption)
    db.flush()
    return

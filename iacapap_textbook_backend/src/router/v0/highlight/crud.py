from fastapi import status, HTTPException, UploadFile
from sqlalchemy.orm import Session

from src.model import Highlight
from datetime import datetime


def db_create_highlight(
    db: Session,
    article_id: int,
    user_id: int,
    block: int,
    start: int,
    end: int,
    text: str = None,
) -> int:
    # 하이라이트 생성
    db_highlight = Highlight(
        article_id=article_id,
        user_id=user_id,
        block=block,
        start=start,
        end=end,
        text=text,
        created_at=datetime.now(),
    )
    db.add(db_highlight)
    db.flush()
    return db_highlight.id


def db_get_highlight(db: Session, highlight_id: int) -> Highlight:
    # 하이라이트 가져오기 (한개)
    db_highlight = db.query(Highlight).filter(Highlight.id == highlight_id).first()
    if db_highlight is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Highlight not found",
        )
    return db_highlight


def db_count_highlights_from_user(db: Session, user_id: int):
    # 하이라이트 개수 가져오기 (유저)
    return db.query(Highlight).filter(Highlight.user_id == user_id).count()


def db_get_highlights_from_user(db: Session, user_id: int, skip: int, limit: int):
    # 하이라이트 가져오기 (유저)
    return (
        db.query(Highlight)
        .filter(Highlight.user_id == user_id)
        .order_by(Highlight.created_at.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )


def db_get_highlights_from_article(db: Session, user_id: int, article_id: int):
    # 하이라이트 가져오기 (유저, 아티클)
    return (
        db.query(Highlight)
        .filter(Highlight.user_id == user_id, Highlight.article_id == article_id)
        .all()
    )


def db_delete_highlight(db: Session, highlight_id: int):
    # 하이라이트 삭제
    db_highlight = db.query(Highlight).filter(Highlight.id == highlight_id).first()
    if db_highlight is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Highlight not found",
        )
    db.delete(db_highlight)
    db.flush()
    return highlight_id

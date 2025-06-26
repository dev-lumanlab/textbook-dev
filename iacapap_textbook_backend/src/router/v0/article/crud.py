from fastapi import status, HTTPException, UploadFile
from sqlalchemy.orm import Session
from sqlalchemy import or_, desc

from src.model import Article
from datetime import datetime
import copy


def db_create_article(
    db: Session,
    book: str,
    title: str,
    content: str,
    content_textonly: str,
    chapter: str,
    user_id: int,
    thumbnail: str = None,
) -> int:
    # 아티클 생성
    db_article = Article(
        published=False,
        book=book,
        title=title,
        content=content,
        content_textonly=content_textonly,
        chapter=chapter,
        last_update=datetime.now(),
        creator_id=user_id,
        thumbnail=thumbnail,
    )
    db.add(db_article)
    db.flush()
    return db_article.id


def db_get_article(db: Session, article_id: int) -> Article:
    # id를 이용해서 아티클 한개 가져오기 (없으면 404 에러)
    db_article = db.query(Article).filter(Article.id == article_id).first()
    if db_article is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Article not found",
        )
    return db_article


def db_get_articles(db: Session, skip: int, limit: int, published: bool = True):
    # published 여부에 따라 아티클 리스트 가져오기, 기본값은 True, skip, limit은 페이징을 위한 값
    return (
        db.query(Article)
        .filter(Article.published == published)
        .order_by(
            desc(Article.last_publish) if published else desc(Article.last_update)
        )
        .offset(skip)
        .limit(limit)
        .all()
    )


def db_count_articles(db: Session, published: bool = True):
    # published 여부에 따라 아티클 개수 가져오기, 기본값은 True
    return db.query(Article).filter(Article.published == published).count()


def db_search_articles(
    db: Session, keyword: str, skip: int, limit: int, published: bool = True
):
    # keyword를 포함하는 아티클 리스트 가져오기, published 여부에 따라 가져오는 아티클이 다름
    return (
        db.query(Article)
        .filter(Article.published == published)
        .filter(or_(Article.content_textonly.like(f"%{keyword}%")))
        .order_by(
            desc(Article.last_publish) if published else desc(Article.last_update)
        )
        .offset(skip)
        .limit(limit)
        .all()
    )


def db_count_search_articles(db: Session, keyword: str, published: bool = True):
    # keyword를 포함하는 아티클 개수 가져오기, published 여부에 따라 가져오는 아티클이 다름
    return (
        db.query(Article)
        .filter(Article.published == published)
        .filter(or_(Article.content_textonly.like(f"%{keyword}%")))
        .count()
    )


def db_duplicate_article(db: Session, article_id: int, user_id: int):
    # 퍼블리쉬된 아티클을 복사해서 수정 가능한 아티클로 저장
    db_article = db.query(Article).filter(Article.id == article_id).first()
    if db_article is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Article not found",
        )
    new_article = Article(
        published=False,
        book=db_article.book,
        title=db_article.title,
        chapter=db_article.chapter,
        content=db_article.content,
        content_textonly=db_article.content_textonly,
        creator_id=user_id,
        last_update=datetime.now(),
        thumbnail=db_article.thumbnail,
    )
    db.add(new_article)
    db.flush()
    return new_article.id


def db_update_article(
    db: Session,
    article_id: int,
    book: str,
    title: str,
    content: str,
    content_textonly: str,
    chapter: str,
    thumbnail: str = None,
):
    # 아티클 수정
    db_article = db.query(Article).filter(Article.id == article_id).first()
    db_article.book = book
    db_article.title = title
    db_article.chapter = chapter
    db_article.content = content
    db_article.content_textonly = content_textonly
    db_article.thumbnail = thumbnail
    db_article.last_update = datetime.now()
    db.flush()
    return db_article.id


def db_publish_article(db: Session, article_id: int, query: bool = False):
    # 아티클 퍼블리시하기 / 해제하기
    db_article = db.query(Article).filter(Article.id == article_id).first()
    if db_article is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Article not found",
        )
    if query:
        # 퍼블리시할때에는 새로운 아티클을 생성
        published_article = Article(
            published=True,
            book=db_article.book,
            chapter=db_article.chapter,
            title=db_article.title,
            content=db_article.content,
            content_textonly=db_article.content_textonly,
            last_update=db_article.last_update,
            last_publish=datetime.now(),
            creator_id=db_article.creator_id,
            thumbnail=db_article.thumbnail,
        )
        db.add(published_article)
        db.flush()
        return published_article.id
    else:
        # 퍼블리시 해제할때에는 published를 False로 변경
        db_article.published = False
        db.flush()
        return db_article.id


def db_delete_article(db: Session, article_id: int):
    # 아티클 삭제
    db_article = db.query(Article).filter(Article.id == article_id).first()
    if db_article is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Article not found",
        )
    db.delete(db_article)
    db.flush()
    return article_id

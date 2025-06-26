from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
    ForeignKey,
    Boolean,
)
from sqlalchemy.orm import relationship

from src.database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    level = Column(Integer, default=0)

    # 유저 삭제시 관련 데이터도 삭제
    user_data = relationship(
        "UserData", back_populates="user", uselist=False, cascade="all, delete"
    )
    articles = relationship("Article", back_populates="creator")
    # 유저 삭제시 하이라이트도 삭제
    highlights = relationship("Highlight", back_populates="user", cascade="all, delete")


class UserData(Base):
    __tablename__ = "user_data"

    user_id = Column(
        Integer, ForeignKey("user.id", ondelete="CASCADE"), primary_key=True
    )
    name = Column(String, index=True)

    user = relationship("User", back_populates="user_data")


class Article(Base):
    __tablename__ = "article"

    id = Column(Integer, primary_key=True, index=True)
    published = Column(Boolean, default=False, index=True, nullable=False)
    book = Column(String, nullable=False)
    chapter = Column(String, nullable=False)
    title = Column(String, nullable=False)
    content = Column(Text)
    content_textonly = Column(Text)
    last_update = Column(DateTime)
    last_publish = Column(DateTime)
    creator_id = Column(Integer, ForeignKey("user.id"))
    thumbnail = Column(String)

    creator = relationship("User", back_populates="articles")
    # 게시글 삭제시 하이라이트도 삭제
    highlights = relationship(
        "Highlight", back_populates="article", cascade="all, delete"
    )


class Highlight(Base):
    __tablename__ = "highlight"

    id = Column(Integer, primary_key=True, index=True)
    article_id = Column(Integer, ForeignKey("article.id", ondelete="CASCADE"))
    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"))
    block = Column(Integer, nullable=False)
    start = Column(Integer, nullable=False)
    end = Column(Integer, nullable=False)
    text = Column(Text)
    created_at = Column(DateTime)

    user = relationship("User", back_populates="highlights")
    article = relationship("Article", back_populates="highlights")


class Caption(Base):
    __tablename__ = "caption"

    id = Column(Integer, primary_key=True, index=True)
    article_id = Column(Integer, ForeignKey("article.id"))
    content = Column(Text)

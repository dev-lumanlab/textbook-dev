from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from dotenv import load_dotenv
import os

# .env 로드하기
load_dotenv()

# 환경변수에서 DATABASE_URL 가져오기
DB_URL = os.getenv("DB_URL")

# 엔진 생성하기
engine = create_engine(DB_URL)

# 세션 생성하기
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base 클래스 생성하기
Base = declarative_base()


# 다른 파일에서 사용할 수 있도록 세션을 반환하는 함수 생성하기
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:  # 세션을 닫기
        db.close()

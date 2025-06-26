from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn
from dotenv import load_dotenv

from src.router import v0

app = FastAPI(root_path="/back")


# 기본 라우터
@app.get("/")
def read_root():
    return {"Hello": "World"}


# 메인 라우터, 버저닝을 위해 v0도메인 이용
app.mount("/v0", v0.app)

# 스토리지 라우터, 스토리지 파일을 가져오기 위한 라우터
app.mount("/storage", StaticFiles(directory="./src/storage"), name="storage")

if __name__ == "__main__":
    uvicorn.run("src.main:app", reload=True, host="0.0.0.0", port=8000)

from fastapi import UploadFile
import aiofiles

from bs4 import BeautifulSoup
import base64
import hashlib
import secrets

import os

URL = os.getenv("DOMAIN_URL")


def save_img(img_data: str) -> str:
    # b64 이미지를 저장하고 url 저장
    format, img_data = img_data.split(";base64,")

    image_type = format.split("/")[-1]

    # 이미지 저장
    image_data = base64.b64decode(img_data)
    file_name = f"{hashlib.md5(image_data).hexdigest()}.{image_type}"
    file_path = f"./src/storage/{file_name}"
    with open(file_path, "wb") as f:
        f.write(image_data)

    # 저장한 이미지 url 이용
    return f"{URL}/storage/{file_name}"


def parse_html(html_data: str) -> str:
    # html 이미지 파싱
    soup = BeautifulSoup(html_data, "lxml")

    # 이미지 태그 찾기
    imgs = soup.find_all("img")

    # 이미지 태그의 src 속성을 가져와서 저장하고 url로 변경
    for img in imgs:
        src = img.get("src")
        if src.startswith("data:image"):
            img_url = save_img(src)
            img["src"] = img_url  # 이미지 소스 업데이트

    return str(soup)


def get_text(html_data: str) -> str:
    # html 태그 제거
    soup = BeautifulSoup(html_data, "lxml")
    text = soup.get_text()
    return text


def get_thumbnail(html_data: str) -> str:
    # html에서 썸네일 이미지 파싱 (첫번째 이미지 가져오기)
    soup = BeautifulSoup(html_data, "lxml")

    imgs = soup.find_all("img")

    # 이미지가 없을 경우
    if not imgs:
        return None

    src = imgs[0].get("src")
    return src


async def upload_image(file: UploadFile) -> str:
    # 이미지 업로드
    randstr = secrets.token_urlsafe(16)
    img_name = randstr + "_" + file.filename
    destination = f"src/storage/{img_name}"
    url = f"{URL}/storage/{img_name}"
    async with aiofiles.open(destination, "wb") as f:
        await f.write(await file.read())
    return url

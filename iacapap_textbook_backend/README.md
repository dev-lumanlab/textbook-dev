# IACAPAP 웹 사이트

사이트 주소 : https://iacapaptextbook2.com  
API 문서 주소 : https://iacapaptextbook2.com/back/v0/docs

## 기술 스택

### Backend

- poetry (의존성 관리)
- FastAPI
- alembic (데이터베이스 마이그레이션 관리)
- sqlalchemy (데이터베이스 쿼리 ORM)

## 폴더 구조

```
📦 backend
┣ 📂.venv                          # 가상환경
┣ 📂logs                           # nginx와 백엔드 서버 로그
┣ 📂migrations                     # 데이터베이스 마이그레이션 관련
┃ ┗ 📂versions                     # 소실되지 않도록 주의.
┣ 📂src
┃ ┣ 📂constant                     # enum 저장용
┃ ┣ 📂middleware                   # 백엔드 서버에 달릴 미들웨어 함수들
┃ ┣ 📂schema
┃ ┃ ┗ 📂response                   # 기본 응답 클래스
┃ ┣ 📂storage                      # 파싱 / 업로드한 이미지 저장
┃ ┣ 📂router
┃ ┃ ┣ 📂v0
┃ ┃ ┃ ┣ 📂article
┃ ┃ ┃ ┃ ┣ 📂caption
┃ ┃ ┃ ┃ ┃   ┣ 📜__init__.py        # 상위 폴더에서 참조할 수 있게 패키지화
┃ ┃ ┃ ┃ ┃   ┣ 📜crud.py            # CRUD 작업
┃ ┃ ┃ ┃ ┃   ┣ 📜response.py        # 응답 관련 파일
┃ ┃ ┃ ┃ ┃   ┣ 📜router.py          # 라우팅 관련 파일
┃ ┃ ┃ ┃ ┃   ┗ 📜schema.py          # 스키마 정의 파일
┃ ┃ ┃ ┃ ┣ 📂image
┃ ┃ ┃ ┃ ┃   ┣ 📜__init__.py      
┃ ┃ ┃ ┃ ┃   ┣ 📜crud.py      
┃ ┃ ┃ ┃ ┃   ┣ 📜response.py      
┃ ┃ ┃ ┃ ┃   ┣ 📜router.py     
┃ ┃ ┃ ┃ ┃   ┗ 📜schema.py    
┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃ ┃ ┣ 📜crud.py
┃ ┃ ┃ ┃ ┣ 📜response.py
┃ ┃ ┃ ┃ ┣ 📜router.py
┃ ┃ ┃ ┃ ┗ 📜schema.py
┃ ┃ ┃ ┣  📂highlight
┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃ ┃ ┣ 📜crud.py
┃ ┃ ┃ ┃ ┣ 📜response.py
┃ ┃ ┃ ┃ ┣ 📜router.py
┃ ┃ ┃ ┃ ┗ 📜schema.py
┃ ┃ ┃ ┣  📂user
┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃ ┃ ┣ 📜crud.py
┃ ┃ ┃ ┃ ┣ 📜response.py
┃ ┃ ┃ ┃ ┣ 📜router.py
┃ ┃ ┃ ┃ ┗ 📜schema.py
┃ ┃ ┃ ┃ ┣ 📜__init__.py
┃ ┃ ┃ ┗ 📜__init__.py               # v0 정리
┃ ┃ ┗📜__init__.py                  # 라우터 정리
┃ ┣ 📜database.py                   # 데이터베이스 연결 파일
┃ ┣ 📜main.py                       # FastAPI 메인 앱
┃ ┗ 📜model.py                      # Pydantic을 이용한 데이터베이스 모델링
┣ 📜makefile                        # 실행을 쉽게 하기 위한 makefile
┣ 📜poetry.lock                     # poetry 의존성 관리
┣ 📜pyproject.toml                  # poetry 의존성 관리
┣ 📜README.md
```

## API 리스트 및 정리

자세한 사용과 요청/응답 예시는
https://iacapaptextbook2.com/back/v0/docs
에서 확인할 수 있습니다.

## AWS 세팅

### NginX


/etc/nginx/sites-available/iacapaptextbook2.com 에서 확인 가능
```
server {
        listen 80;
        server_name iacapaptextbook2.com;
        return 301 https://$server_name$request_uri;
} # 80번 포트로 오는 HTTP 요청을 443번 포트로 리다이렉트

server {
        listen 443 ssl http2;
        server_name iacapaptextbook2.com; # 도메인

        # SSL 인증서
        ssl_certificate /etc/letsencrypt/live/iacapaptextbook2.com/fullchain.pe>
        ssl_certificate_key /etc/letsencrypt/live/iacapaptextbook2.com/privkey.>

        ssl_protocols TLSv1.2 TLSv1.3;
        ssl_ciphers 'ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:> # 범용성이 높은 암호화 방식
        ssl_prefer_server_ciphers on;

        location / { # 프론트엔드 서버
                proxy_pass http://localhost:3000;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header Host $host;
                proxy_set_header X-Forwarded-Proto $scheme;
        }

        location /back { # 백엔드 서버 
                proxy_pass http://unix:/tmp/webtextbook.sock; # 백엔드 서버 소켓
                proxy_set_header Host $host;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### gunicorn

Unix 소켓을 이용하여 NginX와 통신


/etc/systemd/system/webtextbook.service 에서 확인 가능
```
[Unit] # 서비스 설정
Description= gunicorn daemon 
After=network.target # 네트워크가 준비되면 실행

[Service]
User=ubuntu # 유저 설정
Group=ubuntu # 그룹 설정
WorkingDirectory=/home/ubuntu/webtextbook/backend # 작업 디렉토리
ExecStart=/home/ubuntu/.cache/pypoetry/virtualenvs/webwork1-u0B_3aQC-py3.12/bin> # 실행 명령어
        src.main:app \ # FastAPI 메인 앱
        --workers 2 \ # 워커 수
        --worker-class uvicorn.workers.UvicornWorker \ # 워커 클래스
        --bind unix:/tmp/webtextbook.sock \ # 소켓 바인딩
        --log-config /home/ubuntu/webtextbook/backend/logs/uvicorn_log.ini \ # 로그 설정
[Install]
WantedBy=multi-user.target
```

### 가비아

- 도메인 구매
- 네임서버 설정
    - AWS Route 53에서 네임서버 발급받아 가비아에 설정

- 등록일 : 2024-05-03
- 만료일 : 2025-05-03

### SSL

#### SSL 인증서 발급

certbot을 이용하여 SSL 인증서 발급

```
sudo certbot --nginx -d iacapaptextbook2.com
```

/etc/letsencrypt/live/iacapaptextbook2.com/fullchain.pem
/etc/letsencrypt/live/iacapaptextbook2.com/privkey.pem
에 저장됨.

#### SSL 인증서 갱신

```
sudo certbot renew
```

#### SSL 인증서 확인

```
sudo certbot certificates
```

- 등록일 : 2024-05-08
- 만료일 : 2024-08-06

### 기타 AWS 세팅

- Lightsail 인스턴스 생성
- 고정 IP 할당
- 포트 설정
    - 22, 80, 443, 3000, 4173, 8000번 포트 열려있음
- 도메인 연결
    - 가비아에서 도메인 구매
    - AWS Route 53에서 도메인 연결
- 스토리지
    - Lightsail 자체 스토리지 사용
- 데이터베이스
    - PostgreSQL 사용
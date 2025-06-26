# IACAPAP 웹 사이트

사이트 주소 : https://iacapaptextbook2.com  
API 문서 주소 : https://iacapaptextbook2.com/back/v0/docs

## 기술 스택

### Frontend

- [sveltekit](https://kit.svelte.dev/)
- [ckeditor5](https://ckeditor.com/ckeditor-5/) (에디터 라이브러리)
- [sass](https://sass-lang.com/) (CSS 라이브러리)

## 프로젝트 설치 및 실행 방법 - 로컬 환경

1. 이 저장소를 복제합니다.

```bash
git clone https://github.com/dev-lumanlab/iacapap_textbook_frontend.git ./
```

2. 필요한 패키지를 설치합니다.

```bash
npm install
```

3. 환경변수를 추가합니다.

   1. Root 디렉토리에서 .env 파일 생성
   2. [환경변수](#env) 추가

4. 애플리케이션을 실행합니다.

```bash
npm run dev
```

5. 웹 브라우저에서 [http://localhost:5173](http://localhost:5173)으로 접속하여 애플리케이션을 확인하세요.

## 프로젝트 배포 및 실행 - Amazon Lightsail

### Amazon Lightsail 접속 방법

[https://wikidocs.net/177244](https://wikidocs.net/177244)

### 배포 및 실행

1. Amazon Lightsail 접속 후 프로젝트 폴더로 이동합니다.

```bash
cd webtextbook/frontend/
```

2. git 업데이트 받기

```bash
git pull origin main
```

3. 의존성 설치

```bash
npm install
```

4. 배포하기

```bash
npm run build
```

5. 애플리케이션을 재실행합니다.

```bash
pm2 restart 0
```

## 환경변수

### 파일 위치

```bash
webtextbook/frontend/.env
```

### 파일 수정

```bash
vim .env
```

### <a id="env">환경 변수</a>

```bash
# API server URL
# 외부 API 서버의 주소를 설정합니다.
PUBLIC_API_SERVER=https://iacapaptextbook2.com/back/v0

# client URL
# 클라이언트의 URL을 설정합니다.
PUBLIC_CLIENT_URL=https://iacapaptextbook2.com

# 이메일 발송 ID, PW
# 이메일 발송에 사용할 구글 계정의 아이디와 앱 비밀번호를 설정합니다.
EMAIL_ID=구글 아이디
EMAIL_PASSWORD=구글 앱 비밀번호

# google oauth
# Google OAuth 웹 클라이언트의 ID와 비밀번호를 설정합니다.
PUBLIC_GOOGLE_CLIENT_ID=구글 OAuth 웹 클라이언트 ID
PUBLIC_GOOGLE_CLIENT_PW=구글 OAuth 웹 클라이언트 PW
```

## 폴더 구조

📦src  
┣ 📂lib  
┃ ┣ 📂api  
┃ ┣ 📂components  
┃ ┗ 📂utils  
┣ 📂routes  
┃ ┣ 📂(account)  
┃ ┃ ┣ 📂auth  
┃ ┃ ┣ 📂forgot-password  
┃ ┃ ┣ 📂signin  
┃ ┃ ┣ 📂signup  
┃ ┃ ┣ 📂update-password  
┃ ┃ ┣ 📂verify  
┃ ┣ 📂(home)  
┃ ┃ ┣ 📂highlight  
┃ ┃ ┣ 📂new-update  
┃ ┃ ┣ 📂search  
┃ ┣ 📂admin  
┃ ┃ ┣ 📂(account)  
┃ ┃ ┃ ┣ 📂signin  
┃ ┃ ┗ 📂(home)  
┃ ┃ ┃ ┣ 📂members  
┃ ┃ ┃ ┣ 📂publishing-list  
┃ ┃ ┃ ┣ 📂save-list  
┃ ┃ ┃ ┣ 📂write  
┃ ┣ 📂api  
┃ ┃ ┗ 📂auth  
┃ ┣ 📂docs  
┣ 📂stores  
┗ 📂styles

### 구조 설명

1. **lib**: 프로젝트에 사용되는 라이브러리 코드를 포함하는 폴더입니다.
   - **api**: 웹 애플리케이션에서 사용되는 API 호출에 관련된 코드를 포함합니다.
   - **components**: 재사용 가능한 UI 컴포넌트와 관련된 코드가 여기에 위치합니다.
   - **utils**: 프로젝트 전반에서 사용되는 유틸리티 함수들을 포함합니다.
2. **routes**: 웹 애플리케이션의 라우팅에 관련된 코드를 포함하는 폴더입니다. 라우팅은 사용자 요청에 따라 적절한 페이지나 데이터를 제공하는 역할을 합니다.
   - **(account)**, **(home)**: 레이아웃을 묶기 위한 그룹을 나타냅니다.
   - **api**: 클라이언트에서 서버로 요청을 보내는 API 호출과 관련된 코드가 위치합니다.
3. **stores**: 전역 상태 저장소 코드를 포함하는 폴더입니다.
4. **styles**: CSS 파일이나 CSS 전처리기를 사용하여 스타일을 정의하는 코드를 포함하는 폴더입니다. 웹 애플리케이션의 스타일링과 관련된 모든 파일이 여기에 위치할 수 있습니다.

## 페이지 리스트 및 기능 정리

### 유저

- **/signup** : 회원가입 페이지
  - 이메일 회원가입 및 구글 회원가입을 지원합니다.
  - 회원가입 완료시 로그인("/signin") 페이지로 이동합니다.
- **/signin** : 로그인 페이지
  - 이메일 로그인 및 구글 로그인을 지원합니다.
  - 로그인시 메인("/") 페이지로 이동합니다.
- **/update-password** : 비밀번호 변경 페이지
  - **로그인 사용자**가 비밀번호를 변경할 수 있습니다.
  - 비로그인 사용자는 로그인("/signin") 페이지로 리디렉션됩니다.
  - 비밀번호 변경 완료시 메인("/") 페이지로 이동합니다.
- **/forgot-password** : 비밀번호 변경 페이지
  - **비로그인 사용자**가 이메일 인증을 통해 비밀번호를 변경할 수 있습니다.
  - 비밀번호 변경 완료시 로그인("/signin") 페이지로 이동합니다.
- **/new-update** : 새로운 업데이트 내역 페이지 (무한 스크롤)
  - 새로운 업데이트 내역을 확인할 수 있는 페이지입니다.
  - 해당 문서 클릭시 문서 상세("/docs/{id}") 페이지로 이동합니다.
- **/highlight** : 하이라이트 페이지 (무한 스크롤)
  - 하이라이트된 부분을 확인할 수 있는 페이지입니다.
  - 해당 문서 클릭시 문서 상세("/docs/{id}") 페이지로 이동
- **/search** : 검색 페이지 (무한 스크롤)
  - 원하는 내용을 검색할 수 있는 페이지입니다.
  - 제목 또는 내용이 일치할 경우 검색 결과를 반환합니다.
  - 검색 후 해당 문서 클릭시 문서 상세("/docs/{id}") 페이지로 이동합니다
- **/docs/{id}** : 해당 문서 뷰어 페이지
  - 특정 문서를 보여주는 페이지입니다.

### 관리자 - 유저가 접근할 수 없음

- **/admin/signin** : 로그인 페이지
  - 유저가 해당 페이지에서 로그인 할 경우 메인("/") 페이지로 이동합니다.
  - 관리자가 해당 페이지에서 로그인 할 경우 "/admin/publishing-list" 페이지로 이동합니다.
- **/admin/publishing-list** : 퍼블리싱 리스트 페이지 (페이지 네이션)
  - 퍼블리싱된 문서 리스트를 확인할 수 있는 페이지입니다.
  - **퍼블리싱된 문서는 <span style="color:red;">수정이 불가능하며, 삭제 및 unpublishing</span>만 가능합니다.**
  - "Import to save list" 버튼 클릭시 해당 내용으로 복제된 save 문서를 생성합니다.
- **/admin/save-list** : 저장 리스트 페이지 (페이지 네이션)
  - 저장된 문서 리스트를 확인할 수 있는 페이지입니다.
  - 저장된 문서는 수정, 삭제, 퍼블리싱이 가능합니다.
  - 해당 문서 클릭시 해당 문서 수정 페이지("/admin/write/{id}")로 이동합니다.
- **/admin/write** : 문서 작성 페이지
  - 새로운 문서를 작성하거나 기존 문서를 편집할 수 있는 페이지입니다.
  - "save" 버튼 클릭시 해당 문서 수정 페이지("/admin/write/{id}")로 이동합니다.
  - "publishing" 버튼 클릭시 /publishing-list 페이지로 이동합니다.
  - "preview" 버튼 클릭시 미리보기 모달창이 열립니다.
  - **휴지통 버튼 클릭시 해당 문서의 내용만 삭제됩니다.**

### 마스터 - 관리자가 접근할 수 없음

- **/admin/members** : 유저 관리 페이지 (페이지 네이션)
  - 유저를 관리할 수 있는 페이지입니다.
  - 해당 페이지에서 유저를 검색하고, 권한을 수정하거나 삭제할 수 있습니다.

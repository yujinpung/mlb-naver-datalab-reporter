# 네이버 데이터랩 자동 리포팅 시스템 - 설치 가이드

## 📋 목차
1. [필수 준비사항](#필수-준비사항)
2. [설치 방법](#설치-방법)
3. [슬랙 설정](#슬랙-설정)
4. [테스트 실행](#테스트-실행)
5. [자동 실행 설정](#자동-실행-설정)
6. [문제 해결](#문제-해결)

---

## 📌 필수 준비사항

- Python 3.8 이상
- Chrome 브라우저
- 슬랙 Workspace 관리자 권한 (Webhook 또는 Bot 생성용)

---

## 🔧 설치 방법

### 1. 패키지 설치

```bash
# 필수 패키지 설치
pip install -r requirements.txt

# Playwright 브라우저 설치
playwright install chromium
```

### 2. 환경 변수 설정

`.env.example` 파일을 복사하여 `.env` 파일 생성:

```bash
copy .env.example .env
```

`.env` 파일을 열어서 다음 정보 입력:

```env
# 슬랙 웹훅 URL (필수)
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/YOUR/WEBHOOK/URL

# 슬랙 채널명
SLACK_CHANNEL=#datalab-report

# 슬랙 Bot Token (이미지 업로드용, 선택사항)
SLACK_BOT_TOKEN=xoxb-your-bot-token-here
```

---

## 💬 슬랙 설정

### 방법 1: Webhook (간단, 텍스트만)

1. https://api.slack.com/messaging/webhooks 접속
2. "Create your Slack app" 클릭
3. "From scratch" 선택
4. 앱 이름 입력 (예: Naver Datalab Reporter)
5. Workspace 선택
6. "Incoming Webhooks" 활성화
7. "Add New Webhook to Workspace" 클릭
8. 채널 선택 (예: #datalab-report)
9. Webhook URL 복사하여 `.env` 파일에 붙여넣기

### 방법 2: Bot Token (추천, 이미지 업로드 가능)

1. https://api.slack.com/apps 접속
2. 기존 앱 선택 또는 새로 생성
3. "OAuth & Permissions" 메뉴
4. "Bot Token Scopes"에 다음 권한 추가:
   - `chat:write`
   - `files:write`
5. "Install to Workspace" 클릭
6. "Bot User OAuth Token" 복사
7. `.env` 파일에 `SLACK_BOT_TOKEN` 추가

---

## 🧪 테스트 실행

### 1. 개별 모듈 테스트

```bash
# 스크래핑 테스트
python datalab_scraper.py

# 슬랙 전송 테스트
python slack_sender.py
```

### 2. 전체 실행 테스트

```bash
# 브라우저 보이게 실행 (디버깅용)
# config.py에서 HEADLESS_MODE = False로 설정 후
python main.py

# 백그라운드 실행 (실제 운영)
# config.py에서 HEADLESS_MODE = True로 설정 후
python main.py
```

### 3. 배치 파일 테스트

```bash
run_datalab.bat
```

---

## ⏰ 자동 실행 설정 (Windows Task Scheduler)

### 1. 작업 스케줄러 열기

- `Win + R` → `taskschd.msc` 입력

### 2. 새 작업 만들기

**일반 탭:**
- 이름: `네이버 데이터랩 자동 리포팅`
- 설명: `매일 아침 데이터랩 트렌드 슬랙 전송`
- "사용자의 로그온 여부에 관계없이 실행" 선택
- "가장 높은 수준의 권한으로 실행" 체크

**트리거 탭:**
- "새로 만들기" 클릭
- 작업 시작: `일정에 따라`
- 설정: `매일`
- 시작 시간: `오전 09:00:00`
- "사용" 체크

**동작 탭:**
- "새로 만들기" 클릭
- 작업: `프로그램 시작`
- 프로그램/스크립트: `C:\Users\MADUP\Desktop\projectpung\run_datalab.bat`
  (실제 경로로 수정)
- 시작 위치: `C:\Users\MADUP\Desktop\projectpung`

**조건 탭:**
- "컴퓨터의 AC 전원이 켜져 있는 경우에만 작업 시작" 해제

**설정 탭:**
- "작업이 실패하면 다시 시작 간격" 체크 → `1분`, `3번`

### 3. 저장 및 테스트

- 작업 저장
- 작업 우클릭 → "실행"으로 즉시 테스트

---

## 🔍 문제 해결

### 1. Playwright 설치 오류

```bash
# 관리자 권한으로 실행
playwright install chromium --with-deps
```

### 2. 슬랙 전송 실패

- `.env` 파일의 Webhook URL 확인
- 채널명 정확한지 확인 (`#` 포함)
- 인터넷 연결 확인

### 3. 네이버 데이터랩 캡처 실패

- `config.py`의 `HEADLESS_MODE = False`로 설정
- `python datalab_scraper.py` 실행해서 브라우저 동작 확인
- 네이버 데이터랩 페이지 구조 변경 여부 확인

### 4. 한글 깨짐 문제

- 모든 Python 파일 상단에 `# -*- coding: utf-8 -*-` 확인
- 터미널 인코딩 확인: `chcp 65001` (UTF-8)

### 5. 로그 확인

```bash
# 최근 로그 확인
type logs\datalab_2025-11-15.log
```

---

## 📁 프로젝트 구조

```
projectpung/
├── main.py                 # 메인 실행 스크립트
├── config.py              # 설정 파일
├── datalab_scraper.py     # 스크래핑 모듈
├── slack_sender.py        # 슬랙 전송 모듈
├── requirements.txt       # 패키지 목록
├── .env                   # 환경 변수 (직접 생성)
├── .env.example          # 환경 변수 예시
├── run_datalab.bat       # Windows 배치 파일
├── setup_guide.md        # 이 파일
├── screenshots/          # 스크린샷 저장 폴더
└── logs/                 # 로그 파일 폴더
```

---

## 🎯 커스터마이징

### 키워드 변경

`config.py` 파일에서:

```python
KEYWORDS = ["MLB", "MLB키즈", "모자", "패딩"]
```

### 검색 기간 변경

`config.py` 파일에서:

```python
START_DATE = "2025-01-01"  # 시작일 변경
# 종료일은 자동으로 전일(어제)로 계산됨
```

### 검색 조건 변경 (범위/성별/연령)

현재는 모두 "전체"로 설정되어 있습니다:

```python
DATALAB_SETTINGS = {
    "device": "",   # 전체 (MO/PC)
    "gender": "",   # 전체
    "age": "",      # 전체
}
```

### 실행 시간 변경

Windows Task Scheduler에서 트리거 시간 수정

### 이미지 보관 기간 변경

`config.py` 파일에서:

```python
KEEP_HISTORY_DAYS = 30  # 원하는 일수로 변경
```

---

## 📞 추가 지원

문제가 계속되면 로그 파일(`logs/` 폴더)을 확인하세요.


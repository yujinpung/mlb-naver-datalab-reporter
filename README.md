# 📊 네이버 데이터랩 자동 리포팅 시스템

**완전 자동화된 네이버 검색 트렌드 모니터링 & 슬랙 배포 시스템**

매일 아침, 네이버 데이터랩의 검색 트렌드 그래프를 자동으로 캡처하여  
지정한 슬랙 채널로 전송하는 무인 자동화 솔루션입니다.

---

## ✨ 주요 기능

🤖 **완전 자동화**
- 매일 정해진 시간에 자동 실행
- 사용자 개입 없이 완전 무인 운영

📸 **스마트 캡처**
- Playwright 기반 안정적인 브라우저 자동화
- 헤드리스 모드 지원 (백그라운드 실행)
- 고품질 PNG 스크린샷

💬 **슬랙 통합**
- Webhook 또는 Bot Token 방식 지원
- 이미지 + 메시지 자동 전송
- 에러 발생 시 자동 알림

🔄 **신뢰성**
- 자동 재시도 (최대 3회)
- 상세한 로그 기록
- 오래된 파일 자동 정리

---

## 🎯 현재 검색 조건

### 키워드
```
MLB / MLB키즈 / 모자 / 패딩
```

### 기간
```
시작일: 2025년 1월 1일
종료일: 전일 (어제) - 자동 계산
```

**예시:**
- 오늘이 11월 15일 → `2025-01-01 ~ 2025-11-14`
- 오늘이 11월 16일 → `2025-01-01 ~ 2025-11-15`

### 검색 범위
- **기기**: MO/PC 전체
- **성별**: 전체
- **연령**: 전체

---

## 🚀 빠른 시작

### 1. 설치

```bash
# 패키지 설치
pip install -r requirements.txt

# Playwright 브라우저 설치
playwright install chromium
```

### 2. 슬랙 설정

`.env.example` 파일을 복사하여 `.env` 생성:

```bash
copy .env.example .env
```

`.env` 파일에 슬랙 정보 입력:

```env
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/YOUR/WEBHOOK/URL
SLACK_CHANNEL=#datalab-report
SLACK_BOT_TOKEN=xoxb-your-bot-token  # 선택사항
```

### 3. 테스트 실행

```bash
python main.py
```

### 4. 자동 실행 설정

Windows 작업 스케줄러에 `run_datalab.bat` 등록

자세한 방법은 [`setup_guide.md`](setup_guide.md) 참고

---

## 📁 프로젝트 구조

```
projectpung/
├── main.py                # 메인 실행 스크립트
├── config.py              # 설정 파일 (키워드 여기서 변경)
├── datalab_scraper.py     # 네이버 데이터랩 스크래핑
├── slack_sender.py        # 슬랙 메시지 전송
├── requirements.txt       # 필수 패키지
├── .env                   # 환경 변수 (직접 생성)
├── run_datalab.bat        # Windows 실행 배치
├── setup_guide.md         # 상세 설치 가이드
├── README.md              # 이 파일
├── screenshots/           # 캡처 이미지 저장
└── logs/                  # 실행 로그 저장
```

---

## ⚙️ 커스터마이징

### 키워드 변경

`config.py` 열어서 수정:

```python
KEYWORDS = ["MLB", "MLB키즈", "모자", "패딩"]
```

### 실행 시간 변경

Windows 작업 스케줄러에서 트리거 시간 수정

### 헤드리스 모드 전환

`config.py`에서:

```python
HEADLESS_MODE = True   # 백그라운드 실행
HEADLESS_MODE = False  # 브라우저 보이게 (디버깅용)
```

---

## 🛠 기술 스택

- **Python 3.8+**
- **Playwright** - 브라우저 자동화
- **Slack SDK** - 슬랙 통합
- **Windows Task Scheduler** - 스케줄링

---

## 📊 실행 흐름

```
1. Windows Task Scheduler 트리거 (매일 09:00)
   ↓
2. run_datalab.bat 실행
   ↓
3. main.py 시작
   ↓
4. 네이버 데이터랩 접속 → 키워드 입력 → 그래프 캡처
   ↓
5. PNG 파일로 저장 (screenshots/)
   ↓
6. 슬랙 채널로 이미지 전송
   ↓
7. 30일 이상 된 이미지 자동 삭제
   ↓
8. 로그 저장 (logs/)
```

---

## 🔍 로그 확인

```bash
# 오늘 로그 확인
type logs\datalab_2025-11-15.log

# 스크린샷 확인
dir screenshots\
```

---

## ⚠️ 주의사항

1. **네이버 데이터랩 URL**
   - 현재는 기본 URL 사용
   - 특정 키워드 조합 URL을 직접 설정하면 더 안정적
   
2. **슬랙 이미지 업로드**
   - Webhook만으로는 이미지 업로드 불가
   - Bot Token 필요 (선택사항)

3. **윈도우 PC 켜져 있어야 함**
   - 작업 스케줄러는 PC가 켜져 있어야 실행됨
   - 24시간 서버 또는 클라우드 필요 시 별도 설정

---

## 📖 상세 가이드

- [설치 가이드](setup_guide.md) - 단계별 설치 방법
- [슬랙 설정 가이드](setup_guide.md#슬랙-설정) - Webhook/Bot Token 생성
- [문제 해결](setup_guide.md#문제-해결) - 자주 묻는 질문

---

## 🎁 향후 개선 계획

- [ ] 네이버 데이터랩 공식 API 연동 (더 안정적)
- [ ] 여러 키워드 조합 지원
- [ ] 이메일 리포트 추가
- [ ] 대시보드 웹 페이지
- [ ] Docker 컨테이너화

---

## 📝 라이선스

MIT License

---

## 💡 문의 및 기여

문제가 발생하면 로그 파일을 확인하거나  
`setup_guide.md`의 문제 해결 섹션을 참고하세요.

---

**Made with ❤️ for automatic data monitoring**


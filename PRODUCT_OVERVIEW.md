# 📊 네이버 데이터랩 자동 리포팅 시스템

## 🎯 프로덕트 개요

네이버 데이터랩에서 특정 키워드의 검색 트렌드를 **매일 자동으로 수집**하고, **슬랙으로 알림**을 보내며, **웹 대시보드**에서 시각화하는 자동화 시스템입니다.

---

## 🏗️ 시스템 구성도

```
┌─────────────────────────────────────────────────────────┐
│         GitHub Actions (매일 오전 9시 실행)              │
│  ┌───────────────────────────────────────────────────┐  │
│  │ 1. Python 스크립트 실행                            │  │
│  │    - 네이버 데이터랩 접속 (Playwright)             │  │
│  │    - 8개 키워드 스크린샷 캡처                      │  │
│  │    - screenshots/ 폴더에 저장                     │  │
│  └───────────────────────────────────────────────────┘  │
│                         ↓                                │
│  ┌───────────────────────────────────────────────────┐  │
│  │ 2. Firebase Storage 업로드 (선택사항)              │  │
│  │    - 스크린샷을 Firebase Storage에 업로드         │  │
│  │    - 이미지 URL 생성                               │  │
│  └───────────────────────────────────────────────────┘  │
│                         ↓                                │
│  ┌───────────────────────────────────────────────────┐  │
│  │ 3. 슬랙 전송                                       │  │
│  │    - Webhook 또는 Bot Token 사용                  │  │
│  │    - 8개 키워드 각각 메시지 전송                   │  │
│  │    - 이미지 포함 (Firebase Storage URL)           │  │
│  └───────────────────────────────────────────────────┘  │
│                         ↓                                │
│  ┌───────────────────────────────────────────────────┐  │
│  │ 4. 대시보드 배포                                   │  │
│  │    - GitHub Pages 또는 Firebase Hosting          │  │
│  │    - dashboard.html + screenshots/ 배포           │  │
│  └───────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
                         ↓
        ┌────────────────┴────────────────┐
        ↓                                  ↓
┌─────────────────┐              ┌─────────────────┐
│  Slack 채널     │              │  웹 대시보드    │
│  알림 수신      │              │  시각화         │
└─────────────────┘              └─────────────────┘
```

---

## ⚙️ 주요 기능

### 1. 자동 스크린샷 캡처
- **8개 키워드** 모니터링:
  - MLB
  - MLB키즈
  - 패딩
  - 방한화
  - 키즈책가방
  - 커브러너
  - 카리나MLB
  - 비니

- **검색 기간**: 2025-01-01 ~ 어제(전일)
- **검색 범위**: MO/PC 전체, 성별/연령 전체
- **파일명 형식**: `NaverDatalab_2025-11-15_MLB.png`
- **저장 위치**: `screenshots/` 폴더
- **자동 정리**: 30일 이상 된 파일 자동 삭제

### 2. 슬랙 자동 알림
- **전송 방식 2가지**:
  1. **Webhook 방식** (추천):
     - Firebase Storage 이미지 URL 포함
     - Bot 설치 불필요
  2. **Bot Token 방식**:
     - 이미지 파일 직접 업로드
     - Bot 설치 필요

- **전송 내용**:
  - 키워드별 검색 트렌드 그래프 (이미지)
  - 기간 정보
  - 키워드 정보

- **전송 채널**: `#mlb-naver-datalab-reporter`

### 3. 웹 대시보드
- **반응형 디자인**: 모바일/태블릿/데스크톱 최적화
- **자동 업데이트**: 매일 오전 9시 최신 데이터로 갱신
- **8개 키워드 카드** 레이아웃
- **호스팅 옵션 2가지**:
  1. **GitHub Pages** (무료, 추천)
  2. **Firebase Hosting** (선택사항)

- **접속 URL**: `https://yujinpung.github.io/mlb-naver-datalab-reporter/dashboard.html`

### 4. 자동화 스케줄
- **실행 주기**: 매일 오전 9시 (한국 시간 기준)
- **자동화 플랫폼**: GitHub Actions
- **실행 내용**:
  1. 스크린샷 캡처
  2. Firebase Storage 업로드 (선택)
  3. 슬랙 전송
  4. 대시보드 배포
  5. 오래된 파일 정리

---

## 📁 프로젝트 구조

```
projectpung/
├── .github/
│   └── workflows/
│       └── daily.yml                    # GitHub Actions 워크플로우
│
├── screenshots/                         # 스크린샷 저장 폴더
│   ├── NaverDatalab_2025-11-15_MLB.png
│   ├── NaverDatalab_2025-11-15_MLB키즈.png
│   └── ...
│
├── logs/                                # 실행 로그 폴더
│   └── datalab_2025-11-15.log
│
├── main.py                              # 메인 실행 스크립트
├── datalab_scraper.py                   # 데이터랩 스크레이핑 모듈
├── slack_sender.py                      # 슬랙 전송 모듈
├── firebase_uploader.py                 # Firebase Storage 업로드 모듈
├── config.py                            # 설정 파일
├── requirements.txt                     # Python 패키지 의존성
│
├── dashboard.html                       # 웹 대시보드
├── firebase.json                        # Firebase 설정
├── storage.rules                        # Firebase Storage 규칙
│
├── run_datalab.bat                      # 로컬 실행 스크립트 (Windows)
├── diagnose_slack.py                    # 슬랙 진단 스크립트
├── test_slack_token.py                  # 슬랙 토큰 테스트 스크립트
│
├── README.md                            # 프로젝트 소개
├── GITHUB_SETUP.md                      # GitHub Actions 설정 가이드
├── WEBHOOK_SETUP.md                     # Webhook 설정 가이드
├── WEBHOOK_SETUP_DETAILED.md            # 상세 Webhook 설정 가이드
├── DASHBOARD_SETUP.md                   # 대시보드 설정 가이드
├── FIREBASE_SETUP.md                    # Firebase 설정 가이드
├── SLACK_FIX_GUIDE.md                   # 슬랙 문제 해결 가이드
└── SLACK_TROUBLESHOOTING.md             # 슬랙 트러블슈팅 가이드
```

---

## 🔧 기술 스택

### Backend
- **Python 3.9+**
- **Playwright**: 웹 자동화 및 스크린샷
- **slack-sdk**: 슬랙 API 연동
- **firebase-admin**: Firebase Storage 연동
- **python-dotenv**: 환경변수 관리

### Frontend
- **HTML5 + CSS3**: 반응형 웹 디자인
- **JavaScript (Vanilla)**: 동적 콘텐츠 로딩

### Infrastructure
- **GitHub Actions**: CI/CD 자동화
- **GitHub Pages**: 웹 호스팅 (무료)
- **Firebase Storage**: 이미지 저장 (선택사항)
- **Firebase Hosting**: 웹 호스팅 (선택사항)

### Communication
- **Slack Webhook**: 메시지 전송
- **Slack Bot API**: 이미지 업로드 (선택사항)

---

## 📊 모니터링 키워드

| 키워드 | 데이터랩 URL |
|--------|-------------|
| MLB | https://datalab.naver.com/keyword/trendResult.naver?hashKey=N_5422d72... |
| MLB키즈 | https://datalab.naver.com/keyword/trendResult.naver?hashKey=N_1e264dc... |
| 패딩 | https://datalab.naver.com/keyword/trendResult.naver?hashKey=N_c5184aa... |
| 방한화 | https://datalab.naver.com/keyword/trendResult.naver?hashKey=N_8118629... |
| 키즈책가방 | https://datalab.naver.com/keyword/trendResult.naver?hashKey=N_41a8388... |
| 커브러너 | https://datalab.naver.com/keyword/trendResult.naver?hashKey=N_5bd081e... |
| 카리나MLB | https://datalab.naver.com/keyword/trendResult.naver?hashKey=N_f27df0c... |
| 비니 | https://datalab.naver.com/keyword/trendResult.naver?hashKey=N_7e29205... |

---

## 🚀 배포 환경

### Production (자동화)
- **플랫폼**: GitHub Actions
- **실행 주기**: 매일 오전 9시 (KST)
- **자동 배포**: GitHub Pages
- **URL**: https://yujinpung.github.io/mlb-naver-datalab-reporter/dashboard.html

### Local (개발/테스트)
- **실행 방법**: `python main.py` 또는 `run_datalab.bat`
- **환경변수**: `.env` 파일 사용
- **브라우저**: Playwright Chromium

---

## 🔐 필수 설정

### GitHub Secrets
| Secret | 설명 | 필수 |
|--------|------|------|
| `SLACK_WEBHOOK_URL` | 슬랙 Webhook URL | ✅ 필수 |
| `SLACK_CHANNEL` | 슬랙 채널명 | ⚪ 선택 (기본값: `#datalab-report`) |
| `SLACK_BOT_TOKEN` | 슬랙 Bot Token | ⚪ 선택 (Webhook 대신 사용 가능) |
| `FIREBASE_STORAGE_BUCKET` | Firebase Storage 버킷 이름 | ⚪ 선택 (이미지 URL 생성용) |
| `FIREBASE_CREDENTIALS_JSON` | Firebase 서비스 계정 JSON | ⚪ 선택 (Firebase 사용 시) |
| `FIREBASE_PROJECT_ID` | Firebase 프로젝트 ID | ⚪ 선택 (Firebase 사용 시) |

### 로컬 환경변수 (.env)
```env
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/YOUR/WEBHOOK/URL
SLACK_CHANNEL=#mlb-naver-datalab-reporter
SLACK_BOT_TOKEN=xoxb-your-bot-token (선택)
FIREBASE_STORAGE_BUCKET=your-bucket-name.appspot.com (선택)
FIREBASE_CREDENTIALS_JSON={"type": "service_account", ...} (선택)
```

---

## 📈 실행 흐름

### 자동 실행 (GitHub Actions)
```
1. 매일 오전 9시 (KST) 자동 실행
2. Python 환경 설정 및 패키지 설치
3. Playwright 브라우저 설치
4. main.py 실행
   ├── 네이버 데이터랩 접속 및 스크린샷 캡처
   ├── Firebase Storage 업로드 (선택)
   ├── 슬랙 전송 (8개 키워드)
   └── 오래된 파일 정리
5. dashboard.html + screenshots/ 배포
   ├── GitHub Pages 배포 (기본)
   └── 또는 Firebase Hosting 배포 (선택)
6. 실행 결과 로그 저장
```

### 수동 실행 (로컬)
```bash
# 1. 환경변수 설정 (.env 파일 생성)
# 2. Python 패키지 설치
pip install -r requirements.txt

# 3. Playwright 브라우저 설치
playwright install chromium

# 4. 실행
python main.py
# 또는
run_datalab.bat
```

---

## ✅ 주요 특징

### 1. 완전 자동화
- ✅ 매일 자동 실행 (GitHub Actions)
- ✅ 자동 스크린샷 캡처 (Playwright)
- ✅ 자동 슬랙 전송
- ✅ 자동 대시보드 배포
- ✅ 자동 파일 정리 (30일 보관)

### 2. 유연한 설정
- ✅ Webhook 또는 Bot Token 선택 가능
- ✅ GitHub Pages 또는 Firebase Hosting 선택 가능
- ✅ Firebase Storage 선택적 사용
- ✅ 환경변수로 설정 관리

### 3. 강력한 오류 처리
- ✅ 재시도 로직 (최대 3회)
- ✅ 상세한 로그 기록
- ✅ 오류 발생 시 슬랙 알림
- ✅ 진단 스크립트 제공

### 4. 반응형 대시보드
- ✅ 모바일/태블릿/데스크톱 최적화
- ✅ 8개 키워드 카드 레이아웃
- ✅ 자동 업데이트 (매일 오전 9시)
- ✅ 최종 업데이트 시간 표시

### 5. 무료 운영
- ✅ GitHub Actions (무료)
- ✅ GitHub Pages (무료)
- ✅ Slack Webhook (무료)
- ✅ Firebase Free Tier (선택사항)

---

## 📝 사용 가능한 스크립트

| 스크립트 | 설명 |
|----------|------|
| `main.py` | 메인 실행 스크립트 |
| `run_datalab.bat` | Windows 로컬 실행 스크립트 |
| `diagnose_slack.py` | 슬랙 설정 진단 |
| `test_slack_token.py` | 슬랙 토큰 유효성 테스트 |

---

## 📚 설정 가이드

| 문서 | 설명 |
|------|------|
| [`README.md`](README.md) | 프로젝트 소개 및 빠른 시작 |
| [`GITHUB_SETUP.md`](GITHUB_SETUP.md) | GitHub Actions 설정 가이드 |
| [`WEBHOOK_SETUP.md`](WEBHOOK_SETUP.md) | Webhook 설정 가이드 |
| [`WEBHOOK_SETUP_DETAILED.md`](WEBHOOK_SETUP_DETAILED.md) | 상세 Webhook 설정 가이드 |
| [`DASHBOARD_SETUP.md`](DASHBOARD_SETUP.md) | 대시보드 설정 가이드 |
| [`FIREBASE_SETUP.md`](FIREBASE_SETUP.md) | Firebase 설정 가이드 |
| [`SLACK_FIX_GUIDE.md`](SLACK_FIX_GUIDE.md) | 슬랙 문제 해결 가이드 |
| [`SLACK_TROUBLESHOOTING.md`](SLACK_TROUBLESHOOTING.md) | 슬랙 트러블슈팅 가이드 |

---

## 🎯 사용 사례

### 1. 마케팅 팀
- 매일 아침 슬랙으로 키워드 트렌드 확인
- 대시보드에서 전체 트렌드 한눈에 파악
- 시즌별 검색량 변화 모니터링

### 2. 상품 기획팀
- 인기 키워드 트렌드 분석
- 신제품 출시 타이밍 결정
- 경쟁사 키워드 모니터링

### 3. 경영진
- 대시보드에서 전체 비즈니스 트렌드 확인
- 주요 키워드 검색량 변화 모니터링
- 전략적 의사결정 지원

---

## 🔄 업데이트 주기

- **스크린샷 캡처**: 매일 오전 9시
- **슬랙 알림**: 매일 오전 9시
- **대시보드 갱신**: 매일 오전 9시
- **파일 정리**: 매일 실행 시 (30일 이상 된 파일 삭제)

---

## 💡 추가 기능 아이디어 (향후 확장 가능)

- [ ] 키워드 추가/삭제 자동화 (설정 파일 기반)
- [ ] 주간/월간 리포트 생성
- [ ] 이메일 알림 추가
- [ ] 트렌드 분석 및 예측
- [ ] 키워드별 알림 임계값 설정
- [ ] 데이터베이스 연동 (히스토리 저장)
- [ ] API 엔드포인트 제공

---

## 📞 문제 해결

문제가 발생하면 다음 가이드를 참고하세요:

1. **슬랙 메시지가 안 와요**: [`SLACK_TROUBLESHOOTING.md`](SLACK_TROUBLESHOOTING.md)
2. **GitHub Actions 오류**: [`GITHUB_SETUP.md`](GITHUB_SETUP.md)
3. **대시보드가 안 보여요**: [`DASHBOARD_SETUP.md`](DASHBOARD_SETUP.md)
4. **Firebase 설정 오류**: [`FIREBASE_SETUP.md`](FIREBASE_SETUP.md)

---

## 📊 프로덕트 현황

### ✅ 완료된 기능
- [x] 네이버 데이터랩 스크린샷 캡처
- [x] 8개 키워드 모니터링
- [x] 슬랙 Webhook 연동
- [x] 슬랙 Bot Token 연동 (선택)
- [x] Firebase Storage 연동 (선택)
- [x] GitHub Actions 자동화
- [x] 웹 대시보드 (반응형)
- [x] GitHub Pages 배포
- [x] Firebase Hosting 배포 (선택)
- [x] 자동 파일 정리
- [x] 오류 처리 및 재시도
- [x] 진단 스크립트
- [x] 상세 문서화

### 🎯 현재 상태
- **운영 환경**: GitHub Actions (자동 실행 중)
- **배포 환경**: GitHub Pages 또는 Firebase Hosting
- **알림 채널**: Slack `#mlb-naver-datalab-reporter`
- **실행 주기**: 매일 오전 9시 (KST)
- **모니터링 키워드**: 8개

---

## 🏆 프로덕트 요약

**네이버 데이터랩 자동 리포팅 시스템**은 8개 키워드의 검색 트렌드를 매일 자동으로 수집하고, 슬랙으로 알림을 보내며, 웹 대시보드에서 시각화하는 완전 자동화된 모니터링 솔루션입니다.

- ✅ **완전 자동화**: GitHub Actions로 매일 자동 실행
- ✅ **실시간 알림**: 슬랙으로 매일 아침 트렌드 리포트
- ✅ **시각화**: 반응형 웹 대시보드
- ✅ **무료 운영**: GitHub Actions + GitHub Pages
- ✅ **유연한 설정**: Webhook/Bot Token, GitHub Pages/Firebase 선택 가능
- ✅ **강력한 오류 처리**: 재시도, 로그, 진단 스크립트

---

**마지막 업데이트**: 2025-11-26
**프로젝트 저장소**: https://github.com/yujinpung/mlb-naver-datalab-reporter
**대시보드 URL**: https://yujinpung.github.io/mlb-naver-datalab-reporter/dashboard.html


# 🛠️ 네이버 데이터랩 대시보드 - 설치 가이드

이 가이드는 로컬 환경에서 직접 실행하거나, 본인의 GitHub 저장소에 복제하여 사용하는 방법을 설명합니다.

---

## 📋 목차

1. [온라인 대시보드 사용](#온라인-대시보드-사용) ⭐ 권장
2. [로컬 실행 방법](#로컬-실행-방법)
3. [GitHub에 복제하기](#github에-복제하기)
4. [커스터마이징](#커스터마이징)
5. [문제 해결](#문제-해결)

---

## 🌐 온라인 대시보드 사용

**가장 간단한 방법! 설치 없이 바로 사용하세요.**

### 대시보드 접속
```
https://yujinpung.github.io/mlb-naver-datalab-reporter/
```

### 특징
- ✅ 설치 불필요
- ✅ 매일 오전 9시 자동 업데이트
- ✅ PC/모바일 모두 지원
- ✅ 8개 키워드 트렌드 확인

### 북마크 추가
브라우저 북마크에 추가하여 빠르게 접속하세요!

---

## 💻 로컬 실행 방법

본인의 컴퓨터에서 직접 스크린샷을 캡처하고 싶다면:

### 1. 필수 준비사항

- **Python 3.8 이상**
- **Chrome 브라우저**
- **Git** (선택사항)

### 2. 저장소 다운로드

**방법 A: Git 사용**
```bash
git clone https://github.com/yujinpung/mlb-naver-datalab-reporter.git
cd mlb-naver-datalab-reporter
```

**방법 B: ZIP 다운로드**
1. [저장소 페이지](https://github.com/yujinpung/mlb-naver-datalab-reporter)에서 "Code" 클릭
2. "Download ZIP" 선택
3. 압축 해제

### 3. 패키지 설치

```bash
# 필수 패키지 설치
pip install -r requirements.txt

# Playwright 브라우저 설치
playwright install chromium
```

### 4. 스크린샷 캡처

```bash
python main.py
```

### 5. 결과 확인

- **스크린샷**: `screenshots/` 폴더
- **로그**: `logs/` 폴더
- **대시보드**: `dashboard.html` 파일을 브라우저로 열기

---

## 🔄 GitHub에 복제하기

본인의 GitHub 계정에 복제하여 자동 업데이트 받으려면:

### 1. Fork 하기

1. [저장소 페이지](https://github.com/yujinpung/mlb-naver-datalab-reporter) 접속
2. 우측 상단 **"Fork"** 버튼 클릭
3. 본인 계정으로 저장소 복제

### 2. GitHub Pages 활성화

1. 복제된 저장소의 **Settings** 탭
2. 왼쪽 **Pages** 메뉴
3. **Source**: `gh-pages` 브랜치 선택
4. **Save** 클릭

### 3. GitHub Actions 활성화

1. **Actions** 탭
2. **"I understand my workflows, go ahead and enable them"** 클릭
3. 왼쪽 **"Daily Naver Datalab Report"** 선택
4. **"Run workflow"** 버튼으로 수동 실행

### 4. 대시보드 접속

약 3-5분 후 본인의 대시보드 접속:
```
https://YOUR_USERNAME.github.io/mlb-naver-datalab-reporter/
```

---

## 🎨 커스터마이징

### 키워드 변경

`config.py` 파일에서 키워드 수정:

```python
KEYWORD_URLS = {
    "MLB": "https://datalab.naver.com/keyword/trendResult.naver?hashKey=N_5422d72...",
    "MLB키즈": "https://datalab.naver.com/keyword/trendResult.naver?hashKey=N_1e264dc...",
    # 새 키워드 추가
    "새키워드": "https://datalab.naver.com/keyword/trendResult.naver?hashKey=NEW_HASH",
}
```

**네이버 데이터랩 URL 생성 방법**:
1. [네이버 데이터랩](https://datalab.naver.com/keyword/trendSearch.naver) 접속
2. 원하는 키워드 검색
3. 브라우저 주소창의 URL 복사
4. `config.py`에 추가

### 대시보드 디자인 변경

`dashboard.html` 파일 수정:

```html
<style>
    /* 배경 그라데이션 변경 */
    body {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* 카드 색상 변경 */
    .keyword-card {
        background: white;
        border-radius: 12px;
    }
</style>
```

### 검색 기간 변경

`config.py` 파일에서:

```python
START_DATE = "2025-01-01"  # 원하는 시작일
# 종료일은 자동으로 전일(어제)로 계산됨
```

### 자동 실행 시간 변경

`.github/workflows/daily.yml` 파일에서:

```yaml
schedule:
  - cron: '0 0 * * *'  # UTC 0시 = 한국 오전 9시
```

**시간 변환표**:
| 한국 시간 | UTC 시간 | Cron 표현식 |
|---------|---------|------------|
| 오전 8시 | 23시 (전날) | `'0 23 * * *'` |
| 오전 9시 | 0시 | `'0 0 * * *'` ⭐ (현재) |
| 오전 10시 | 1시 | `'0 1 * * *'` |
| 정오 12시 | 3시 | `'0 3 * * *'` |

### 이미지 보관 기간 변경

`config.py` 파일에서:

```python
KEEP_HISTORY_DAYS = 30  # 원하는 일수로 변경
```

---

## 🔍 문제 해결

### 1. Playwright 설치 오류

**증상**: `playwright: command not found`

**해결**:
```bash
# 관리자 권한으로 재설치
playwright install chromium --with-deps
```

### 2. 스크린샷이 비어있음

**증상**: 이미지는 생성되지만 내용이 비어있음

**해결**:
1. `config.py`에서 `HEADLESS_MODE = False`로 변경
2. `python main.py` 실행
3. 브라우저 동작 확인
4. 네이버 데이터랩 로딩 시간 확인

### 3. GitHub Actions 실행 실패

**증상**: Actions 탭에서 빨간색 X 표시

**해결**:
1. 실패한 워크플로우 클릭
2. 로그 확인
3. 가능한 원인:
   - Playwright 브라우저 설치 실패
   - 네이버 데이터랩 URL 변경
   - 타임아웃 (대기 시간 부족)

### 4. 대시보드 이미지 안 보임

**증상**: 대시보드는 열리지만 이미지가 "불러올 수 없습니다"

**해결**:
1. **GitHub Actions 확인**: [Actions 탭](https://github.com/yujinpung/mlb-naver-datalab-reporter/actions)에서 최근 실행 성공 확인
2. **브라우저 캐시 삭제**: `Ctrl + F5` (Windows) 또는 `Cmd + Shift + R` (Mac)
3. **GitHub Pages 확인**: Settings → Pages에서 `gh-pages` 브랜치 활성화 확인
4. **파일 확인**: 저장소의 `screenshots/` 폴더에 이미지 파일이 있는지 확인

### 5. Python 버전 오류

**증상**: `SyntaxError` 또는 호환성 오류

**해결**:
```bash
# Python 버전 확인
python --version

# Python 3.8 이상 필요
# Python 3.11 권장
```

### 6. 한글 깨짐 (로컬 실행)

**증상**: 로그나 파일명에서 한글이 깨짐

**해결**:
- Windows: `chcp 65001` (UTF-8 설정)
- 모든 Python 파일은 UTF-8 인코딩 사용

### 7. Git push 실패

**증상**: `permission denied` 또는 인증 오류

**해결**:
```bash
# Personal Access Token 생성
# GitHub → Settings → Developer settings → Personal access tokens
# "repo" 권한 선택

# 원격 저장소 URL에 토큰 포함
git remote set-url origin https://YOUR_TOKEN@github.com/YOUR_USERNAME/mlb-naver-datalab-reporter.git
```

---

## 📊 프로젝트 구조

```
mlb-naver-datalab-reporter/
├── .github/
│   └── workflows/
│       └── daily.yml           # GitHub Actions 워크플로우
├── screenshots/                # 캡처된 이미지 저장
│   └── NaverDatalab_2025-11-25_MLB.png
├── logs/                       # 실행 로그
│   └── datalab_2025-11-26.log
├── main.py                     # 메인 실행 스크립트
├── config.py                   # 설정 파일 ⚙️
├── datalab_scraper.py          # 스크래핑 로직
├── dashboard.html              # 대시보드 UI 🎨
├── requirements.txt            # Python 패키지
├── README.md                   # 프로젝트 소개
├── setup_guide.md              # 이 파일
├── .gitignore                  # Git 제외 파일 목록
└── SECURITY_AUDIT_REPORT.md    # 보안 점검 리포트
```

**중요 파일**:
- ⚙️ **config.py**: 키워드, 날짜, 설정 변경
- 🎨 **dashboard.html**: 디자인, 레이아웃 변경
- 📅 **.github/workflows/daily.yml**: 스케줄, 자동화 설정

---

## 🚀 배포 흐름

### GitHub Actions 워크플로우

```
1. 스케줄 트리거 (매일 UTC 0시)
   ↓
2. Ubuntu 환경 준비
   ↓
3. Python 3.11 설치
   ↓
4. 패키지 및 Playwright 설치
   ↓
5. main.py 실행 (스크린샷 캡처)
   ↓
6. 스크린샷 Git에 커밋
   ↓
7. GitHub Pages 배포 디렉토리 준비
   ↓
8. gh-pages 브랜치에 배포
   ↓
9. 대시보드 자동 업데이트 완료! ✅
```

---

## 💡 추가 팁

### 로컬 대시보드 사용

로컬에서 캡처한 스크린샷을 대시보드로 보려면:
1. `python main.py` 실행
2. `dashboard.html` 파일을 브라우저로 열기
3. 로컬 스크린샷이 자동으로 로드됨

### 수동 실행 (GitHub Actions)

자동 스케줄을 기다리지 않고 즉시 실행:
1. [Actions 탭](https://github.com/yujinpung/mlb-naver-datalab-reporter/actions) 접속
2. **"Daily Naver Datalab Report"** 선택
3. **"Run workflow"** 버튼 클릭
4. 약 3-5분 후 대시보드 확인

### 모바일 접근

대시보드는 반응형으로 제작되어 모바일에서도 최적화되어 있습니다:
- 📱 스마트폰: 세로 1열 레이아웃
- 📲 태블릿: 2열 레이아웃
- 💻 PC: 3-4열 레이아웃

### 여러 프로젝트 관리

여러 세트의 키워드를 모니터링하려면:
1. 저장소를 여러 개 Fork
2. 각각 다른 키워드 설정
3. 각각의 대시보드 URL 생성

---

## 📞 추가 지원

### 커뮤니티

- **Issues**: 버그 리포트, 기능 요청
- **Discussions**: 질문, 아이디어 공유

### 참고 문서

- [GitHub Actions 문서](https://docs.github.com/en/actions)
- [GitHub Pages 가이드](https://docs.github.com/en/pages)
- [Playwright 문서](https://playwright.dev/python/)
- [네이버 데이터랩](https://datalab.naver.com)

---

## ✅ 설치 체크리스트

### 온라인 대시보드 사용 (권장)
- [ ] 대시보드 URL 접속 확인
- [ ] 북마크 추가
- [ ] 모바일에서도 접속 확인

### 로컬 실행
- [ ] Python 3.8+ 설치
- [ ] 저장소 다운로드/클론
- [ ] 패키지 설치 (`pip install -r requirements.txt`)
- [ ] Playwright 설치 (`playwright install chromium`)
- [ ] 테스트 실행 (`python main.py`)
- [ ] 스크린샷 확인 (`screenshots/` 폴더)

### GitHub 복제 (자동화)
- [ ] Fork 완료
- [ ] GitHub Pages 활성화
- [ ] GitHub Actions 활성화
- [ ] 수동 실행 테스트
- [ ] 대시보드 URL 확인
- [ ] 자동 스케줄 확인 (다음날 오전 9시)

---

**축하합니다! 설치가 완료되었습니다! 🎉**

대시보드를 통해 매일 업데이트되는 트렌드를 확인하세요!


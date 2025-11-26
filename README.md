# 📊 네이버 데이터랩 모니터링 대시보드

**매일 자동 업데이트되는 네이버 검색 트렌드 모니터링 대시보드**

[![GitHub Pages](https://img.shields.io/badge/Dashboard-Live-brightgreen?style=for-the-badge&logo=github)](https://yujinpung.github.io/mlb-naver-datalab-reporter/)
[![Auto Update](https://img.shields.io/badge/Update-Daily%209AM-blue?style=for-the-badge&logo=github-actions)](https://github.com/yujinpung/mlb-naver-datalab-reporter/actions)

**🌐 대시보드 바로가기**: https://yujinpung.github.io/mlb-naver-datalab-reporter/

---

## ✨ 주요 기능

### 🤖 완전 자동화
- **매일 오전 9시** 자동 실행 (GitHub Actions)
- **무인 운영** - 서버 없이 클라우드에서 자동 실행
- **자동 배포** - GitHub Pages에 즉시 반영

### 📊 실시간 대시보드
- **반응형 디자인** - PC, 태블릿, 모바일 최적화
- **8개 키워드** 동시 모니터링
- **깔끔한 UI** - 한눈에 트렌드 파악

### 📸 스마트 캡처
- **Playwright 기반** 안정적인 브라우저 자동화
- **고품질 PNG** 스크린샷
- **자동 히스토리 관리** (30일)

### 🔒 보안
- **민감 정보 보호** - 환경변수 관리
- **GitHub Secrets** 사용
- **Public 저장소** 안전성 인증 완료

---

## 🎯 모니터링 키워드

현재 다음 8개 키워드를 추적하고 있습니다:

```
✅ MLB          ✅ MLB키즈
✅ 패딩         ✅ 방한화
✅ 키즈책가방   ✅ 커브러너
✅ 카리나MLB    ✅ 비니
```

**검색 기간**: 2025-01-01 ~ 전일(어제)  
**검색 범위**: MO/PC 전체, 성별/연령 전체

---

## 🖥️ 대시보드 미리보기

대시보드에서 확인할 수 있는 정보:
- 📈 키워드별 검색 트렌드 그래프
- 📅 데이터 수집 날짜
- 🔄 마지막 업데이트 시간
- 🖱️ 이미지 클릭 시 확대 보기

**매일 오전 9시 자동 업데이트!**

---

## 🚀 로컬 실행 방법

### 1. 저장소 클론

```bash
git clone https://github.com/yujinpung/mlb-naver-datalab-reporter.git
cd mlb-naver-datalab-reporter
```

### 2. 패키지 설치

```bash
pip install -r requirements.txt
playwright install chromium
```

### 3. 스크린샷 캡처

```bash
python main.py
```

캡처된 이미지는 `screenshots/` 폴더에 저장됩니다.

### 4. 대시보드 확인

`dashboard.html`을 브라우저로 열어 로컬에서 확인할 수 있습니다.

---

## ⚙️ 커스터마이징

### 키워드 변경

`config.py` 파일에서 원하는 키워드 추가/변경:

```python
KEYWORD_URLS = {
    "MLB": "https://datalab.naver.com/keyword/trendResult.naver?hashKey=...",
    "새키워드": "새로운_URL",
}
```

### 대시보드 디자인 변경

`dashboard.html` 파일의 CSS 섹션 수정:

```html
<style>
    /* 여기서 색상, 레이아웃 등 커스터마이징 */
</style>
```

### 검색 기간 변경

`config.py` 파일에서:

```python
START_DATE = "2025-01-01"  # 원하는 시작일로 변경
# 종료일은 자동으로 전일(어제)로 계산됨
```

---

## 🏗️ 프로젝트 구조

```
mlb-naver-datalab-reporter/
├── .github/
│   └── workflows/
│       └── daily.yml           # GitHub Actions 워크플로우
├── screenshots/                # 스크린샷 저장 (자동 생성)
├── logs/                       # 실행 로그 (자동 생성)
├── main.py                     # 메인 실행 스크립트
├── config.py                   # 설정 파일
├── datalab_scraper.py          # 스크래핑 모듈
├── dashboard.html              # 대시보드 (GitHub Pages)
├── requirements.txt            # Python 패키지 목록
└── README.md                   # 이 파일
```

---

## 🔧 기술 스택

### Backend (자동화)
- **Python 3.11** - 메인 언어
- **Playwright** - 브라우저 자동화
- **python-dotenv** - 환경변수 관리

### Frontend (대시보드)
- **HTML5/CSS3** - 대시보드 UI
- **JavaScript** - 동적 콘텐츠 로딩
- **Responsive Design** - 모바일 최적화

### CI/CD
- **GitHub Actions** - 자동 실행 (매일 UTC 0시)
- **GitHub Pages** - 대시보드 호스팅

---

## 📊 동작 원리

```
1. GitHub Actions 트리거 (매일 UTC 0시 = 한국 오전 9시)
   ↓
2. Python 스크립트 실행
   ↓
3. Playwright로 네이버 데이터랩 접속
   ↓
4. 키워드별 트렌드 그래프 캡처 (8개)
   ↓
5. PNG 파일로 저장 (screenshots/)
   ↓
6. Git에 커밋 및 푸시
   ↓
7. GitHub Pages에 자동 배포
   ↓
8. 대시보드 업데이트 완료! ✅
```

---

## 🔍 GitHub Actions 워크플로우

`.github/workflows/daily.yml`에서 자동화 설정:

- **스케줄**: 매일 UTC 0시 (한국 오전 9시)
- **수동 실행**: "Run workflow" 버튼으로 즉시 실행 가능
- **자동 배포**: 성공 시 GitHub Pages에 자동 배포

**워크플로우 확인**: [Actions 탭](https://github.com/yujinpung/mlb-naver-datalab-reporter/actions)

---

## 📈 사용 예시

### 대시보드 접속
```
https://yujinpung.github.io/mlb-naver-datalab-reporter/
```

### 특정 날짜 스크린샷 확인
```
screenshots/NaverDatalab_2025-11-25_MLB.png
screenshots/NaverDatalab_2025-11-25_패딩.png
```

### 로그 확인
```
logs/datalab_2025-11-26.log
```

---

## 🛠️ 문제 해결

### 대시보드에서 이미지가 안 보일 때

1. **GitHub Actions 실행 확인**
   - [Actions 탭](https://github.com/yujinpung/mlb-naver-datalab-reporter/actions)에서 최근 실행 확인
   - 초록색 체크마크(✅) 확인

2. **브라우저 캐시 삭제**
   - `Ctrl + F5` (Windows) 또는 `Cmd + Shift + R` (Mac)

3. **GitHub Pages 설정 확인**
   - Settings → Pages → Source: `gh-pages` 브랜치 확인

### 로컬 실행 오류

```bash
# Playwright 재설치
playwright install chromium --with-deps

# 패키지 업데이트
pip install --upgrade -r requirements.txt
```

---

## 📝 업데이트 이력

- **2025-11-26**: Public 저장소 전환, 보안 강화, 문서 개선
- **2025-11-26**: GitHub Pages 대시보드 추가
- **2025-11-15**: 8개 키워드로 확장
- **2025-11-14**: 초기 버전 배포

---

## 📄 관련 문서

- [보안 점검 리포트](SECURITY_AUDIT_REPORT.md) - 보안 감사 결과
- [최종 보안 확인](FINAL_SECURITY_CHECK.md) - Public 전환 후 점검
- [GitHub Actions 설정](GITHUB_SETUP.md) - 워크플로우 가이드
- [대시보드 설정](DASHBOARD_SETUP.md) - GitHub Pages 설정

---

## 🎁 향후 개선 계획

- [ ] 키워드별 알림 설정 (급등/급락 감지)
- [ ] 주간/월간 리포트 생성
- [ ] 차트 라이브러리 추가 (인터랙티브 그래프)
- [ ] 키워드 비교 기능
- [ ] 데이터 다운로드 기능 (CSV/Excel)

---

## 🤝 기여하기

이 프로젝트에 기여하고 싶으신가요?

1. **Fork** 저장소
2. **Feature Branch** 생성 (`git checkout -b feature/AmazingFeature`)
3. **Commit** 변경사항 (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to Branch (`git push origin feature/AmazingFeature`)
5. **Pull Request** 생성

---

## 📜 라이선스

이 프로젝트는 MIT 라이선스 하에 있습니다.

---

## 💡 문의 및 지원

- **Issues**: [GitHub Issues](https://github.com/yujinpung/mlb-naver-datalab-reporter/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yujinpung/mlb-naver-datalab-reporter/discussions)

---

## ⭐ Star History

이 프로젝트가 도움이 되셨다면 ⭐ Star를 눌러주세요!

---

**Made with ❤️ for automated trend monitoring**


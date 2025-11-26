# 📊 대시보드 자동 업데이트 설정 가이드

네이버 데이터랩 모니터링 대시보드가 매일 오전 9시에 자동으로 업데이트되도록 설정하는 방법입니다.

---

## 🎯 작동 원리

### 자동 업데이트 프로세스

```
매일 오전 9시 (한국 시간)
    ↓
GitHub Actions 실행
    ↓
1. 네이버 데이터랩 스크린샷 생성 (8개 키워드)
    ↓
2. 슬랙으로 리포트 전송
    ↓
3. 스크린샷을 저장소에 커밋
    ↓
4. GitHub Pages에 배포
    ↓
대시보드 자동 업데이트 완료! ✨
```

---

## 📋 설정 단계

### 1️⃣ GitHub Pages 활성화

**1-1. 저장소 Settings 접속**
```
https://github.com/yujinpung/mlb-naver-datalab-reporter/settings/pages
```

**1-2. Pages 설정**
- **Source**: `GitHub Actions` 선택
- 자동으로 저장됨

**1-3. 대시보드 접속 주소 확인**
```
https://yujinpung.github.io/mlb-naver-datalab-reporter/dashboard.html
```

> ⚠️ **참고**: 첫 배포 후 몇 분 정도 소요될 수 있습니다.

---

### 2️⃣ GitHub Actions 권한 확인

**2-1. Settings → Actions → General 접속**
```
https://github.com/yujinpung/mlb-naver-datalab-reporter/settings/actions
```

**2-2. Workflow permissions 확인**
- **"Read and write permissions"** 선택되어 있는지 확인
- 또는 **"Read repository contents and packages permissions"** + **"Allow GitHub Actions to create and approve pull requests"** 체크

---

### 3️⃣ 코드 업로드

변경된 파일들을 GitHub에 업로드합니다:

```powershell
cd C:\Users\MADUP\Desktop\projectpung

# Git PATH 추가 (필요시)
$env:Path += ";C:\Program Files\Git\bin"

# 변경사항 확인
git status

# 파일 추가
git add dashboard.html
git add .github/workflows/daily.yml

# 커밋
git commit -m "Add dashboard auto-update feature"

# 업로드
git push
```

---

## ✅ 확인 방법

### 1. GitHub Actions 실행 확인

**Actions 탭 접속**:
```
https://github.com/yujinpung/mlb-naver-datalab-reporter/actions
```

**확인 사항**:
- ✅ "Daily Naver Datalab Report" workflow 실행
- ✅ 모든 단계 성공 (초록색 체크)
- ✅ "Deploy to GitHub Pages" 단계 성공

---

### 2. 대시보드 접속 확인

**대시보드 URL**:
```
https://yujinpung.github.io/mlb-naver-datalab-reporter/dashboard.html
```

**확인 사항**:
- ✅ 8개 키워드 카드 표시
- ✅ 스크린샷 이미지 로드
- ✅ 날짜 정보 표시
- ✅ 모바일 반응형 작동

---

### 3. 자동 업데이트 확인

**내일 오전 9시 이후**:
1. 대시보드 새로고침 (F5)
2. 날짜가 자동으로 업데이트되었는지 확인
3. 새로운 스크린샷이 표시되는지 확인

---

## 🔧 작동 방식 상세

### 대시보드 날짜 자동 계산

대시보드는 **JavaScript**로 자동으로 날짜를 계산합니다:

```javascript
// 어제 날짜 계산
function getYesterdayDateString() {
    const yesterday = new Date();
    yesterday.setDate(yesterday.getDate() - 1);
    return `${year}-${month}-${day}`;
}

// 파일명 자동 생성
function generateFilename(keywordName) {
    const dateStr = getYesterdayDateString();
    return `NaverDatalab_${dateStr}_${keywordName}.png`;
}
```

**예시**:
- 오늘이 11월 16일 → 어제는 11월 15일
- 파일명: `NaverDatalab_2025-11-15_MLB.png`

---

### GitHub Actions 업데이트 프로세스

**매일 오전 9시 실행**:

1. **스크린샷 생성**
   ```bash
   python main.py
   # → screenshots/NaverDatalab_2025-11-15_*.png 생성
   ```

2. **저장소에 커밋**
   ```bash
   git add screenshots/*.png
   git add dashboard.html
   git commit -m "Update dashboard: 2025-11-16"
   git push
   ```

3. **GitHub Pages 배포**
   - `peaceiris/actions-gh-pages` 액션 사용
   - 대시보드와 스크린샷을 GitHub Pages에 배포
   - 몇 분 후 자동으로 반영됨

---

## 📱 모바일 접속

대시보드는 **완전 반응형**으로 설계되었습니다:

### 접속 방법
```
모바일 브라우저에서:
https://yujinpung.github.io/mlb-naver-datalab-reporter/dashboard.html
```

### 화면 크기별 레이아웃
- **모바일** (768px 이하): 1열
- **태블릿** (769px~1024px): 2열
- **데스크톱** (1025px~1399px): 3열
- **대형 화면** (1400px 이상): 4열

---

## 🛠️ 문제 해결

### ❌ 대시보드가 표시되지 않음

**원인**: GitHub Pages 미활성화

**해결 방법**:
1. Settings → Pages 접속
2. Source를 "GitHub Actions"로 설정
3. 저장 후 몇 분 대기

---

### ❌ 이미지가 로드되지 않음

**원인**: 스크린샷 파일 경로 문제

**해결 방법**:
1. GitHub 저장소에서 `screenshots/` 폴더 확인
2. 파일명이 올바른지 확인 (날짜 형식)
3. 브라우저 개발자 도구 (F12) → Console에서 에러 확인

---

### ❌ 자동 업데이트가 안 됨

**원인**: GitHub Actions 실행 실패

**해결 방법**:
1. Actions 탭에서 실행 이력 확인
2. 실패한 단계의 로그 확인
3. Secrets 설정 확인 (모든 URL 등록되었는지)

---

### ❌ GitHub Pages 배포 실패

**원인**: 권한 문제

**해결 방법**:
1. Settings → Actions → General
2. "Read and write permissions" 확인
3. `.github/workflows/daily.yml`의 `permissions` 섹션 확인

---

## 📊 업데이트 주기

### 현재 설정
- **자동 실행**: 매일 오전 9시 (한국 시간)
- **업데이트 내용**: 8개 키워드 스크린샷
- **배포 시간**: 실행 후 약 3-5분

### 변경 방법

`.github/workflows/daily.yml` 파일 수정:

```yaml
schedule:
  - cron: '0 0 * * *'  # UTC 0시 = 한국 오전 9시
```

**시간 변환표**:
- 오전 8시: `'0 23 * * *'` (UTC 23시 전날)
- 오전 9시: `'0 0 * * *'` ⭐ (현재)
- 오전 10시: `'0 1 * * *'`

---

## 🎯 체크리스트

설정 완료 전 확인:

- [ ] GitHub Pages 활성화 (Settings → Pages)
- [ ] Workflow permissions 설정 (Read and write)
- [ ] dashboard.html 파일 업로드
- [ ] .github/workflows/daily.yml 파일 업로드
- [ ] 첫 번째 Actions 실행 테스트
- [ ] 대시보드 접속 확인
- [ ] 모바일 반응형 확인

---

## 💡 추가 기능 (향후)

### 가능한 개선사항:
- [ ] 이미지 확대 보기 (모달)
- [ ] 키워드 필터링
- [ ] 날짜별 히스토리 보기
- [ ] 차트/그래프 통합
- [ ] 다크 모드
- [ ] 알림 설정

---

## 🔗 관련 링크

- **대시보드**: https://yujinpung.github.io/mlb-naver-datalab-reporter/dashboard.html
- **GitHub 저장소**: https://github.com/yujinpung/mlb-naver-datalab-reporter
- **Actions**: https://github.com/yujinpung/mlb-naver-datalab-reporter/actions
- **Pages 설정**: https://github.com/yujinpung/mlb-naver-datalab-reporter/settings/pages

---

## ✅ 완료!

축하합니다! 이제 매일 오전 9시에 대시보드가 자동으로 업데이트됩니다! 🎉

**다음 단계**:
- 첫 번째 자동 실행까지 기다리기 (내일 오전 9시)
- 또는 "Run workflow" 버튼으로 즉시 테스트하기

---

**문제가 발생하면 Actions 로그를 확인하거나 이 가이드의 문제 해결 섹션을 참고하세요!**


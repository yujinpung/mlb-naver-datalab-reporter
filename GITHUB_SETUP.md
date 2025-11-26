# 🚀 GitHub Actions 자동화 설정 가이드

네이버 데이터랩 모니터링 대시보드를 GitHub Actions와 GitHub Pages로 자동화하는 방법입니다.

---

## 📋 목차

1. [GitHub 저장소 생성](#1-github-저장소-생성)
2. [GitHub Pages 활성화](#2-github-pages-활성화)
3. [코드 업로드](#3-코드-업로드)
4. [실행 시간 설정](#4-실행-시간-설정)
5. [테스트 실행](#5-테스트-실행)
6. [문제 해결](#6-문제-해결)

---

## 1️⃣ GitHub 저장소 생성

### 1-1. 새 저장소 만들기

1. **GitHub 접속**: https://github.com
2. **로그인** 후 우측 상단 **"+"** 클릭 → **"New repository"** 선택
3. **저장소 설정**:
   - **Repository name**: `mlb-naver-datalab-reporter` (또는 원하는 이름)
   - **Description**: `네이버 데이터랩 모니터링 대시보드`
   - **Visibility**: 
     - ⭐ **Public** (필수) - GitHub Pages는 무료 계정에서 Public 저장소만 지원
   - **Initialize this repository**:
     - ✅ **체크 해제** (로컬 코드를 업로드할 예정)
4. **"Create repository"** 클릭

### 1-2. 저장소 주소 복사

생성 완료 후 표시되는 주소 복사:
```
https://github.com/YOUR_USERNAME/mlb-naver-datalab-reporter.git
```

---

## 2️⃣ GitHub Pages 활성화

### 2-1. Pages 설정 페이지 열기

1. 생성한 저장소 페이지에서 **"Settings"** 탭 클릭
2. 왼쪽 사이드바에서 **"Pages"** 클릭

### 2-2. Pages 활성화

1. **Source** 섹션에서:
   - **Branch**: `gh-pages` 선택
   - **Folder**: `/ (root)` 선택
2. **"Save"** 버튼 클릭

### 2-3. 접속 URL 확인

설정 완료 후 표시되는 URL 확인:
```
https://YOUR_USERNAME.github.io/mlb-naver-datalab-reporter/
```

⚠️ **주의**: 첫 배포 전까지는 404 에러가 발생합니다. GitHub Actions 실행 후 접속하세요

---

## 3️⃣ 코드 업로드

### 3-1. Git 초기화 및 업로드

PowerShell을 열고 프로젝트 폴더로 이동:

```powershell
# 프로젝트 폴더로 이동
cd C:\Users\MADUP\Desktop\projectpung

# Git 초기화
git init

# 모든 파일 추가 (.gitignore에 명시된 파일은 제외됨)
git add .

# 첫 커밋
git commit -m "Initial commit: Naver Datalab Dashboard"

# 원격 저장소 연결 (YOUR_USERNAME을 실제 GitHub 아이디로 변경)
git remote add origin https://github.com/YOUR_USERNAME/mlb-naver-datalab-reporter.git

# main 브랜치로 변경 (GitHub 기본 브랜치명)
git branch -M main

# 업로드
git push -u origin main
```

### 3-2. GitHub 로그인

업로드 중 GitHub 로그인 창이 뜨면:
- **GitHub 아이디와 비밀번호** 입력
- 또는 **Personal Access Token** 입력

### 3-3. Personal Access Token 생성 (필요시)

비밀번호 인증이 안 되면 Token 생성:

1. **GitHub 설정**: https://github.com/settings/tokens
2. **"Generate new token"** → **"Generate new token (classic)"**
3. **Note**: `Datalab Dashboard Token`
4. **Expiration**: `No expiration` (또는 원하는 기간)
5. **Select scopes**:
   - ✅ `repo` (전체 체크)
   - ✅ `workflow`
6. **"Generate token"** 클릭
7. **생성된 토큰 복사** (한 번만 보임!)
8. `git push` 시 비밀번호 입력란에 **토큰 붙여넣기**

### 3-4. 업로드 확인

GitHub 저장소 페이지를 새로고침하여 파일들이 업로드되었는지 확인:
```
✅ .github/workflows/daily.yml
✅ config.py
✅ datalab_scraper.py
✅ main.py
✅ dashboard.html
✅ requirements.txt
✅ README.md
✅ .gitignore
```

❌ **업로드되면 안 되는 파일** (.gitignore로 차단됨):
```
❌ .env (환경변수 파일)
❌ logs/ (로컬 로그)
❌ __pycache__/
```

⚠️ **screenshots 폴더는 GitHub Actions가 자동으로 추가합니다**

---

## 4️⃣ 실행 시간 설정

### 4-1. 기본 설정

현재 설정된 실행 시간:
- **매일 한국 시간 오전 9시 (UTC 0시)**

### 4-2. 실행 시간 변경 방법

다른 시간으로 변경하려면 `.github/workflows/daily.yml` 파일 수정:

```yaml
schedule:
  - cron: '0 0 * * *'  # UTC 0시 = 한국 오전 9시
```

**시간 변환표** (한국 시간 → UTC):

| 한국 시간 | UTC 시간 | Cron 표현식 |
|---------|---------|------------|
| 오전 8시 | 23시 (전날) | `'0 23 * * *'` |
| 오전 9시 | 0시 | `'0 0 * * *'` ⭐ (현재) |
| 오전 10시 | 1시 | `'0 1 * * *'` |
| 오전 11시 | 2시 | `'0 2 * * *'` |
| 정오 12시 | 3시 | `'0 3 * * *'` |

**변경 방법**:
1. `.github/workflows/daily.yml` 파일 열기
2. `cron:` 라인 수정
3. Git 커밋 및 푸시:
   ```powershell
   git add .github/workflows/daily.yml
   git commit -m "Change execution time"
   git push
   ```

---

## 5️⃣ 테스트 실행

### 5-1. 수동 실행 (즉시 테스트)

1. **GitHub 저장소 페이지** → **"Actions"** 탭 클릭
2. 왼쪽 사이드바에서 **"Daily Naver Datalab Report"** 클릭
3. 우측 **"Run workflow"** 버튼 클릭
4. **"Run workflow"** 확인 버튼 클릭

### 5-2. 실행 상태 확인

- **진행 중**: 🟡 노란색 점
- **성공**: 🟢 초록색 체크
- **실패**: 🔴 빨간색 X

### 5-3. 로그 확인

1. 실행 중인 workflow 클릭
2. **"datalab-report"** job 클릭
3. 각 단계별 로그 확인 가능

### 5-4. 대시보드 확인

실행 성공 시 (약 3-5분 소요) 대시보드 접속:
```
https://YOUR_USERNAME.github.io/mlb-naver-datalab-reporter/
```

**포함된 키워드** (8개):
- MLB
- MLB키즈
- 패딩
- 방한화
- 키즈책가방
- 커브러너
- 카리나MLB
- 비니

### 5-5. 스크린샷/로그 다운로드 (선택사항)

Actions 페이지 하단에서 Artifacts 다운로드 가능:
- **screenshots-[번호]**: 캡처된 이미지 (7일간 보관)
- **logs-[번호]**: 실행 로그 (7일간 보관)

---

## 6️⃣ 문제 해결

### ❌ "Error: Process completed with exit code 1"

**원인**: Python 스크립트 실행 중 오류

**해결 방법**:
1. Actions 로그에서 상세 에러 메시지 확인
2. 가능한 원인:
   - 네이버 데이터랩 URL 변경
   - Playwright 브라우저 설치 오류
   - 의존성 패키지 버전 문제

### ❌ 대시보드에서 이미지가 안 보임

**원인**: 이미지 파일 경로 또는 배포 문제

**해결 방법**:
1. **Screenshots 폴더 확인**:
   - GitHub 저장소의 `screenshots/` 폴더에 이미지가 있는지 확인
   - `main` 브랜치에 커밋되었는지 확인
2. **GitHub Pages 배포 확인**:
   - Actions 탭에서 "Deploy to GitHub Pages" 단계 성공 여부 확인
   - Settings → Pages에서 `gh-pages` 브랜치 활성화 확인
3. **브라우저 캐시 삭제**:
   - `Ctrl + F5` (Windows) 또는 `Cmd + Shift + R` (Mac)으로 강력 새로고침

### ❌ 스크린샷이 비어있음

**원인**: 네이버 데이터랩 로딩 시간 부족

**해결 방법**:
1. `datalab_scraper.py`의 `await asyncio.sleep(13)` 값을 `20`으로 증가
2. Git 커밋 및 푸시

### ❌ Workflow가 자동으로 실행 안 됨

**원인**: Cron 스케줄 또는 Actions 권한 문제

**해결 방법**:
1. `.github/workflows/daily.yml`의 cron 문법 확인
2. GitHub Actions가 활성화되어 있는지 확인:
   - 저장소 **Settings** → **Actions** → **General**
   - "Allow all actions and reusable workflows" 선택
   - **Workflow permissions**: "Read and write permissions" 선택
3. 저장소가 **Public**인지 확인 (GitHub Pages 무료 사용 조건)

### ❌ Git push 오류

**원인**: 인증 문제

**해결 방법**:
```powershell
# Personal Access Token으로 재시도
git remote set-url origin https://YOUR_TOKEN@github.com/YOUR_USERNAME/mlb-naver-datalab-reporter.git
git push -u origin main
```

### ❌ 404 Not Found (GitHub Pages)

**원인**: GitHub Pages가 아직 활성화되지 않음

**해결 방법**:
1. **첫 배포 완료 대기** (최대 10분 소요)
2. **Settings → Pages** 확인:
   - Source: `gh-pages` 브랜치
   - 초록색 체크마크 확인
3. **URL 확인**:
   - `https://YOUR_USERNAME.github.io/mlb-naver-datalab-reporter/`
   - ⚠️ 끝에 `/dashboard.html` 없이 접속

---

## 🎯 체크리스트

설정 완료 전 다음 사항들을 확인하세요:

### GitHub 저장소
- [ ] 저장소 생성 완료 (Public 저장소)
- [ ] 파일 업로드 완료
- [ ] GitHub Pages 활성화 (`gh-pages` 브랜치)

### Workflow
- [ ] `.github/workflows/daily.yml` 파일 존재
- [ ] 실행 시간 설정 확인 (매일 UTC 0시)
- [ ] Actions 권한 확인 (Read and write permissions)

### 테스트
- [ ] 수동 실행 성공 (초록색 체크)
- [ ] 대시보드 접속 확인
- [ ] 8개 키워드 이미지 모두 표시됨

---

## 🔄 일상 관리

### 매일 자동 실행
- **매일 UTC 0시** (한국 시간 오전 9시)에 자동 실행
- 별도 조치 불필요

### 주기적 확인 (선택사항)
- **주 1회**: Actions 탭에서 실행 이력 확인
- **실패 시**: GitHub에서 이메일 알림 발송

### 키워드 추가/변경
1. 네이버 데이터랩에서 새 키워드 URL 생성
2. `config.py`의 `KEYWORDS` 리스트에 추가:
   ```python
   KEYWORDS = [
       {'name': 'MLB', 'url': '...'},
       {'name': '새키워드', 'url': 'https://datalab.naver.com/...'},
   ]
   ```
3. `dashboard.html`의 `keywords` 배열에도 추가:
   ```javascript
   const keywords = [
       { name: 'MLB' },
       { name: '새키워드' },
   ];
   ```
4. Git 커밋 및 푸시

### 대시보드 디자인 변경
- `dashboard.html`의 CSS 섹션 수정
- 로컬에서 브라우저로 열어 미리보기
- Git 커밋 및 푸시 → 자동 배포

---

## 💡 추가 팁

### 비용
- **GitHub Actions**: Public 저장소는 **완전 무료** (무제한)
- **GitHub Pages**: 무료 호스팅
- 이 프로젝트는 1회 실행 시 약 **3-5분** 소요

### 알림 설정
GitHub에서 실패 시 이메일 알림:
1. **GitHub 설정**: https://github.com/settings/notifications
2. **Actions** 섹션에서 "Send notifications for failed workflows only" 체크

### 로컬 테스트
GitHub에 푸시하기 전 로컬에서 테스트:
```powershell
cd C:\Users\MADUP\Desktop\projectpung
python main.py
```

### 모바일에서 확인
대시보드는 반응형 디자인으로 제작되어 **모바일, 태블릿, PC** 모두 지원합니다!

### 북마크 추가
대시보드 URL을 브라우저 북마크에 추가하여 빠르게 접속하세요.

---

## 📞 문제 발생 시

1. **Actions 로그 확인**: 가장 상세한 오류 정보
2. **대시보드 접속**: 이미지 로딩 여부 확인
3. **GitHub Pages 상태**: Settings → Pages에서 배포 상태 확인
4. **로컬 테스트**: 코드 자체의 문제인지 확인

---

## ✅ 완료!

축하합니다! 이제 매일 자동으로 네이버 데이터랩 대시보드가 업데이트됩니다. 🎉

**다음 단계**:
- 대시보드 접속: `https://YOUR_USERNAME.github.io/mlb-naver-datalab-reporter/`
- 북마크 추가
- 첫 자동 실행까지 기다리기 (매일 오전 9시)
- 또는 "Run workflow" 버튼으로 즉시 테스트하기


# 🚀 GitHub Actions 자동화 설정 가이드

네이버 데이터랩 리포팅을 GitHub Actions로 자동화하는 방법입니다.

---

## 📋 목차

1. [GitHub 저장소 생성](#1-github-저장소-생성)
2. [GitHub Secrets 설정](#2-github-secrets-설정)
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
   - **Description**: `네이버 데이터랩 자동 리포팅 시스템`
   - **Visibility**: 
     - ⭐ **Private** (추천) - 슬랙 토큰 보안
     - Public - 공개
   - **Initialize this repository**:
     - ✅ **체크 해제** (로컬 코드를 업로드할 예정)
4. **"Create repository"** 클릭

### 1-2. 저장소 주소 복사

생성 완료 후 표시되는 주소 복사:
```
https://github.com/YOUR_USERNAME/mlb-naver-datalab-reporter.git
```

---

## 2️⃣ GitHub Secrets 설정

### 2-1. Secrets 페이지 열기

1. 생성한 저장소 페이지에서 **"Settings"** 탭 클릭
2. 왼쪽 사이드바에서 **"Secrets and variables"** 클릭
3. **"Actions"** 클릭

### 2-2. Secrets 등록

**"New repository secret"** 버튼을 눌러 다음 5개의 Secret을 하나씩 등록:

#### ① SLACK_BOT_TOKEN
```
Name: SLACK_BOT_TOKEN
Secret: xoxb-YOUR-BOT-TOKEN-HERE
```
**"Add secret"** 클릭

#### ② SLACK_CHANNEL
```
Name: SLACK_CHANNEL
Secret: #mlb-naver-datalab-reporter
```
**"Add secret"** 클릭

#### ③ MLB_URL
```
Name: MLB_URL
Secret: https://datalab.naver.com/keyword/trendResult.naver?hashKey=N_5422d72450d3c367ca4fefc5d74524a3
```
**"Add secret"** 클릭

#### ④ MLB_KIDS_URL
```
Name: MLB_KIDS_URL
Secret: https://datalab.naver.com/keyword/trendResult.naver?hashKey=N_1e264dc137a94b75c129002965cd45be
```
**"Add secret"** 클릭

#### ⑤ PADDING_URL
```
Name: PADDING_URL
Secret: https://datalab.naver.com/keyword/trendResult.naver?hashKey=N_c5184aac11432a4daed599107c939117
```
**"Add secret"** 클릭

### 2-3. 등록 확인

총 **5개의 Secrets**가 등록되었는지 확인:
- ✅ SLACK_BOT_TOKEN
- ✅ SLACK_CHANNEL
- ✅ MLB_URL
- ✅ MLB_KIDS_URL
- ✅ PADDING_URL

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
git commit -m "Initial commit: Naver Datalab Reporter"

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
3. **Note**: `Datalab Reporter Token`
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
✅ slack_sender.py
✅ requirements.txt
✅ README.md
✅ setup_guide.md
✅ .gitignore
```

❌ **업로드되면 안 되는 파일** (.gitignore로 차단됨):
```
❌ .env (슬랙 토큰 포함)
❌ screenshots/ (로컬 스크린샷)
❌ logs/ (로컬 로그)
❌ __pycache__/
```

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
2. **"report"** job 클릭
3. 각 단계별 로그 확인 가능

### 5-4. 슬랙 확인

실행 성공 시 **#mlb-naver-datalab-reporter** 채널에 다음 메시지 도착:
```
📊 네이버 검색 트렌드: MLB
📊 네이버 검색 트렌드: MLB키즈
📊 네이버 검색 트렌드: 패딩
```
각 메시지에 스크린샷 첨부됨

### 5-5. 스크린샷/로그 다운로드

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
   - Secrets 설정 누락 또는 오타
   - 네이버 데이터랩 URL 변경
   - Slack 토큰 만료

### ❌ Slack 메시지가 안 옴

**원인**: Slack 연동 문제

**해결 방법**:
1. **Secrets 확인**:
   - `SLACK_BOT_TOKEN` 값이 정확한지
   - `SLACK_CHANNEL` 값이 `#mlb-naver-datalab-reporter`인지
2. **Slack 앱 권한 확인**:
   - `chat:write` (메시지 전송)
   - `chat:write.public` (공개 채널 접근)
   - `files:write` (파일 업로드)
3. **채널에 앱 추가**:
   - Slack 채널에서 `/invite @Datalab Reporter` 실행

### ❌ 스크린샷이 비어있음

**원인**: 네이버 데이터랩 로딩 시간 부족

**해결 방법**:
1. `datalab_scraper.py`의 `asyncio.sleep(2)` 값을 `5`로 증가
2. Git 커밋 및 푸시

### ❌ Workflow가 자동으로 실행 안 됨

**원인**: Cron 스케줄 문제

**해결 방법**:
1. `.github/workflows/daily.yml`의 cron 문법 확인
2. GitHub Actions가 활성화되어 있는지 확인:
   - 저장소 **Settings** → **Actions** → **General**
   - "Allow all actions and reusable workflows" 선택
3. 저장소가 Public이면 즉시 작동
4. 저장소가 Private이면 GitHub Free 플랜에서는 월 2,000분 제한 있음

### ❌ Git push 오류

**원인**: 인증 문제

**해결 방법**:
```powershell
# Personal Access Token으로 재시도
git remote set-url origin https://YOUR_TOKEN@github.com/YOUR_USERNAME/mlb-naver-datalab-reporter.git
git push -u origin main
```

---

## 🎯 체크리스트

설정 완료 전 다음 사항들을 확인하세요:

### GitHub 저장소
- [ ] 저장소 생성 완료
- [ ] Private 저장소 (보안 권장)
- [ ] 파일 업로드 완료

### GitHub Secrets
- [ ] SLACK_BOT_TOKEN 등록
- [ ] SLACK_CHANNEL 등록
- [ ] MLB_URL 등록
- [ ] MLB_KIDS_URL 등록
- [ ] PADDING_URL 등록

### Workflow
- [ ] `.github/workflows/daily.yml` 파일 존재
- [ ] 실행 시간 설정 확인
- [ ] Actions 활성화 확인

### 테스트
- [ ] 수동 실행 성공
- [ ] Slack 메시지 수신 확인
- [ ] 스크린샷 정상 확인

---

## 🔄 일상 관리

### 매일 자동 실행
- **설정한 시간**에 자동으로 실행됨
- 별도 조치 불필요

### 주기적 확인 (선택사항)
- **주 1회**: Actions 탭에서 실행 이력 확인
- **실패 시**: 이메일 알림 옴 (GitHub 설정)

### 키워드 추가/변경
1. 네이버 데이터랩에서 새 URL 생성
2. GitHub Secrets에 추가 (예: `NEW_KEYWORD_URL`)
3. `config.py`의 `KEYWORD_URLS` 딕셔너리에 추가
4. Git 커밋 및 푸시

### Slack 토큰 갱신
1. Slack에서 새 토큰 발급
2. GitHub Secrets의 `SLACK_BOT_TOKEN` 값 업데이트

---

## 💡 추가 팁

### 비용
- **GitHub Actions**: Private 저장소는 월 2,000분 무료
- 이 프로젝트는 1회 실행 시 약 **2-3분** 소요
- 매일 1회 실행: **월 60-90분** (무료 범위 내)

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

---

## 📞 문제 발생 시

1. **Actions 로그 확인**: 가장 상세한 오류 정보
2. **Slack 채널 확인**: 메시지 도착 여부
3. **Secrets 재확인**: 오타가 가장 흔한 원인
4. **로컬 테스트**: 코드 자체의 문제인지 확인

---

## ✅ 완료!

축하합니다! 이제 매일 자동으로 네이버 데이터랩 리포트가 슬랙으로 전송됩니다. 🎉

**다음 단계**:
- 첫 자동 실행까지 기다리기 (설정한 시간)
- 또는 "Run workflow" 버튼으로 즉시 테스트하기


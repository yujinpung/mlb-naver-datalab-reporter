# 🔗 Slack Webhook 등록 상세 가이드

단계별로 Slack Webhook을 등록하는 방법입니다.

---

## 📋 목차

1. [Slack Webhook URL 생성](#1-slack-webhook-url-생성)
2. [GitHub Secrets 등록](#2-github-secrets-등록)
3. [테스트 실행](#3-테스트-실행)

---

## 1️⃣ Slack Webhook URL 생성

### Step 1: Slack API 페이지 접속

1. 브라우저에서 다음 주소 접속:
   ```
   https://api.slack.com/messaging/webhooks
   ```

2. **Slack 계정으로 로그인** (필요시)

---

### Step 2: 앱 생성 또는 선택

#### 방법 A: 새 앱 생성 (추천)

1. 페이지에서 **"Create your Slack app"** 버튼 클릭
   - 또는 **"Create New App"** 버튼 클릭

2. **"From scratch"** 선택
   - "From an app manifest" 또는 다른 옵션 선택하지 마세요

3. **앱 정보 입력**:
   - **App Name**: `Naver Datalab Reporter` (또는 원하는 이름)
   - **Pick a workspace**: 워크스페이스 선택
   - **"Create App"** 버튼 클릭

#### 방법 B: 기존 앱 사용

1. **https://api.slack.com/apps** 접속
2. 기존 앱 선택

---

### Step 3: Incoming Webhooks 활성화

1. 왼쪽 사이드바에서 **"Incoming Webhooks"** 클릭
   - 또는 **"Features" → "Incoming Webhooks"** 클릭

2. **"Activate Incoming Webhooks"** 토글을 **ON**으로 변경
   - 오른쪽으로 스위치를 밀어서 활성화

3. 페이지 하단으로 스크롤

---

### Step 4: Webhook 생성

1. **"Add New Webhook to Workspace"** 버튼 클릭
   - 또는 **"Add New Webhook to Workspace"** 링크 클릭

2. **채널 선택**:
   - 드롭다운에서 `#mlb-naver-datalab-reporter` 선택
   - 또는 원하는 채널 선택
   - 채널이 없다면 먼저 슬랙에서 채널 생성

3. **"Allow"** 버튼 클릭

---

### Step 5: Webhook URL 복사

1. 생성된 Webhook URL 확인
   - 형식: `https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX`
   - 예시: `https://hooks.slack.com/services/T01234567/B09876543/abcdefghijklmnopqrstuvwx`

2. **Webhook URL 복사**
   - URL 전체를 복사 (Ctrl+C 또는 우클릭 → 복사)
   - 이 URL은 나중에 다시 볼 수 없으므로 **반드시 복사해두세요!**

---

## 2️⃣ GitHub Secrets 등록

### Step 1: GitHub 저장소 접속

1. 브라우저에서 다음 주소 접속:
   ```
   https://github.com/yujinpung/mlb-naver-datalab-reporter
   ```

2. **GitHub 계정으로 로그인** (필요시)

---

### Step 2: Secrets 페이지 열기

1. 저장소 페이지에서 **"Settings"** 탭 클릭
   - 상단 메뉴에서 "Settings" 선택

2. 왼쪽 사이드바에서 **"Secrets and variables"** 클릭
   - "Security" 섹션 아래에 있습니다

3. **"Actions"** 클릭
   - "Repository secrets" 또는 "Actions secrets" 선택

---

### Step 3: SLACK_WEBHOOK_URL Secret 추가

1. **"New repository secret"** 버튼 클릭
   - 오른쪽 상단에 있습니다

2. **Secret 정보 입력**:
   ```
   Name: SLACK_WEBHOOK_URL
   Secret: [복사한 Webhook URL 붙여넣기]
   ```
   - **Name**: 정확히 `SLACK_WEBHOOK_URL` 입력 (대소문자 구분)
   - **Secret**: Step 5에서 복사한 Webhook URL 붙여넣기

3. **"Add secret"** 버튼 클릭

4. **등록 확인**:
   - Secrets 목록에 `SLACK_WEBHOOK_URL`이 표시되는지 확인
   - 값은 `***`로 마스킹되어 표시됩니다

---

### Step 4: 기존 Secrets 확인 (선택사항)

다음 Secrets도 등록되어 있는지 확인:
- ✅ `SLACK_CHANNEL`: `#mlb-naver-datalab-reporter`
- ✅ `FIREBASE_STORAGE_BUCKET`: Firebase Storage 버킷 이름 (이미지 전송용)
- ✅ `FIREBASE_CREDENTIALS_JSON`: Firebase 인증 정보 (이미지 전송용)
- ✅ `FIREBASE_PROJECT_ID`: Firebase 프로젝트 ID (이미지 전송용)
- ✅ `FIREBASE_SERVICE_ACCOUNT`: Firebase 서비스 계정 (이미지 전송용)

> **참고**: 이미지 전송을 위해서는 Firebase Storage 설정이 필요합니다.
> Firebase가 없다면 텍스트 메시지만 전송됩니다.

---

## 3️⃣ 테스트 실행

### Step 1: GitHub Actions 페이지 접속

1. 저장소 페이지에서 **"Actions"** 탭 클릭

2. 왼쪽 사이드바에서 **"Daily Naver Datalab Report"** 워크플로우 클릭

---

### Step 2: 수동 실행

1. 오른쪽 상단의 **"Run workflow"** 버튼 클릭
   - 드롭다운이 열립니다

2. **"Run workflow"** 버튼 클릭
   - 기본 설정으로 실행됩니다

---

### Step 3: 실행 상태 확인

1. **실행 목록 확인**:
   - 최신 실행이 목록 맨 위에 표시됩니다
   - 노란색 점: 실행 중
   - 초록색 체크: 성공
   - 빨간색 X: 실패

2. **실행 클릭하여 상세 로그 확인**:
   - 각 단계를 클릭하여 로그 확인
   - "Run Datalab Report" 단계에서 슬랙 전송 로그 확인

---

### Step 4: 슬랙 채널 확인

1. **Slack 앱 또는 웹사이트 열기**

2. **`#mlb-naver-datalab-reporter` 채널 열기**
   - 또는 Webhook을 등록한 채널 열기

3. **메시지 확인**:
   - ✅ 메시지가 도착했는지 확인
   - ✅ 이미지가 표시되는지 확인 (Firebase Storage 설정 시)
   - ✅ 텍스트 메시지만 표시되는지 확인 (Firebase Storage 미설정 시)

---

## ✅ 성공 확인

다음이 모두 확인되면 성공입니다:

- [ ] GitHub Actions 실행 성공 (초록색 체크)
- [ ] "Run Datalab Report" 단계 로그에서 "✅ 슬랙 전송 완료" 메시지 확인
- [ ] 슬랙 채널에서 메시지 수신 확인
- [ ] 이미지가 표시되는지 확인 (Firebase Storage 설정 시)

---

## 🔍 문제 해결

### ❌ "Webhook URL이 없어 메시지 전송 불가" 오류

**원인**: `SLACK_WEBHOOK_URL` Secret이 등록되지 않음

**해결 방법**:
1. GitHub Secrets 페이지에서 `SLACK_WEBHOOK_URL` 확인
2. Secret 이름이 정확한지 확인 (대소문자 구분)
3. Secret 값이 올바른지 확인

---

### ❌ "invalid_payload" 오류

**원인**: Webhook URL이 잘못되었거나 만료됨

**해결 방법**:
1. Slack API 페이지에서 Webhook URL 다시 확인
2. 새 Webhook URL 생성
3. GitHub Secrets 업데이트

---

### ❌ 메시지는 도착하지만 이미지가 표시되지 않음

**원인**: Firebase Storage 설정이 없거나 업로드 실패

**해결 방법**:
1. Firebase Storage 설정 확인
2. GitHub Secrets의 Firebase 관련 Secrets 확인
3. 로그에서 Firebase 업로드 오류 확인

---

### ❌ "channel_not_found" 오류

**원인**: Webhook이 등록된 채널이 존재하지 않음

**해결 방법**:
1. 슬랙에서 채널이 존재하는지 확인
2. Webhook을 올바른 채널에 다시 등록

---

## 📝 체크리스트

Webhook 등록 완료 체크리스트:

- [ ] Slack API 페이지 접속
- [ ] 앱 생성 또는 선택
- [ ] Incoming Webhooks 활성화
- [ ] Webhook 생성 및 채널 선택
- [ ] Webhook URL 복사
- [ ] GitHub Secrets 페이지 접속
- [ ] `SLACK_WEBHOOK_URL` Secret 추가
- [ ] GitHub Actions 테스트 실행
- [ ] 슬랙 채널에서 메시지 수신 확인

---

## 💡 참고사항

### Webhook URL 보안

- ⚠️ **절대 공개하지 마세요!**
- ⚠️ GitHub에 커밋하지 마세요
- ⚠️ `.env` 파일은 `.gitignore`에 추가되어 있습니다
- ✅ GitHub Secrets에만 저장하세요

### Webhook URL 재생성

- Webhook URL은 언제든지 재생성할 수 있습니다
- 재생성 시 이전 URL은 무효화됩니다
- 새 URL을 GitHub Secrets에 업데이트하세요

### 채널 변경

- Webhook을 다른 채널로 변경하려면:
  1. Slack API 페이지에서 Webhook 삭제
  2. 새 채널로 Webhook 재생성
  3. GitHub Secrets 업데이트 (URL이 변경될 수 있음)

---

## 🎯 다음 단계

Webhook 등록이 완료되면:

1. ✅ GitHub Actions에서 테스트 실행
2. ✅ 슬랙 채널에서 메시지 확인
3. ✅ 매일 자동 실행 확인 (오전 9시)

자세한 내용은 [`WEBHOOK_SETUP.md`](WEBHOOK_SETUP.md) 참고하세요.


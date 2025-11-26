# 🔗 슬랙 웹훅 URL 생성 완벽 가이드 (상세 버전)

## 📋 목차

1. [준비사항](#준비사항)
2. [슬랙 채널 생성](#1-슬랙-채널-생성)
3. [슬랙 앱 생성](#2-슬랙-앱-생성)
4. [Incoming Webhooks 설정](#3-incoming-webhooks-설정)
5. [Webhook URL 생성](#4-webhook-url-생성)
6. [GitHub Secrets 등록](#5-github-secrets-등록)
7. [테스트 및 확인](#6-테스트-및-확인)

---

## 준비사항

### 필요한 것

- ✅ 슬랙 워크스페이스 (회사 또는 개인)
- ✅ 워크스페이스 관리자 권한 (앱 설치 권한)
- ✅ GitHub 저장소 접근 권한
- ✅ 브라우저 (Chrome, Edge, Firefox 등)

### 예상 소요 시간

- 🕐 약 5-10분

---

## 1. 슬랙 채널 생성

먼저 메시지를 받을 슬랙 채널을 만듭니다.

### 1-1. 슬랙 앱 또는 웹 접속

```
https://slack.com/
또는
슬랙 데스크톱 앱 실행
```

### 1-2. 채널 생성

**방법 1: 사이드바에서 생성**

1. 왼쪽 사이드바에서 **"Channels"** 옆의 **+** 버튼 클릭

2. **"Create a channel"** 선택

3. 채널 정보 입력:
   ```
   Name: mlb-naver-datalab-reporter
   Description: 네이버 데이터랩 자동 리포트 수신용
   ```

4. **채널 공개 설정**:
   - **Public** (추천): 모든 워크스페이스 멤버 접근 가능
   - **Private**: 초대된 사람만 접근 가능

5. **"Create"** 버튼 클릭

**방법 2: 단축키 사용**

1. `Ctrl + Shift + N` (Windows) 또는 `Cmd + Shift + N` (Mac)

2. 채널 이름 입력 후 생성

### 1-3. 채널 확인

왼쪽 사이드바에 `#mlb-naver-datalab-reporter` 채널이 보이면 성공!

---

## 2. 슬랙 앱 생성

이제 메시지를 보낼 슬랙 앱을 만듭니다.

### 2-1. Slack API 페이지 접속

브라우저에서 다음 링크를 엽니다:

```
https://api.slack.com/messaging/webhooks
```

또는

```
https://api.slack.com/apps
```

### 2-2. 로그인

슬랙 계정으로 로그인:
- 워크스페이스 선택
- 이메일/비밀번호 입력
- 또는 Google/Apple 계정으로 로그인

### 2-3. 앱 생성 시작

페이지 상단 또는 중앙에서 **"Create New App"** 또는 **"Create an App"** 버튼 클릭

### 2-4. 앱 생성 방법 선택

팝업 창이 나타나면:

```
┌──────────────────────────────────────────────┐
│  Create an app                               │
├──────────────────────────────────────────────┤
│                                              │
│  ┌────────────────────────────────────────┐ │
│  │  📝 From scratch                       │ │
│  │  Create a new app with no              │ │
│  │  pre-built functionality               │ │
│  └────────────────────────────────────────┘ │
│                                              │
│  ┌────────────────────────────────────────┐ │
│  │  📄 From an app manifest               │ │
│  │  Create an app from a                  │ │
│  │  configuration file                    │ │
│  └────────────────────────────────────────┘ │
│                                              │
└──────────────────────────────────────────────┘
```

**"From scratch"** 선택 (위쪽 옵션)

### 2-5. 앱 정보 입력

다음 정보를 입력합니다:

```
┌──────────────────────────────────────────────┐
│  Name your app & choose a workspace          │
├──────────────────────────────────────────────┤
│                                              │
│  App Name *                                  │
│  ┌────────────────────────────────────────┐ │
│  │ Naver Datalab Reporter                 │ │
│  └────────────────────────────────────────┘ │
│                                              │
│  Pick a workspace to develop your app in: * │
│  ┌────────────────────────────────────────┐ │
│  │ [선택한 워크스페이스 이름] ▼          │ │
│  └────────────────────────────────────────┘ │
│                                              │
│              [Create App]                    │
│                                              │
└──────────────────────────────────────────────┘
```

**입력 예시**:
- **App Name**: `Naver Datalab Reporter` (또는 원하는 이름)
- **Workspace**: 드롭다운에서 워크스페이스 선택

### 2-6. 앱 생성 완료

**"Create App"** 버튼 클릭

성공하면 앱 설정 페이지로 이동합니다.

---

## 3. Incoming Webhooks 설정

앱에서 Webhook 기능을 활성화합니다.

### 3-1. Incoming Webhooks 페이지 접속

**방법 1: 왼쪽 메뉴에서**

왼쪽 사이드바 메뉴에서 **"Incoming Webhooks"** 클릭

```
┌────────────────────────┐
│  Features              │
├────────────────────────┤
│  ○ App Home            │
│  ○ Incoming Webhooks   │ ← 클릭
│  ○ Interactivity       │
│  ○ Slash Commands      │
│  ○ Event Subscriptions │
└────────────────────────┘
```

**방법 2: 직접 링크 접속**

```
https://api.slack.com/apps/[YOUR_APP_ID]/incoming-webhooks
```

### 3-2. Incoming Webhooks 활성화

페이지 상단에 토글 스위치가 있습니다:

```
┌──────────────────────────────────────────────┐
│  Incoming Webhooks                           │
├──────────────────────────────────────────────┤
│                                              │
│  Activate Incoming Webhooks        ○ → ●    │
│                                     OFF  ON  │
│                                              │
└──────────────────────────────────────────────┘
```

**오른쪽 토글을 클릭하여 OFF → ON으로 변경**

### 3-3. 페이지 새로고침 확인

토글이 **초록색**으로 변하면 성공!

페이지가 자동으로 새로고침되면서 아래쪽에 새로운 섹션이 나타납니다:

```
┌──────────────────────────────────────────────┐
│  Webhook URLs for Your Workspace             │
├──────────────────────────────────────────────┤
│  No webhook URLs yet                         │
│                                              │
│  [Add New Webhook to Workspace]              │
│                                              │
└──────────────────────────────────────────────┘
```

---

## 4. Webhook URL 생성

이제 실제로 사용할 Webhook URL을 생성합니다.

### 4-1. Webhook 추가 시작

페이지 하단의 **"Add New Webhook to Workspace"** 버튼 클릭

### 4-2. 권한 요청 화면

새 창 또는 페이지가 열리면서 권한 요청 화면이 나타납니다:

```
┌──────────────────────────────────────────────────────┐
│  [앱 이름] is requesting permission to access        │
│  the [워크스페이스 이름] Slack workspace             │
├──────────────────────────────────────────────────────┤
│                                                      │
│  [앱 아이콘]  Naver Datalab Reporter                │
│                                                      │
│  This app would like to:                            │
│  • Post messages to specific channels               │
│                                                      │
│  Where should [앱 이름] post?                       │
│  ┌──────────────────────────────────────────────┐  │
│  │ 🔍 Search for a channel...                   │  │
│  ├──────────────────────────────────────────────┤  │
│  │  # general                                   │  │
│  │  # mlb-naver-datalab-reporter  ✓             │  │ ← 선택
│  │  # random                                    │  │
│  │  ... (다른 채널들)                           │  │
│  └──────────────────────────────────────────────┘  │
│                                                      │
│  Learn more about [앱 이름]                         │
│                                                      │
│              [Cancel]    [Allow]                    │
│                                                      │
└──────────────────────────────────────────────────────┘
```

### 4-3. 채널 선택

1. **검색창에서 채널 검색** (선택사항):
   ```
   mlb-naver-datalab-reporter
   ```

2. **`#mlb-naver-datalab-reporter` 선택**
   - 클릭하면 체크 표시(✓)가 나타남

3. **다른 채널을 선택하지 않도록 주의!**

### 4-4. 권한 허용

화면 하단의 **초록색 "Allow" 버튼** 클릭

### 4-5. Webhook URL 생성 확인

다시 이전 페이지로 돌아오면, 새로운 Webhook URL이 생성되어 있습니다:

```
┌───────────────────────────────────────────────────────────┐
│  Webhook URLs for Your Workspace                          │
├───────────────────────────────────────────────────────────┤
│                                                           │
│  ┌─────────────────────────────────────────────────────┐ │
│  │  Sample curl request to post to a channel:          │ │
│  │                                                      │ │
│  │  Webhook URL                                         │ │
│  │  https://hooks.slack.com/services/T01234ABC/        │ │
│  │  B01234XYZ/abcdefghijklmnopqrstuvwxyz1234           │ │
│  │                                              [Copy]  │ │
│  │                                                      │ │
│  │  Channel: #mlb-naver-datalab-reporter               │ │
│  │  Configuration: Edit  Delete                        │ │
│  └─────────────────────────────────────────────────────┘ │
│                                                           │
│  [Add New Webhook to Workspace]                          │
│                                                           │
└───────────────────────────────────────────────────────────┘
```

### 4-6. Webhook URL 복사

**"Copy" 버튼 클릭** 또는 **URL을 마우스로 드래그하여 복사**

복사된 URL 형식:
```
https://hooks.slack.com/services/T01234ABC/B01234XYZ/abcdefghijklmnopqrstuvwxyz1234
```

⚠️ **매우 중요**: 
- 이 URL은 비밀번호와 같습니다!
- 누구나 이 URL을 알면 채널에 메시지를 보낼 수 있습니다!
- 안전한 곳에 보관하세요!

### 4-7. URL 저장 (임시)

메모장이나 안전한 곳에 임시로 붙여넣기 (다음 단계에서 사용)

---

## 5. GitHub Secrets 등록

이제 복사한 Webhook URL을 GitHub에 안전하게 저장합니다.

### 5-1. GitHub 저장소 Settings 접속

**방법 1: 직접 링크**

브라우저 새 탭에서:
```
https://github.com/yujinpung/mlb-naver-datalab-reporter/settings
```

**방법 2: 수동 접속**

1. GitHub 저장소 접속:
   ```
   https://github.com/yujinpung/mlb-naver-datalab-reporter
   ```

2. 상단 메뉴에서 **"Settings"** 탭 클릭

### 5-2. Secrets and variables 메뉴 접속

왼쪽 사이드바에서:

```
┌────────────────────────────────────┐
│  Settings                          │
├────────────────────────────────────┤
│  General                           │
│  Access                            │
│    Collaborators                   │
│    Moderation options             │
│  Code and automation              │
│    Branches                        │
│    Tags                            │
│    Actions                         │
│      General                       │
│      Runners                       │
│      ▶ Secrets and variables       │ ← 클릭하여 펼치기
│        Actions                     │ ← 그 다음 클릭
│        Codespaces                  │
│        Dependabot                  │
└────────────────────────────────────┘
```

1. **"Secrets and variables"** 옆의 **▶** 화살표 클릭 (펼치기)
2. 하위 메뉴에서 **"Actions"** 클릭

### 5-3. Secrets 페이지 확인

페이지가 열리면 다음과 같은 화면이 나타납니다:

```
┌─────────────────────────────────────────────────────────┐
│  Actions secrets and variables                          │
├─────────────────────────────────────────────────────────┤
│  [Secrets]  [Variables]                                 │
│                                                          │
│  Secrets                                                 │
│  ────────────────────────────────────────────────────  │
│  Environment secrets are not available for public       │
│  repositories.                                           │
│                                                          │
│  Repository secrets                                      │
│  Secrets are encrypted and sent to GitHub Actions.      │
│  Anyone with collaborator access can use these secrets  │
│  in Actions.                                             │
│                                                          │
│  [New repository secret]                                │
│                                                          │
│  (기존 Secrets 목록 - 있다면)                          │
│  ────────────────────────────────────────────────────  │
│  Name                        Updated                    │
│  FIREBASE_CREDENTIALS_JSON   2 days ago                 │
│  FIREBASE_PROJECT_ID         2 days ago                 │
│  ...                                                     │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

### 5-4. 새 Secret 추가

**"New repository secret"** 버튼 클릭 (초록색 버튼)

### 5-5. Secret 정보 입력

새 페이지가 열리면:

```
┌─────────────────────────────────────────────────────────┐
│  Actions secrets / New secret                           │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  Name *                                                  │
│  ┌────────────────────────────────────────────────────┐ │
│  │ SLACK_WEBHOOK_URL                                  │ │
│  └────────────────────────────────────────────────────┘ │
│  Secret names can only contain alphanumeric characters  │
│  ([a-z], [A-Z], [0-9]) or underscores (_). Spaces are  │
│  not allowed. Must start with a letter or _.            │
│                                                          │
│  Secret *                                                │
│  ┌────────────────────────────────────────────────────┐ │
│  │ https://hooks.slack.com/services/T01234ABC/        │ │
│  │ B01234XYZ/abcdefghijklmnopqrstuvwxyz1234           │ │
│  └────────────────────────────────────────────────────┘ │
│                                                          │
│              [Add secret]                                │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

**입력 내용**:

1. **Name** 필드에 정확히 입력 (대소문자 구분!):
   ```
   SLACK_WEBHOOK_URL
   ```

2. **Secret** 필드에 복사한 Webhook URL 붙여넣기:
   ```
   https://hooks.slack.com/services/T01234ABC/B01234XYZ/abcdefghijklmnopqrstuvwxyz1234
   ```

### 5-6. Secret 추가 완료

**"Add secret"** 버튼 클릭 (초록색 버튼)

### 5-7. Secret 등록 확인

이전 페이지로 돌아오면서 새 Secret이 추가되었습니다:

```
┌─────────────────────────────────────────────────────────┐
│  Repository secrets                                      │
│                                                          │
│  Name                        Updated                    │
│  ────────────────────────────────────────────────────  │
│  SLACK_WEBHOOK_URL          just now            [...]  │ ← 새로 추가됨!
│  FIREBASE_CREDENTIALS_JSON  2 days ago          [...]  │
│  FIREBASE_PROJECT_ID        2 days ago          [...]  │
│  ...                                                     │
└─────────────────────────────────────────────────────────┘
```

✅ **성공!** `SLACK_WEBHOOK_URL`이 목록에 보이면 완료입니다!

---

## 6. 테스트 및 확인

이제 모든 설정이 완료되었으니 테스트해봅시다!

### 6-1. GitHub Actions 페이지 접속

```
https://github.com/yujinpung/mlb-naver-datalab-reporter/actions
```

### 6-2. 워크플로우 선택

왼쪽 사이드바에서:

```
┌────────────────────────────────────┐
│  All workflows                     │
├────────────────────────────────────┤
│  ✓ Daily Naver Datalab Report      │ ← 클릭
└────────────────────────────────────┘
```

**"Daily Naver Datalab Report"** 클릭

### 6-3. 워크플로우 수동 실행

페이지 오른쪽 상단에:

```
┌─────────────────────────────────────────────────────────┐
│  Daily Naver Datalab Report                             │
│                                                          │
│  This workflow has a workflow_dispatch event trigger.   │
│                                              ┌─────────┐ │
│                                              │Run work │ │
│                                              │  flow   │ │ ← 클릭
│                                              └─────────┘ │
└─────────────────────────────────────────────────────────┘
```

**"Run workflow"** 버튼 클릭 (회색 버튼)

### 6-4. 브랜치 선택

드롭다운 메뉴가 나타나면:

```
┌─────────────────────────────────────┐
│  Use workflow from                  │
│  ┌───────────────────────────────┐  │
│  │ Branch: main              ▼   │  │ ← 확인
│  └───────────────────────────────┘  │
│                                     │
│         [Run workflow]              │ ← 클릭
│                                     │
└─────────────────────────────────────┘
```

1. **"Branch: main"** 선택되어 있는지 확인
2. **초록색 "Run workflow"** 버튼 클릭

### 6-5. 실행 시작 확인

페이지 상단에 노란색 알림이 나타납니다:

```
✓ Workflow run was successfully requested.
```

**페이지 새로고침 (F5 또는 브라우저 새로고침 버튼)**

### 6-6. 실행 상태 확인

페이지 상단에 새로운 실행 항목이 나타납니다:

```
┌─────────────────────────────────────────────────────────┐
│  All workflows                                          │
├─────────────────────────────────────────────────────────┤
│  🟡 Update dashboard and screenshots...  main  #123    │ ← 실행 중 (노란색)
│     username · Workflow dispatch                        │
│     ⏱️ in progress                                      │
│                                                          │
│  ✅ Update dashboard and screenshots...  main  #122    │ ← 이전 실행 (성공)
│     username · Schedule                                 │
│     ✓ 5 minutes ago in 3m 24s                          │
└─────────────────────────────────────────────────────────┘
```

상태 표시:
- 🟡 **노란색 점**: 실행 중
- ✅ **초록색 체크**: 성공
- ❌ **빨간색 X**: 실패

### 6-7. 로그 확인

실행 중인 항목을 클릭하여 상세 로그를 확인합니다:

```
┌─────────────────────────────────────────────────────────┐
│  Update dashboard and screenshots...                    │
├─────────────────────────────────────────────────────────┤
│  Summary  Jobs(1)                                       │
│                                                          │
│  ✓ datalab-report (ubuntu-latest)          3m 24s      │
│    ├─ ✓ Checkout code                      2s         │
│    ├─ ✓ Set up Python 3.9                  15s        │
│    ├─ ✓ Install dependencies               23s        │
│    ├─ ✓ Install Playwright browsers        45s        │
│    ├─ ✓ Create required directories        1s         │
│    ├─ 🟡 Run Datalab Report                 ← 실행 중  │
│    ├─ ⏸️ Commit and push screenshots                   │
│    └─ ⏸️ Deploy to GitHub Pages                        │
└─────────────────────────────────────────────────────────┘
```

**"Run Datalab Report"** 단계를 클릭하여 실시간 로그 확인

### 6-8. 슬랙 전송 로그 확인

로그에서 다음 메시지를 찾습니다:

```
📤 STEP 3: 슬랙 전송

  키워드 'MLB' 전송 중...
  ✅ 'MLB' 전송 완료
  
  키워드 'MLB키즈' 전송 중...
  ✅ 'MLB키즈' 전송 완료
  
  키워드 '패딩' 전송 중...
  ✅ '패딩' 전송 완료
  
  ... (계속)
  
✅ 슬랙 전송 완료: 8/8개
```

### 6-9. 슬랙 채널 확인

1. **슬랙 앱 또는 웹 열기**

2. **`#mlb-naver-datalab-reporter` 채널 접속**

3. **8개 메시지 확인**:

```
┌─────────────────────────────────────────────────────────┐
│  #mlb-naver-datalab-reporter                            │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  🤖 Naver Datalab Reporter  APP  5:00 PM                │
│  📊 네이버 검색 트렌드: MLB                            │
│  ┌────────────────────────────────────────────────────┐ │
│  │                                                    │ │
│  │  [네이버 데이터랩 그래프 이미지]                  │ │
│  │                                                    │ │
│  └────────────────────────────────────────────────────┘ │
│                                                          │
│  🤖 Naver Datalab Reporter  APP  5:00 PM                │
│  📊 네이버 검색 트렌드: MLB키즈                        │
│  ┌────────────────────────────────────────────────────┐ │
│  │                                                    │ │
│  │  [네이버 데이터랩 그래프 이미지]                  │ │
│  │                                                    │ │
│  └────────────────────────────────────────────────────┘ │
│                                                          │
│  ... (8개 메시지 모두)                                  │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

✅ **성공!** 8개 메시지가 모두 이미지와 함께 도착했다면 완벽하게 설정된 것입니다!

---

## 🐛 자주 발생하는 문제와 해결

### 문제 1: "invalid_auth" 오류

**증상**:
```
❌ 슬랙 API 오류: invalid_auth
```

**원인**:
- Webhook URL이 잘못 복사됨
- URL에 공백이나 줄바꿈이 포함됨
- Secret 이름이 잘못됨

**해결**:
1. GitHub Secrets에서 `SLACK_WEBHOOK_URL` 확인
2. Secret을 삭제하고 다시 추가
3. Webhook URL을 다시 복사할 때 앞뒤 공백 제거
4. URL이 한 줄로 되어 있는지 확인

### 문제 2: Secret을 찾을 수 없음

**증상**:
```
SLACK_WEBHOOK_URL이 설정되지 않았습니다
```

**원인**:
- Secret 이름이 정확하지 않음
- 대소문자가 다름
- 공백이 포함됨

**해결**:
1. Secret 이름을 정확히 확인: `SLACK_WEBHOOK_URL` (모두 대문자, 언더스코어 사용)
2. 오타가 없는지 확인
3. 필요시 Secret 삭제 후 재생성

### 문제 3: 슬랙 메시지는 오지만 이미지가 없음

**증상**:
- 슬랙 메시지는 도착함
- 이미지가 표시되지 않거나 깨진 이미지 아이콘

**원인**:
- GitHub에 스크린샷이 업로드되지 않음
- GitHub Raw URL이 아직 활성화되지 않음

**해결**:
1. GitHub 저장소의 `screenshots/` 폴더 확인
2. 5-10분 대기 후 재시도 (GitHub Raw URL 캐싱 시간)
3. 브라우저에서 이미지 URL 직접 접속 테스트

### 문제 4: 채널에 메시지가 안 옴

**원인**:
- Webhook이 다른 채널에 연결됨
- 채널이 삭제됨
- 워크스페이스 권한 문제

**해결**:
1. Slack API 페이지에서 Webhook 설정 확인
2. 올바른 채널에 연결되어 있는지 확인
3. 필요시 Webhook 삭제 후 재생성

---

## 🔒 보안 모범 사례

### ✅ 해야 할 것

1. **GitHub Secrets 사용**
   - 모든 민감한 정보는 Secrets에 저장

2. **`.env` 파일 보호**
   - `.gitignore`에 포함되어 있는지 확인
   - 절대 Git에 커밋하지 않기

3. **Webhook URL 주기적 갱신**
   - 3-6개월마다 새 URL 생성 고려

4. **접근 권한 최소화**
   - 필요한 사람에게만 저장소 접근 권한 부여

### ❌ 하지 말아야 할 것

1. **Webhook URL 공개**
   - 공개 저장소에 커밋
   - 이메일, 메신저로 공유
   - 스크린샷에 노출

2. **테스트 URL 재사용**
   - 테스트용과 운영용 URL 분리

3. **권한 남용**
   - 불필요한 권한 요청하지 않기

---

## 📚 추가 자료

### 공식 문서

- [Slack Incoming Webhooks 공식 문서](https://api.slack.com/messaging/webhooks)
- [GitHub Secrets 공식 문서](https://docs.github.com/en/actions/security-guides/encrypted-secrets)

### 프로젝트 가이드

- [`SLACK_WEBHOOK_SETUP_QUICK.md`](SLACK_WEBHOOK_SETUP_QUICK.md) - 빠른 설정
- [`WEBHOOK_SETUP.md`](WEBHOOK_SETUP.md) - 기본 가이드
- [`SLACK_TROUBLESHOOTING.md`](SLACK_TROUBLESHOOTING.md) - 문제 해결
- [`GITHUB_ACTIONS_MANUAL_RUN.md`](GITHUB_ACTIONS_MANUAL_RUN.md) - GitHub Actions 수동 실행

---

## ✅ 최종 체크리스트

설정이 완료되었는지 확인하세요:

- [ ] 슬랙 워크스페이스 접속 완료
- [ ] `#mlb-naver-datalab-reporter` 채널 생성 완료
- [ ] Slack API 페이지에서 앱 생성 완료
- [ ] Incoming Webhooks 활성화 완료
- [ ] Webhook URL 생성 및 복사 완료
- [ ] GitHub Secrets에 `SLACK_WEBHOOK_URL` 등록 완료
- [ ] GitHub Actions 수동 실행 완료
- [ ] Actions 로그에서 "✅ 슬랙 전송 완료: 8/8개" 확인
- [ ] 슬랙 채널에서 8개 메시지 수신 확인
- [ ] 각 메시지에 이미지가 정상적으로 표시되는지 확인

---

## 🎉 축하합니다!

모든 설정이 완료되었습니다!

이제 매일 오전 9시에 자동으로:
- ✅ 네이버 데이터랩에서 8개 키워드 트렌드 수집
- ✅ 슬랙으로 이미지 포함 메시지 전송
- ✅ 대시보드 자동 업데이트

더 궁금한 사항이 있으면 다른 가이드 문서를 참고하세요! 🚀


# ⚡ 슬랙 웹훅 빠른 설정 가이드

## 🎯 5분 안에 완료하기

---

## 1️⃣ 슬랙 웹훅 URL 생성 (2분)

### 방법 1: 새 앱 생성 (추천)

1. **접속**: https://api.slack.com/messaging/webhooks

2. **앱 생성**:
   - "Create your Slack app" 클릭
   - "From scratch" 선택
   - App Name: `Naver Datalab Reporter`
   - Workspace 선택
   - "Create App" 클릭

3. **Webhook 활성화**:
   - 왼쪽 메뉴 "Incoming Webhooks" 클릭
   - "Activate Incoming Webhooks" 토글 ON
   - "Add New Webhook to Workspace" 클릭
   - 채널 선택: `#mlb-naver-datalab-reporter`
   - "Allow" 클릭

4. **URL 복사**: 
   ```
   https://hooks.slack.com/services/T.../B.../...
   ```

### 방법 2: 기존 앱 사용

1. **접속**: https://api.slack.com/apps

2. **앱 선택**: 기존 앱 클릭

3. **Incoming Webhooks** 페이지에서 URL 확인

---

## 2️⃣ GitHub Secrets 등록 (2분)

### 단계별 진행

1. **GitHub 저장소 접속**:
   ```
   https://github.com/yujinpung/mlb-naver-datalab-reporter/settings/secrets/actions
   ```

2. **"New repository secret" 클릭**

3. **정보 입력**:
   ```
   Name: SLACK_WEBHOOK_URL
   Secret: [복사한 Webhook URL 붙여넣기]
   ```

4. **"Add secret" 클릭**

5. **✅ 완료!**

---

## 3️⃣ 테스트 실행 (1분)

### GitHub Actions 수동 실행

1. **Actions 페이지 접속**:
   ```
   https://github.com/yujinpung/mlb-naver-datalab-reporter/actions
   ```

2. **"Daily Naver Datalab Report" 클릭**

3. **"Run workflow" 버튼 클릭**

4. **"Run workflow" 다시 클릭** (초록색 버튼)

5. **페이지 새로고침 (F5)**

6. **실행 항목 클릭하여 로그 확인**

---

## ✅ 성공 확인

### 1. GitHub Actions 로그

다음 메시지가 보이면 성공:

```
📤 STEP 3: 슬랙 전송
  키워드 'MLB' 전송 중...
  ✅ 'MLB' 전송 완료
  ...
✅ 슬랙 전송 완료: 8/8개
```

### 2. 슬랙 채널

`#mlb-naver-datalab-reporter` 채널에서 메시지 확인:

```
📊 네이버 검색 트렌드: MLB
[이미지]
```

8개 키워드 메시지가 모두 와야 합니다!

---

## 🐛 문제 해결

### ❌ "invalid_auth" 오류

**원인**: Webhook URL이 잘못되었거나 만료됨

**해결**:
1. Webhook URL 다시 확인
2. 새 Webhook URL 생성
3. GitHub Secrets 업데이트

---

### ❌ 슬랙 메시지가 안 옴

**원인**: Secret 이름이 잘못됨

**해결**:
1. Secret 이름이 정확히 `SLACK_WEBHOOK_URL`인지 확인 (대소문자 구분)
2. Secret 값에 전체 URL이 포함되어 있는지 확인
3. URL이 `https://hooks.slack.com/services/`로 시작하는지 확인

---

### ❌ 채널을 찾을 수 없음

**원인**: 채널이 존재하지 않음

**해결**:
1. 슬랙에서 `#mlb-naver-datalab-reporter` 채널 생성
2. Webhook을 해당 채널에 다시 연결

---

## 📸 스크린샷 가이드

### 1. Slack API - Webhook URL 생성 화면

```
┌─────────────────────────────────────────┐
│ Incoming Webhooks                       │
├─────────────────────────────────────────┤
│ ○ → ● Activate Incoming Webhooks        │
│                                         │
│ Webhook URLs for Your Workspace         │
│ ┌─────────────────────────────────────┐ │
│ │ https://hooks.slack.com/services/   │ │
│ │ T012345/B012345/XXXXXXXXXXXX        │ │
│ │                           [Copy]    │ │
│ └─────────────────────────────────────┘ │
│                                         │
│ [Add New Webhook to Workspace]          │
└─────────────────────────────────────────┘
```

### 2. GitHub Secrets 등록 화면

```
┌─────────────────────────────────────────┐
│ Actions secrets / New secret            │
├─────────────────────────────────────────┤
│ Name *                                  │
│ ┌─────────────────────────────────────┐ │
│ │ SLACK_WEBHOOK_URL                   │ │
│ └─────────────────────────────────────┘ │
│                                         │
│ Secret *                                │
│ ┌─────────────────────────────────────┐ │
│ │ https://hooks.slack.com/services/   │ │
│ │ T012345/B012345/XXXXXXXXXXXX        │ │
│ └─────────────────────────────────────┘ │
│                                         │
│              [Add secret]               │
└─────────────────────────────────────────┘
```

---

## 🔒 보안 주의사항

### ⚠️ Webhook URL 보안

- **절대 공개하지 마세요!**
- **GitHub에 커밋하지 마세요!**
- **`.env` 파일은 `.gitignore`에 포함됨**
- **GitHub Secrets만 사용하세요**

### 🔄 URL 재생성

필요시 언제든지 새 Webhook URL을 생성할 수 있습니다:
1. Slack API 페이지 → 앱 선택
2. Incoming Webhooks
3. 기존 URL 삭제 (선택)
4. "Add New Webhook to Workspace"

---

## 📞 추가 지원

더 자세한 정보가 필요하면:

- [`WEBHOOK_SETUP.md`](WEBHOOK_SETUP.md) - 기본 가이드
- [`WEBHOOK_SETUP_DETAILED.md`](WEBHOOK_SETUP_DETAILED.md) - 상세 가이드
- [`SLACK_TROUBLESHOOTING.md`](SLACK_TROUBLESHOOTING.md) - 문제 해결

---

## 🎉 완료!

설정이 완료되면:
- ✅ 매일 오전 9시 자동 실행
- ✅ 슬랙으로 8개 키워드 트렌드 수신
- ✅ 이미지 포함된 메시지 확인
- ✅ 대시보드 자동 업데이트

**지금 바로 GitHub Actions를 실행하여 테스트하세요!** 🚀


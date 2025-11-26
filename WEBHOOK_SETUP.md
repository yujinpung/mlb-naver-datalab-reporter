# 🔗 Slack Webhook 설정 가이드

Webhook 방식으로 슬랙 메시지를 전송하는 방법입니다.

---

## 📋 Webhook vs Bot Token

### Webhook 방식
- ✅ **설정 간단**: URL만 있으면 됨
- ✅ **이미지 URL 지원**: Firebase Storage URL 포함 가능
- ❌ **이미지 파일 직접 업로드 불가**: URL만 전송 가능
- ✅ **Bot 설치 불필요**: 채널에 Bot 추가할 필요 없음

### Bot Token 방식
- ✅ **이미지 파일 직접 업로드**: 파일을 직접 슬랙에 업로드
- ❌ **Bot 설치 필요**: 워크스페이스에 Bot 추가 필요
- ❌ **채널 초대 필요**: Bot을 채널에 초대해야 함

---

## 🚀 Webhook 설정 방법

### 1단계: Slack Webhook URL 생성

1. **Slack API 페이지 접속**
   ```
   https://api.slack.com/messaging/webhooks
   ```

2. **"Create your Slack app" 클릭** (또는 기존 앱 선택)

3. **"From scratch" 선택**

4. **앱 정보 입력**
   - **App Name**: `Naver Datalab Reporter` (또는 원하는 이름)
   - **Workspace**: 워크스페이스 선택

5. **"Create App" 클릭**

6. **"Incoming Webhooks" 활성화**
   - 왼쪽 메뉴에서 **"Incoming Webhooks"** 클릭
   - **"Activate Incoming Webhooks"** 토글을 **ON**으로 변경

7. **Webhook 생성**
   - **"Add New Webhook to Workspace"** 버튼 클릭
   - 채널 선택: `#mlb-naver-datalab-reporter` (또는 원하는 채널)
   - **"Allow"** 클릭

8. **Webhook URL 복사**
   - 생성된 Webhook URL 복사
   - 형식: `https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX`

---

### 2단계: GitHub Secrets 등록

1. **GitHub 저장소 접속**
   ```
   https://github.com/yujinpung/mlb-naver-datalab-reporter
   ```

2. **Settings → Secrets and variables → Actions**

3. **SLACK_WEBHOOK_URL Secret 추가**
   ```
   Name: SLACK_WEBHOOK_URL
   Secret: https://hooks.slack.com/services/YOUR/WEBHOOK/URL
   ```

4. **"Add secret" 클릭**

---

### 3단계: Firebase Storage 설정 (이미지 전송용)

Webhook은 이미지 파일을 직접 업로드할 수 없으므로, **Firebase Storage에 이미지를 업로드한 후 URL을 전송**합니다.

#### Firebase Storage가 이미 설정되어 있다면
- 자동으로 이미지가 업로드되고 URL이 슬랙 메시지에 포함됩니다.

#### Firebase Storage가 없다면
1. **Firebase 프로젝트 생성** (이미 있으면 스킵)
2. **Storage 활성화**
3. **GitHub Secrets에 Firebase 설정 추가**:
   - `FIREBASE_STORAGE_BUCKET`
   - `FIREBASE_CREDENTIALS_JSON`
   - `FIREBASE_PROJECT_ID`
   - `FIREBASE_SERVICE_ACCOUNT`

자세한 방법은 [`FIREBASE_SETUP.md`](FIREBASE_SETUP.md) 참고

---

## 🔄 작동 방식

### Webhook + Firebase Storage 사용 시

```
1. 스크린샷 생성
   ↓
2. Firebase Storage에 업로드 → 공개 URL 생성
   ↓
3. Webhook으로 이미지 URL 포함 메시지 전송
   ↓
4. 슬랙에서 이미지 표시 ✅
```

### Webhook만 사용 시 (Firebase 없음)

```
1. 스크린샷 생성
   ↓
2. Webhook으로 텍스트 메시지만 전송
   ↓
3. 이미지 없음 ⚠️
```

---

## ✅ 테스트

### GitHub Actions에서 테스트

1. **Actions 탭 → "Daily Naver Datalab Report" 클릭**
2. **"Run workflow" 버튼 클릭**
3. **실행 로그 확인**
   - "STEP 2: Firebase Storage 업로드" 성공 확인
   - "STEP 3: 슬랙 전송" 성공 확인
4. **슬랙 채널 확인**
   - `#mlb-naver-datalab-reporter` 채널에서 메시지 수신 확인
   - 이미지가 표시되는지 확인

---

## 🔍 문제 해결

### ❌ 이미지가 표시되지 않음

**원인**: Firebase Storage 업로드 실패 또는 URL 오류

**해결 방법**:
1. Firebase Storage 설정 확인
2. GitHub Secrets의 `FIREBASE_STORAGE_BUCKET` 확인
3. 로그에서 Firebase 업로드 오류 확인

### ❌ 메시지가 전송되지 않음

**원인**: Webhook URL 오류

**해결 방법**:
1. GitHub Secrets의 `SLACK_WEBHOOK_URL` 확인
2. Webhook URL이 올바른지 확인
3. 채널이 올바른지 확인

### ❌ "invalid_payload" 오류

**원인**: 메시지 형식 오류

**해결 방법**:
1. 로그 확인
2. 코드의 메시지 블록 형식 확인

---

## 📝 체크리스트

- [ ] Slack Webhook URL 생성
- [ ] GitHub Secrets에 `SLACK_WEBHOOK_URL` 등록
- [ ] Firebase Storage 설정 (이미지 전송용)
- [ ] GitHub Actions 테스트 실행
- [ ] 슬랙 채널에서 메시지 수신 확인
- [ ] 이미지가 표시되는지 확인

---

## 💡 참고사항

### Webhook URL 보안

- **절대 공개하지 마세요!**
- GitHub Secrets에만 저장
- `.env` 파일은 `.gitignore`에 추가되어 있습니다

### 이미지 전송 방법 선택

| 방법 | 이미지 전송 | 설정 난이도 |
|------|------------|------------|
| **Webhook + Firebase** | ✅ URL 포함 | 중간 |
| **Bot Token** | ✅ 파일 직접 업로드 | 어려움 |
| **Webhook만** | ❌ 텍스트만 | 쉬움 |

---

## 🎯 권장 설정

**이미지를 전송하려면:**
1. ✅ **Webhook URL** 설정 (필수)
2. ✅ **Firebase Storage** 설정 (이미지 URL 생성용)

이렇게 하면 Bot Token 없이도 이미지를 포함한 메시지를 전송할 수 있습니다!


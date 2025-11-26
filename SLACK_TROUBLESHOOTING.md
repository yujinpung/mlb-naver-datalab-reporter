# 🔍 슬랙 메시지 미수신 문제 해결 가이드

슬랙 메시지가 오지 않는 문제를 진단하고 해결하는 방법입니다.

---

## 📋 체크리스트

먼저 다음 항목들을 확인하세요:

- [ ] GitHub Secrets에 `SLACK_WEBHOOK_URL` 등록됨
- [ ] GitHub Actions 워크플로우 실행 성공
- [ ] 워크플로우 로그에서 "✅ 슬랙 전송 완료" 메시지 확인
- [ ] 슬랙 채널에서 메시지 확인

---

## 🔍 문제 진단

### 1단계: GitHub Actions 로그 확인

1. **GitHub 저장소 → Actions 탭**
2. **최신 실행 클릭**
3. **"Run Datalab Report" 단계 클릭**
4. **로그에서 다음 메시지 확인**:
   - `📤 STEP 3: 슬랙 전송`
   - `✅ 슬랙 전송 완료: X/8개`
   - 또는 오류 메시지

---

### 2단계: 가능한 오류 메시지 확인

#### ❌ "SLACK_WEBHOOK_URL 또는 SLACK_BOT_TOKEN이 설정되어야 합니다"

**원인**: GitHub Secrets에 Webhook URL 또는 Bot Token이 등록되지 않음

**해결 방법**:
1. GitHub 저장소 → Settings → Secrets and variables → Actions
2. `SLACK_WEBHOOK_URL` 또는 `SLACK_BOT_TOKEN` 확인
3. 없다면 추가:
   - `SLACK_WEBHOOK_URL`: Webhook URL
   - 또는 `SLACK_BOT_TOKEN`: Bot Token

---

#### ❌ "Webhook URL이 없어 메시지 전송 불가"

**원인**: `SLACK_WEBHOOK_URL`이 비어있거나 잘못됨

**해결 방법**:
1. GitHub Secrets의 `SLACK_WEBHOOK_URL` 확인
2. Webhook URL이 올바른지 확인
3. Slack API 페이지에서 Webhook URL 재생성

---

#### ❌ "슬랙 전송 완료: 0/8개"

**원인**: 모든 메시지 전송 실패

**해결 방법**:
1. 로그에서 각 키워드별 오류 메시지 확인
2. Webhook URL 유효성 확인
3. Firebase Storage 설정 확인 (이미지 전송 시)

---

#### ❌ "⚠️ 이미지 URL 없음 (텍스트만 전송)"

**원인**: Firebase Storage 업로드 실패

**해결 방법**:
1. Firebase Storage 설정 확인
2. GitHub Secrets의 Firebase 관련 Secrets 확인
3. 로그에서 Firebase 업로드 오류 확인

---

## 🛠️ 해결 방법

### 방법 1: Webhook URL 확인 및 재등록

1. **Slack API 페이지 접속**
   ```
   https://api.slack.com/apps
   ```

2. **앱 선택 → Incoming Webhooks**

3. **Webhook URL 확인 또는 재생성**

4. **GitHub Secrets 업데이트**
   - Settings → Secrets and variables → Actions
   - `SLACK_WEBHOOK_URL` 업데이트

---

### 방법 2: GitHub Actions 재실행

1. **Actions 탭 → "Daily Naver Datalab Report" 클릭**

2. **"Run workflow" 버튼 클릭**

3. **실행 로그 확인**

4. **슬랙 채널 확인**

---

### 방법 3: 로컬에서 테스트

```bash
# 환경변수 설정 (테스트용)
export SLACK_WEBHOOK_URL="your-webhook-url"
export SLACK_CHANNEL="#mlb-naver-datalab-reporter"

# 진단 스크립트 실행
python diagnose_slack.py
```

---

## 📊 일반적인 문제와 해결책

### 문제 1: Webhook URL이 등록되지 않음

**증상**: 로그에 "SLACK_WEBHOOK_URL 또는 SLACK_BOT_TOKEN이 설정되어야 합니다" 오류

**해결**:
1. GitHub Secrets에 `SLACK_WEBHOOK_URL` 등록
2. Webhook URL 생성 방법: [`WEBHOOK_SETUP.md`](WEBHOOK_SETUP.md) 참고

---

### 문제 2: Webhook URL이 잘못됨

**증상**: 로그에 "invalid_payload" 또는 "Webhook URL이 없어 메시지 전송 불가" 오류

**해결**:
1. Slack API 페이지에서 Webhook URL 확인
2. Webhook URL 재생성
3. GitHub Secrets 업데이트

---

### 문제 3: Firebase Storage 설정 없음

**증상**: 로그에 "⚠️ 이미지 URL 없음 (텍스트만 전송)" 메시지

**해결**:
1. Firebase Storage 설정 (이미지 전송용)
2. GitHub Secrets에 Firebase 관련 Secrets 등록
3. 자세한 방법: [`FIREBASE_SETUP.md`](FIREBASE_SETUP.md) 참고

---

### 문제 4: 워크플로우 실행 실패

**증상**: 워크플로우가 실패하여 슬랙 전송 단계에 도달하지 못함

**해결**:
1. 워크플로우 로그 확인
2. 오류 메시지 확인
3. 문제 해결 후 재실행

---

## 🔍 상세 진단

### GitHub Actions 로그에서 확인할 항목

1. **"Run Datalab Report" 단계**:
   - `📤 STEP 3: 슬랙 전송` 메시지 확인
   - 각 키워드별 전송 결과 확인
   - `✅ 슬랙 전송 완료: X/8개` 확인

2. **오류 메시지**:
   - `❌ 슬랙 전송 실패: ...` 확인
   - `⚠️  '키워드' 전송 실패: ...` 확인

3. **Firebase Storage 업로드**:
   - `☁️  STEP 2: Firebase Storage 업로드` 확인
   - `✅ Firebase Storage 업로드 완료` 확인

---

## ✅ 성공 확인

다음이 모두 확인되면 성공입니다:

- [ ] GitHub Actions 실행 성공 (초록색 체크)
- [ ] 로그에 "✅ 슬랙 전송 완료: 8/8개" 메시지
- [ ] 슬랙 채널에서 메시지 수신 확인
- [ ] 이미지가 표시되는지 확인 (Firebase Storage 설정 시)

---

## 💡 추가 도움말

### 로그 확인 방법

1. **GitHub Actions 페이지 접속**
2. **최신 실행 클릭**
3. **각 단계 클릭하여 로그 확인**
4. **오류 메시지 복사하여 검색**

### 지원 문서

- [`WEBHOOK_SETUP.md`](WEBHOOK_SETUP.md): Webhook 설정 가이드
- [`WEBHOOK_SETUP_DETAILED.md`](WEBHOOK_SETUP_DETAILED.md): 상세 Webhook 설정 가이드
- [`FIREBASE_SETUP.md`](FIREBASE_SETUP.md): Firebase Storage 설정 가이드
- [`SLACK_FIX_GUIDE.md`](SLACK_FIX_GUIDE.md): 슬랙 문제 해결 가이드

---

## 🆘 여전히 해결되지 않으면

1. **GitHub Actions 로그 전체 복사**
2. **오류 메시지 확인**
3. **슬랙 채널 설정 확인**
4. **Webhook URL 재생성**

문제가 계속되면 로그를 공유해주시면 추가로 도와드리겠습니다.



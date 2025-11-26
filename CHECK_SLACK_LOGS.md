# 🔍 슬랙 전송 로그 확인 방법

## GitHub Actions 로그에서 확인할 내용

### 1단계: 실행 로그 열기

1. GitHub Actions 페이지 접속:
   ```
   https://github.com/yujinpung/mlb-naver-datalab-reporter/actions
   ```

2. 가장 최근 실행 (초록색 체크) 클릭

3. "datalab-report" Job 클릭

### 2단계: "Run Datalab Report" 단계 확인

"Run Datalab Report" 단계를 펼쳐서 다음 메시지를 찾으세요:

```
📤 STEP 3: 슬랙 전송

  키워드 'MLB' 전송 중...
  ✅ 'MLB' 전송 완료
  
또는

  키워드 'MLB' 전송 중...
  ❌ 슬랙 API 오류: [오류 메시지]
```

### 3단계: 확인할 포인트

#### ✅ 성공 시 로그:
```
🔗 STEP 2-2: GitHub Raw URL 생성
   - MLB: https://raw.githubusercontent.com/.../MLB.png
   - MLB키즈: https://raw.githubusercontent.com/.../MLB키즈.png
   ... (8개)
✅ GitHub Raw URL 생성 완료: 8개

📤 STEP 3: 슬랙 전송
  키워드 'MLB' 전송 중...
  ✅ 'MLB' 전송 완료
  ... (8개 키워드 모두)
✅ 슬랙 전송 완료: 8/8개
```

#### ❌ 실패 시 로그:
```
📤 STEP 3: 슬랙 전송
  키워드 'MLB' 전송 중...
  ❌ 슬랙 API 오류: invalid_auth
또는
  ❌ 슬랙 API 오류: channel_not_found
```

---

## 가능한 원인과 해결

### 원인 1: SLACK_WEBHOOK_URL이 설정되지 않음

**확인 방법**:
로그에서 다음 메시지가 있는지 확인:
```
⚠️ Webhook 방식 사용 시 이미지 URL이 필요합니다.
```

**해결 방법**:
1. GitHub Secrets 확인:
   ```
   https://github.com/yujinpung/mlb-naver-datalab-reporter/settings/secrets/actions
   ```
2. `SLACK_WEBHOOK_URL`이 있는지 확인
3. 없다면 다시 추가

---

### 원인 2: Webhook URL이 잘못됨

**확인 방법**:
로그에서 다음 메시지가 있는지 확인:
```
❌ 슬랙 API 오류: invalid_auth
```

**해결 방법**:
1. Slack에서 Webhook URL 다시 생성
2. GitHub Secrets 업데이트

---

### 원인 3: 슬랙 채널 문제

**확인 방법**:
로그에서 다음 메시지가 있는지 확인:
```
❌ 슬랙 API 오류: channel_not_found
```

**해결 방법**:
1. 슬랙에서 `#mlb-naver-datalab-reporter` 채널이 있는지 확인
2. Webhook을 올바른 채널에 연결했는지 확인

---

## 빠른 진단 명령

로그에서 다음 키워드를 검색하세요:

1. **"STEP 3: 슬랙 전송"** - 슬랙 전송 시작 확인
2. **"슬랙 전송 완료"** - 성공 여부 확인
3. **"슬랙 API 오류"** - 오류 메시지 확인
4. **"invalid_auth"** - 인증 오류
5. **"channel_not_found"** - 채널 오류

---

## 로그 예시

### 성공 예시:
```
2025-11-26 09:00:15 - INFO - 📤 STEP 3: 슬랙 전송
2025-11-26 09:00:15 - INFO - 
  키워드 'MLB' 전송 중...
2025-11-26 09:00:16 - INFO -   ✅ 'MLB' 전송 완료
2025-11-26 09:00:17 - INFO - 
  키워드 'MLB키즈' 전송 중...
2025-11-26 09:00:18 - INFO -   ✅ 'MLB키즈' 전송 완료
...
2025-11-26 09:00:30 - INFO - ✅ 슬랙 전송 완료: 8/8개
```

### 실패 예시 (Webhook URL 없음):
```
2025-11-26 09:00:15 - INFO - 📤 STEP 3: 슬랙 전송
2025-11-26 09:00:15 - ERROR - ValueError: SLACK_WEBHOOK_URL 또는 SLACK_BOT_TOKEN이 설정되어야 합니다.
```

### 실패 예시 (인증 오류):
```
2025-11-26 09:00:15 - INFO - 📤 STEP 3: 슬랙 전송
2025-11-26 09:00:15 - INFO - 
  키워드 'MLB' 전송 중...
2025-11-26 09:00:16 - ERROR - ❌ 슬랙 API 오류: invalid_auth
```


# 🔧 슬랙 전송 문제 해결 가이드

## ❌ 현재 문제

GitHub Actions에서 슬랙 메시지가 전송되지 않는 이유:
- **Bot Token이 비활성화됨** (`account_inactive` 오류)

---

## ✅ 해결 방법

### 1단계: Slack 앱 재설치

1. **Slack API 페이지 접속**
   ```
   https://api.slack.com/apps
   ```

2. **앱 선택**
   - 이전에 생성한 앱 클릭

3. **OAuth & Permissions 탭 클릭**

4. **"Reinstall to Workspace" 버튼 클릭**
   - 또는 "Install to Workspace" 버튼이 보이면 클릭

5. **"Allow" 클릭**

6. **새 Bot Token 복사**
   - "Bot User OAuth Token" 섹션에서 새 토큰 복사
   - 형식: `xoxb-...`

---

### 2단계: GitHub Secrets 업데이트

1. **GitHub 저장소 접속**
   ```
   https://github.com/yujinpung/mlb-naver-datalab-reporter
   ```

2. **Settings → Secrets and variables → Actions**

3. **SLACK_BOT_TOKEN Secret 찾기**

4. **"Update" 버튼 클릭**

5. **새 토큰 붙여넣기**
   ```
   Value: xoxb-새로운-토큰-여기에-붙여넣기
   ```

6. **"Update secret" 클릭**

---

### 3단계: 채널 확인

1. **Slack 워크스페이스 접속**

2. **#mlb-naver-datalab-reporter 채널 열기**

3. **Bot이 채널에 있는지 확인**
   - 채널 멤버 목록에서 Bot 확인
   - 없다면 Bot을 채널에 초대:
     ```
     /invite @[Bot이름]
     ```

---

### 4단계: 테스트 실행

1. **GitHub Actions 페이지 접속**
   ```
   https://github.com/yujinpung/mlb-naver-datalab-reporter/actions
   ```

2. **"Daily Naver Datalab Report" 워크플로우 클릭**

3. **"Run workflow" 버튼 클릭**

4. **실행 상태 확인**
   - "Run Datalab Report" 단계 로그 확인
   - 슬랙 전송 성공 메시지 확인

5. **슬랙 채널 확인**
   - `#mlb-naver-datalab-reporter` 채널에서 이미지 수신 확인

---

## 🔍 문제 진단

### 로컬에서 테스트

```bash
python check_slack_issue.py
```

이 스크립트는 다음을 확인합니다:
- ✅ Bot Token 유효성
- ✅ 채널 접근 권한
- ✅ Bot이 채널 멤버인지
- ✅ 테스트 메시지 전송

---

## ⚠️ 주의사항

1. **Bot Token은 절대 공개하지 마세요**
   - GitHub에 커밋하지 마세요
   - `.env` 파일은 `.gitignore`에 추가되어 있습니다

2. **채널에 Bot 초대 필수**
   - Bot이 채널 멤버가 아니면 메시지를 보낼 수 없습니다

3. **Bot 권한 확인**
   - `chat:write` 권한 필요
   - `files:write` 권한 필요 (이미지 업로드용)

---

## 📝 체크리스트

- [ ] Slack 앱 재설치 완료
- [ ] 새 Bot Token 복사
- [ ] GitHub Secrets 업데이트
- [ ] Bot이 채널 멤버인지 확인
- [ ] GitHub Actions 테스트 실행
- [ ] 슬랙 채널에서 메시지 수신 확인

---

## 💡 추가 도움말

### Bot Token이 계속 비활성화되는 경우

1. **앱이 워크스페이스에서 제거되었는지 확인**
2. **앱 권한이 변경되었는지 확인**
3. **새 앱을 생성하여 다시 시작**

### 채널을 찾을 수 없는 경우

1. **채널 이름 확인** (`#mlb-naver-datalab-reporter`)
2. **채널이 공개 채널인지 확인**
3. **Bot이 워크스페이스에 설치되어 있는지 확인**


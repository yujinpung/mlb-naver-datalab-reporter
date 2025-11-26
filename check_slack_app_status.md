# Slack 앱 상태 확인 가이드

## 🔍 1단계: 앱 목록 확인

1. **Slack API 페이지 접속**
   ```
   https://api.slack.com/apps
   ```

2. **앱 목록 확인**
   - 이전에 생성한 앱이 목록에 있는지 확인
   - 앱이 없다면 → **앱이 삭제됨** (새로 생성 필요)

---

## 🔍 2단계: 앱 상태 확인

앱을 클릭하여 상세 페이지로 이동:

### A. "Basic Information" 탭
- **App Status**: Active인지 확인
- **App ID**: 앱 ID 확인

### B. "OAuth & Permissions" 탭
- **Bot User OAuth Token** 섹션 확인
  - 토큰이 표시되는지 확인
  - "Revoke" 버튼이 있는지 확인 (Revoke되면 비활성화됨)
  
- **"Install to Workspace"** 또는 **"Reinstall to Workspace"** 버튼 확인
  - 버튼이 보이면 → 앱이 워크스페이스에서 제거됨
  - 버튼이 없고 토큰만 보이면 → 정상 상태

### C. "App Home" 탭
- **Bot User** 섹션 확인
- Bot이 활성화되어 있는지 확인

---

## 🔍 3단계: 워크스페이스에서 확인

1. **Slack 워크스페이스 접속**
2. **앱 관리 페이지 접속**
   - 워크스페이스 설정 → "Manage apps"
3. **앱 목록 확인**
   - 해당 앱이 목록에 있는지 확인
   - 없다면 → 워크스페이스에서 제거됨

---

## 💡 가장 흔한 원인

### 1. 앱이 워크스페이스에서 제거됨 (90% 확률)
- **증상**: `account_inactive` 오류
- **원인**: 누군가 앱을 제거했거나, 앱 설정 변경 후 재설치 필요
- **해결**: "Reinstall to Workspace" 클릭

### 2. 토큰이 Revoke됨
- **증상**: `account_inactive` 오류
- **원인**: 토큰이 수동으로 취소됨
- **해결**: 새 토큰 생성 또는 앱 재설치

### 3. 앱이 삭제됨
- **증상**: 앱 목록에 없음
- **원인**: 앱이 완전히 삭제됨
- **해결**: 새 앱 생성

---

## ✅ 빠른 해결 방법

대부분의 경우 다음 단계로 해결됩니다:

1. **https://api.slack.com/apps** 접속
2. **앱 선택**
3. **"OAuth & Permissions"** 탭 클릭
4. **"Reinstall to Workspace"** 버튼 클릭 (있다면)
5. **새 Bot Token 복사**
6. **`.env` 파일 업데이트**

---

## 🔐 보안 참고사항

- Bot Token은 **절대 공개하지 마세요**
- GitHub에 커밋하지 마세요 (`.gitignore`에 `.env` 추가)
- 토큰이 노출되면 즉시 Revoke하고 새로 생성하세요


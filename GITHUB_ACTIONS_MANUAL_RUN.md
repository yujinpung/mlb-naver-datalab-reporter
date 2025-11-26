# 🚀 GitHub Actions 수동 실행 가이드

## 📋 수동 실행 방법

### 1단계: GitHub Actions 페이지 접속

1. **GitHub 저장소 접속**
   ```
   https://github.com/yujinpung/mlb-naver-datalab-reporter
   ```

2. **상단 메뉴에서 "Actions" 탭 클릭**

---

### 2단계: 워크플로우 선택

1. **왼쪽 사이드바에서 "Daily Naver Datalab Report" 클릭**

2. **오른쪽 상단의 "Run workflow" 버튼 클릭**

---

### 3단계: 워크플로우 실행

1. **"Use workflow from" 드롭다운에서 "Branch: main" 선택**

2. **초록색 "Run workflow" 버튼 클릭**

3. **실행 시작!** 🎉

---

### 4단계: 실행 로그 확인

1. **페이지 새로고침 (F5)**

2. **최상단에 노란색 점 🟡 표시된 실행 항목 클릭**
   - 실행 중: 🟡 노란색
   - 성공: ✅ 초록색
   - 실패: ❌ 빨간색

3. **"Run Datalab Report" 단계 클릭하여 로그 확인**

---

### 5단계: 슬랙 채널 확인

1. **슬랙 앱 또는 웹 접속**

2. **`#mlb-naver-datalab-reporter` 채널 확인**

3. **8개 키워드 메시지 및 이미지 확인** ✅

---

## 🔍 확인할 로그 메시지

### ✅ 성공 시 보이는 로그

```
🔗 STEP 2-2: GitHub Raw URL 생성
   - MLB: https://raw.githubusercontent.com/.../NaverDatalab_2025-11-25_MLB.png
   - MLB키즈: https://raw.githubusercontent.com/.../NaverDatalab_2025-11-25_MLB키즈.png
   ...
✅ GitHub Raw URL 생성 완료: 8개

📤 STEP 3: 슬랙 전송
  키워드 'MLB' 전송 중...
  ✅ 'MLB' 전송 완료
  
  키워드 'MLB키즈' 전송 중...
  ✅ 'MLB키즈' 전송 완료
  
  ... (8개 키워드 모두)
  
✅ 슬랙 전송 완료: 8/8개
```

---

## ❌ 문제 해결

### 워크플로우가 보이지 않음

**원인**: 워크플로우 파일이 제대로 푸시되지 않음

**해결**:
1. `.github/workflows/daily.yml` 파일 확인
2. GitHub에 파일이 있는지 확인
3. 파일 이름 및 경로 확인

---

### "Run workflow" 버튼이 보이지 않음

**원인**: 워크플로우에 `workflow_dispatch` 트리거가 없음

**해결**:
- `.github/workflows/daily.yml` 파일에 다음이 있는지 확인:
```yaml
on:
  workflow_dispatch:  # 수동 실행 허용
```

---

### 슬랙 메시지가 안 옴

**원인**: `SLACK_WEBHOOK_URL` Secret이 설정되지 않음

**해결**:
1. Settings → Secrets and variables → Actions
2. `SLACK_WEBHOOK_URL` Secret 확인
3. 없다면 추가: [`WEBHOOK_SETUP.md`](WEBHOOK_SETUP.md) 참고

---

## 📊 실행 시간

- **예상 실행 시간**: 약 3-5분
  - 스크린샷 캡처: 2-3분
  - GitHub Raw URL 생성: 즉시
  - 슬랙 전송: 8초 (키워드당 1초)
  - GitHub Pages 배포: 1-2분

---

## 🎯 성공 확인

다음이 모두 확인되면 성공입니다:

- [ ] GitHub Actions 실행 성공 (✅ 초록색)
- [ ] 로그에 "✅ 슬랙 전송 완료: 8/8개" 메시지
- [ ] 슬랙 채널에서 8개 메시지 수신
- [ ] 슬랙 메시지에 이미지 표시
- [ ] 대시보드 업데이트 확인

---

## 💡 참고사항

### 수동 실행 시 주의사항

- **실행 횟수 제한**: GitHub Actions는 무료 계정에서 월 2,000분 제공
- **동시 실행 제한**: 같은 워크플로우를 동시에 여러 번 실행할 수 없음
- **로그 보관**: 실행 로그는 90일간 보관됨

---

## 🔄 자동 실행 확인

### 자동 실행 스케줄

- **실행 주기**: 매일 오전 9시 (한국 시간 기준)
- **Cron 표현식**: `0 0 * * *` (UTC 00:00 = KST 09:00)

### 다음 자동 실행 시간 확인

워크플로우 페이지에서 "Next scheduled run" 확인

---

## 📞 추가 지원

문제가 발생하면 다음 문서를 참고하세요:

- [`SLACK_TROUBLESHOOTING.md`](SLACK_TROUBLESHOOTING.md): 슬랙 문제 해결
- [`WEBHOOK_GITHUB_URL.md`](WEBHOOK_GITHUB_URL.md): GitHub Raw URL 가이드
- [`GITHUB_SETUP.md`](GITHUB_SETUP.md): GitHub Actions 설정

---

**현재 상태**: 스크린샷이 GitHub에 업로드되었으므로, 지금 바로 실행하면 슬랙으로 이미지가 전송됩니다! 🎉


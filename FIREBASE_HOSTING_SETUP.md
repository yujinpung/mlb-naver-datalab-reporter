# 🔥 Firebase Hosting 설정 가이드

## 📋 개요

GitHub에 저장된 스크린샷을 Firebase Hosting에서 호스팅하는 방법입니다.

---

## 🎯 작동 방식

```
1. GitHub Actions 실행
   ↓
2. 스크린샷 캡처 → GitHub 저장
   ↓
3. dashboard.html 생성
   - GitHub Raw URL 사용
   - 이미지 경로: https://raw.githubusercontent.com/.../screenshots/...
   ↓
4. Firebase Hosting 배포
   - public/index.html로 배포
   ↓
5. Firebase URL로 접속 가능
```

---

## 🚀 설정 단계

### 1단계: Firebase 프로젝트 생성 (완료)

✅ 이미 생성됨: `mlb-datalab-reporter`

---

### 2단계: Firebase Service Account 생성

1. **Firebase Console 접속**:
   ```
   https://console.firebase.google.com/project/mlb-datalab-reporter/settings/serviceaccounts/adminsdk
   ```

2. **새 비공개 키 생성**:
   - "Generate new private key" 버튼 클릭
   - JSON 파일 다운로드

3. **JSON 파일 내용 복사**:
   ```json
   {
     "type": "service_account",
     "project_id": "mlb-datalab-reporter",
     "private_key_id": "...",
     "private_key": "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n",
     "client_email": "...",
     ...
   }
   ```

---

### 3단계: GitHub Secrets 등록

1. **GitHub 저장소 → Settings → Secrets and variables → Actions**

2. **FIREBASE_SERVICE_ACCOUNT 추가**:
   ```
   Name: FIREBASE_SERVICE_ACCOUNT
   Secret: [JSON 파일 전체 내용 붙여넣기]
   ```

3. **완료!**

---

## 📁 파일 구조

```
projectpung/
├── dashboard.html              # 원본 파일
├── public/
│   └── index.html             # Firebase Hosting용 (dashboard.html 복사본)
├── firebase.json              # Firebase 설정
├── .firebaserc                # Firebase 프로젝트 설정
└── .github/workflows/
    └── daily.yml              # GitHub Actions 워크플로우
```

---

## 🔗 이미지 경로

### GitHub Raw URL 사용

```javascript
const screenshotsPath = 'https://raw.githubusercontent.com/yujinpung/mlb-naver-datalab-reporter/main/screenshots/';
```

**장점**:
- ✅ Firebase Hosting에 이미지 업로드 불필요
- ✅ GitHub에 저장된 이미지 직접 사용
- ✅ 배포 속도 빠름
- ✅ 완전 무료

---

## 🌐 배포 URL

배포 완료 후 다음 URL로 접속 가능:

```
https://mlb-datalab-reporter.web.app
또는
https://mlb-datalab-reporter.firebaseapp.com
```

---

## ✅ GitHub Actions 워크플로우

### 배포 흐름

```yaml
# 9. Firebase Hosting용 public 폴더 준비
- name: Prepare public folder for Firebase Hosting
  run: |
    mkdir -p public
    cp dashboard.html public/index.html

# 10. Firebase Hosting에 배포
- name: Deploy to Firebase Hosting
  uses: FirebaseExtended/action-hosting-deploy@v0
  with:
    firebaseServiceAccount: '${{ secrets.FIREBASE_SERVICE_ACCOUNT }}'
    channelId: live
    projectId: mlb-datalab-reporter
```

---

## 🔧 Firebase 설정 파일

### firebase.json

```json
{
  "hosting": {
    "public": "public",
    "ignore": [
      "firebase.json",
      "**/.*",
      "**/node_modules/**"
    ],
    "rewrites": [
      {
        "source": "**",
        "destination": "/index.html"
      }
    ]
  }
}
```

### .firebaserc

```json
{
  "projects": {
    "default": "mlb-datalab-reporter"
  }
}
```

---

## 🐛 문제 해결

### ❌ "Permission denied" 오류

**원인**: Firebase Service Account JSON이 잘못됨

**해결**:
1. Firebase Console에서 새 Service Account 생성
2. JSON 파일 전체 내용 복사
3. GitHub Secrets 업데이트

---

### ❌ "Project not found" 오류

**원인**: 프로젝트 ID가 잘못됨

**해결**:
1. `.firebaserc` 파일에서 프로젝트 ID 확인
2. Firebase Console에서 프로젝트 ID 확인
3. 워크플로우의 `projectId` 수정

---

### ❌ 이미지가 표시되지 않음

**원인**: GitHub Raw URL이 아직 활성화되지 않음

**해결**:
1. 5-10분 대기 (GitHub Raw URL 캐싱 시간)
2. 브라우저에서 이미지 URL 직접 접속 테스트
3. 페이지 강제 새로고침 (Ctrl+F5)

---

## 📊 비용

### Firebase Hosting 무료 티어

- ✅ 저장 용량: 10GB
- ✅ 전송량: 360MB/일
- ✅ 커스텀 도메인: 무제한
- ✅ SSL 인증서: 자동 제공

**현재 프로젝트**:
- HTML 파일: ~10KB
- 이미지: GitHub에서 직접 로드 (Firebase 용량 사용 안 함)
- 예상 사용량: < 1MB/일

→ **완전 무료!** 💰

---

## 🎯 최종 체크리스트

- [ ] Firebase 프로젝트 생성 완료
- [ ] Firebase Service Account JSON 생성 완료
- [ ] GitHub Secrets에 `FIREBASE_SERVICE_ACCOUNT` 등록 완료
- [ ] `firebase.json` 파일 확인
- [ ] `.firebaserc` 파일 확인
- [ ] `dashboard.html`에 GitHub Raw URL 설정 완료
- [ ] GitHub Actions 워크플로우 수정 완료
- [ ] GitHub Actions 실행 및 배포 완료
- [ ] Firebase URL 접속 확인

---

## 🚀 다음 단계

1. **Firebase Service Account JSON 생성**
2. **GitHub Secrets 등록**
3. **GitHub Actions 실행**
4. **Firebase URL 접속 확인**

---

## 💡 참고

### Firebase CLI로 로컬 테스트 (선택사항)

```bash
# Firebase CLI 설치
npm install -g firebase-tools

# Firebase 로그인
firebase login

# 로컬 서버 실행
firebase serve

# 접속: http://localhost:5000
```

---

**설정이 완료되면 매일 오전 9시에 자동으로 배포됩니다!** 🎉


# 🔥 Firebase 설정 가이드

Firebase Hosting과 Storage를 사용하여 대시보드를 배포하고 스크린샷을 저장하는 방법입니다.

---

## 📋 목차

1. [Firebase 프로젝트 생성](#1-firebase-프로젝트-생성)
2. [Firebase 인증 설정](#2-firebase-인증-설정)
3. [GitHub Secrets 등록](#3-github-secrets-등록)
4. [로컬 테스트](#4-로컬-테스트)
5. [배포 확인](#5-배포-확인)

---

## 1️⃣ Firebase 프로젝트 생성

### 1-1. Firebase Console 접속

1. **Firebase Console 접속**: https://console.firebase.google.com
2. **Google 계정으로 로그인**

### 1-2. 새 프로젝트 생성

1. **"프로젝트 추가"** 또는 **"Add project"** 클릭
2. **프로젝트 이름 입력**: `mlb-datalab-reporter` (또는 원하는 이름)
3. **Google Analytics 설정** (선택사항):
   - 사용 안 함 선택 가능
   - 또는 사용함 선택
4. **"프로젝트 만들기"** 클릭
5. 생성 완료까지 몇 초 대기

### 1-3. Firebase 서비스 활성화

#### Hosting 활성화

1. 왼쪽 메뉴에서 **"Hosting"** 클릭
2. **"시작하기"** 또는 **"Get started"** 클릭
3. 단계별 안내는 나중에 진행 (지금은 건너뛰기)

#### Storage 활성화

1. 왼쪽 메뉴에서 **"Storage"** 클릭
2. **"시작하기"** 클릭
3. **"프로덕션 모드로 시작"** 선택
4. **위치 선택**: `asia-northeast3` (서울) 또는 원하는 지역
5. **"완료"** 클릭

---

## 2️⃣ Firebase 인증 설정

### 2-1. 서비스 계정 키 생성

1. **프로젝트 설정** 접속:
   - Firebase Console → 프로젝트 설정 (톱니바퀴 아이콘)
   - 또는 https://console.firebase.google.com/project/[프로젝트ID]/settings/serviceaccounts/adminsdk

2. **서비스 계정** 탭 클릭

3. **"새 비공개 키 생성"** 또는 **"Generate new private key"** 클릭

4. **경고 확인**: "생성" 클릭

5. **JSON 파일 다운로드**: `[프로젝트ID]-[랜덤문자].json`

6. **파일 내용 복사**: 나중에 GitHub Secrets에 등록

> ⚠️ **중요**: 이 파일은 한 번만 다운로드 가능합니다. 안전하게 보관하세요!

---

### 2-2. Storage 버킷 이름 확인

1. **Storage** 페이지 접속
2. **"파일"** 탭에서 URL 확인:
   ```
   gs://[프로젝트ID].appspot.com
   ```
   또는
   ```
   [프로젝트ID].appspot.com
   ```

3. **버킷 이름 복사**: 예) `mlb-datalab-reporter.appspot.com`

---

### 2-3. 프로젝트 ID 확인

1. **프로젝트 설정** → **일반** 탭
2. **프로젝트 ID** 확인 및 복사

---

## 3️⃣ GitHub Secrets 등록

### 3-1. Secrets 페이지 접속

```
https://github.com/yujinpung/mlb-naver-datalab-reporter/settings/secrets/actions
```

### 3-2. Firebase Secrets 등록

#### ① FIREBASE_PROJECT_ID

```
Name: FIREBASE_PROJECT_ID
Secret: [프로젝트ID] (예: mlb-datalab-reporter)
```

#### ② FIREBASE_STORAGE_BUCKET

```
Name: FIREBASE_STORAGE_BUCKET
Secret: [버킷이름] (예: mlb-datalab-reporter.appspot.com)
```

#### ③ FIREBASE_CREDENTIALS_JSON

```
Name: FIREBASE_CREDENTIALS_JSON
Secret: [다운로드한 JSON 파일의 전체 내용]
```

**JSON 파일 내용 예시**:
```json
{
  "type": "service_account",
  "project_id": "mlb-datalab-reporter",
  "private_key_id": "...",
  "private_key": "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n",
  "client_email": "...",
  "client_id": "...",
  ...
}
```

> ⚠️ **주의**: JSON 전체 내용을 복사하되, 줄바꿈 문자(`\n`)는 그대로 유지해야 합니다.

#### ④ FIREBASE_SERVICE_ACCOUNT (선택사항, Hosting 배포용)

```
Name: FIREBASE_SERVICE_ACCOUNT
Secret: [FIREBASE_CREDENTIALS_JSON과 동일한 내용]
```

---

## 4️⃣ 로컬 테스트

### 4-1. Firebase CLI 설치

```powershell
# npm이 설치되어 있어야 함
npm install -g firebase-tools
```

### 4-2. Firebase 로그인

```powershell
firebase login
```

브라우저가 열리면 Google 계정으로 로그인

### 4-3. 프로젝트 연결

```powershell
cd C:\Users\MADUP\Desktop\projectpung
firebase use [프로젝트ID]
```

### 4-4. .firebaserc 파일 수정

`.firebaserc` 파일을 열어서 프로젝트 ID를 실제 값으로 변경:

```json
{
  "projects": {
    "default": "mlb-datalab-reporter"
  }
}
```

### 4-5. 로컬 테스트 실행

```powershell
# Python 스크립트 실행
python main.py

# Firebase Storage 업로드 확인
# (main.py에서 자동으로 실행됨)
```

---

## 5️⃣ 배포 확인

### 5-1. Firebase Hosting 배포

#### 수동 배포 (테스트용)

```powershell
# public 폴더 생성 (없으면)
mkdir public

# dashboard.html을 public 폴더로 복사
copy dashboard.html public\dashboard.html

# Firebase 배포
firebase deploy --only hosting
```

#### 자동 배포 (GitHub Actions)

GitHub Actions가 자동으로 배포합니다.

---

### 5-2. 대시보드 접속

배포 완료 후 Firebase가 제공하는 URL:

```
https://[프로젝트ID].web.app/dashboard.html
```

또는

```
https://[프로젝트ID].firebaseapp.com/dashboard.html
```

예시:
```
https://mlb-datalab-reporter.web.app/dashboard.html
```

---

## 🔧 설정 파일 설명

### firebase.json

```json
{
  "hosting": {
    "public": "public",
    "rewrites": [
      {
        "source": "**",
        "destination": "/dashboard.html"
      }
    ]
  },
  "storage": {
    "rules": "storage.rules"
  }
}
```

### storage.rules

```javascript
rules_version = '2';
service firebase.storage {
  match /b/{bucket}/o {
    match /screenshots/{allPaths=**} {
      allow read: if true;  // 모든 사용자 읽기 허용
      allow write: if request.auth != null;  // 인증된 사용자만 쓰기
    }
  }
}
```

---

## 📊 작동 방식

### 자동 업데이트 프로세스

```
매일 오전 9시 GitHub Actions 실행
    ↓
1. 네이버 데이터랩 스크린샷 생성
    ↓
2. 슬랙으로 전송
    ↓
3. Firebase Storage에 업로드 ✅
    ↓
4. Firebase Hosting에 배포 ✅
    ↓
5. 대시보드 자동 업데이트 완료!
```

---

## 🆚 Firebase vs GitHub Pages

### Firebase 장점

- ✅ **빠른 이미지 로딩**: CDN 제공
- ✅ **무제한 저장소**: 충분한 용량
- ✅ **실시간 업데이트**: 빠른 반영
- ✅ **커스텀 도메인**: 쉽게 연결 가능

### GitHub Pages 장점

- ✅ **설정 간단**: 바로 사용 가능
- ✅ **완전 무료**: 제한 없음
- ✅ **Git 통합**: 코드와 함께 관리

---

## ⚠️ 주의사항

### 1. Firebase 무료 플랜 제한

- **Storage**: 5GB 무료
- **Hosting**: 10GB 무료
- **트래픽**: 월 360MB 무료

> 현재 프로젝트는 무료 플랜으로 충분합니다!

### 2. 인증 정보 보안

- **절대 공개하지 마세요!**
- GitHub Secrets에만 저장
- 로컬 파일은 `.gitignore`에 추가

### 3. Storage 규칙

- 현재 설정: 모든 사용자 읽기 허용
- 필요시 더 엄격한 규칙 설정 가능

---

## 🔍 문제 해결

### ❌ Firebase 배포 실패

**원인**: 인증 정보 오류

**해결 방법**:
1. GitHub Secrets의 `FIREBASE_CREDENTIALS_JSON` 확인
2. JSON 형식이 올바른지 확인
3. 프로젝트 ID가 맞는지 확인

---

### ❌ 이미지가 로드되지 않음

**원인**: Storage 버킷 이름 오류

**해결 방법**:
1. `FIREBASE_STORAGE_BUCKET` Secret 확인
2. `dashboard.html`의 URL 형식 확인
3. Storage 규칙이 읽기를 허용하는지 확인

---

### ❌ 업로드 권한 오류

**원인**: Storage 규칙 문제

**해결 방법**:
1. Firebase Console → Storage → 규칙
2. 읽기 규칙 확인: `allow read: if true;`
3. 배포: `firebase deploy --only storage`

---

## 📝 체크리스트

Firebase 설정 완료 전 확인:

- [ ] Firebase 프로젝트 생성
- [ ] Hosting 활성화
- [ ] Storage 활성화
- [ ] 서비스 계정 키 다운로드
- [ ] 프로젝트 ID 확인
- [ ] Storage 버킷 이름 확인
- [ ] GitHub Secrets 3개 등록
- [ ] .firebaserc 파일 수정
- [ ] 로컬 테스트 실행
- [ ] Firebase 배포 테스트
- [ ] 대시보드 접속 확인

---

## 🎯 다음 단계

설정 완료 후:

1. **GitHub Actions 테스트**: "Run workflow" 클릭
2. **대시보드 확인**: Firebase URL 접속
3. **자동 업데이트 확인**: 내일 오전 9시 이후 확인

---

## 🔗 관련 링크

- **Firebase Console**: https://console.firebase.google.com
- **Firebase 문서**: https://firebase.google.com/docs
- **GitHub 저장소**: https://github.com/yujinpung/mlb-naver-datalab-reporter

---

## ✅ 완료!

축하합니다! Firebase 설정이 완료되었습니다! 🎉

**다음 단계**:
- GitHub에 코드 업로드
- GitHub Actions 테스트 실행
- Firebase 대시보드 확인

---

**문제가 발생하면 Firebase Console의 로그를 확인하거나 이 가이드의 문제 해결 섹션을 참고하세요!**


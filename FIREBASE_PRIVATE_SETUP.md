# 🔒 Private 저장소 + Firebase 전용 호스팅 가이드

## 📋 개요

GitHub 저장소를 **Private**로 유지하면서 Firebase만으로 호스팅하는 방법입니다.

---

## 🎯 장점

### ✅ Private 저장소 유지
- 코드 비공개
- GitHub Pages 불필요
- 완전한 Firebase 독립

### ✅ Firebase 무료 티어로 충분
- Storage: 5GB
- Hosting: 10GB 저장, 360MB/일 전송
- 현재 프로젝트: ~300KB (이미지 8개 x ~35KB)

---

## 🔥 필수 설정

### 1. Firebase Storage 활성화

1. **Firebase Console 접속**:
   ```
   https://console.firebase.google.com/project/mlb-datalab-reporter/storage
   ```

2. **"Get started" 클릭**

3. **Security rules 선택**:
   ```
   Start in production mode (권장)
   ```

4. **Location 선택**:
   ```
   asia-northeast3 (서울)
   ```

5. **"Done" 클릭**

---

### 2. Storage Rules 설정

Firebase Storage에 읽기 권한 설정:

```javascript
rules_version = '2';
service firebase.storage {
  match /b/{bucket}/o {
    // screenshots 폴더는 누구나 읽기 가능
    match /screenshots/{allPaths=**} {
      allow read: if true;
      allow write: if request.auth != null;
    }
  }
}
```

**적용 방법**:
1. Firebase Console → Storage → Rules 탭
2. 위 코드 붙여넣기
3. "Publish" 클릭

---

### 3. GitHub Secrets 등록

다음 3개 Secrets 필요:

#### FIREBASE_STORAGE_BUCKET
```
mlb-datalab-reporter.firebasestorage.app
```

#### FIREBASE_PROJECT_ID
```
mlb-datalab-reporter
```

#### FIREBASE_CREDENTIALS_JSON
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

**Service Account 생성 방법**:
1. Firebase Console → Project Settings → Service Accounts
2. "Generate new private key" 클릭
3. JSON 파일 다운로드
4. 전체 내용 복사하여 GitHub Secrets에 등록

---

## 🚀 배포 흐름

```
GitHub Actions (Private 저장소)
        ↓
1. 스크린샷 캡처 (8개 키워드)
        ↓
2. Firebase Storage 업로드
   └─> https://storage.googleapis.com/mlb-datalab-reporter.firebasestorage.app/screenshots/...
        ↓
3. Firebase Hosting 배포
   └─> https://mlb-datalab-reporter.web.app/
        ↓
✅ 완료! (GitHub는 Private 유지)
```

---

## 📊 이미지 URL 예시

### Firebase Storage URL
```
https://storage.googleapis.com/mlb-datalab-reporter.firebasestorage.app/screenshots/NaverDatalab_2025-11-25_MLB.png
```

**장점**:
- ✅ Private 저장소에서도 작동
- ✅ 인증 불필요 (Public 읽기 권한)
- ✅ CDN 제공 (빠른 속도)
- ✅ CORS 문제 없음

---

## 🔧 현재 설정 확인

### main.py 확인

Firebase Storage 업로드가 활성화되어 있는지 확인:

```python
# 2. Firebase Storage 업로드
if FIREBASE_AVAILABLE and os.getenv("FIREBASE_STORAGE_BUCKET"):
    try:
        logger.info("\n☁️  STEP 2-1: Firebase Storage 업로드")
        firebase_urls = upload_all_screenshots(config.OUTPUT_DIR)
        if firebase_urls:
            logger.info(f"✅ Firebase Storage 업로드 완료: {len(firebase_urls)}개")
            image_urls.update(firebase_urls)
    except Exception as e:
        logger.warning(f"⚠️  Firebase Storage 업로드 실패: {str(e)}")
```

---

## 💰 비용 분석

### Firebase 무료 티어

| 항목 | 무료 제공량 | 현재 사용량 | 초과 가능성 |
|------|------------|-----------|-----------|
| Storage | 5GB | ~1MB | ❌ 없음 |
| Hosting (저장) | 10GB | ~10KB | ❌ 없음 |
| Hosting (전송) | 360MB/일 | ~1MB/일 | ❌ 없음 |
| Functions | 125K 호출/월 | 0 | ❌ 없음 |

**예상 비용**: $0 (완전 무료) 💰✅

### GitHub Actions

| 항목 | 무료 제공량 | 현재 사용량 | 초과 가능성 |
|------|------------|-----------|-----------|
| Actions 실행 시간 | 2,000분/월 | ~90분/월 | ❌ 없음 |
| Private 저장소 | ✅ 무제한 | 1개 | ❌ 없음 |

**총 비용**: $0 (완전 무료) 💰✅

---

## ✅ 체크리스트

### Firebase 설정
- [ ] Firebase Storage 활성화
- [ ] Storage Rules 설정 (Public 읽기 허용)
- [ ] Service Account JSON 생성
- [ ] GitHub Secrets 3개 등록:
  - [ ] FIREBASE_STORAGE_BUCKET
  - [ ] FIREBASE_PROJECT_ID
  - [ ] FIREBASE_CREDENTIALS_JSON

### GitHub 설정
- [ ] 저장소 Private로 설정
- [ ] GitHub Actions 활성화 확인
- [ ] Secrets 확인

### 코드 설정
- [x] dashboard.html - Firebase Storage URL 사용
- [x] main.py - Firebase Storage 업로드 활성화
- [x] .github/workflows/daily.yml - Firebase 배포
- [x] firebase_uploader.py - Storage 업로드 로직

---

## 🐛 문제 해결

### ❌ Firebase Storage 업로드 실패

**로그 예시**:
```
⚠️  Firebase Storage 업로드 실패: Permission denied
```

**해결**:
1. Firebase Console에서 Storage 활성화 확인
2. Storage Rules 확인 (읽기/쓰기 권한)
3. Service Account JSON 확인
4. FIREBASE_CREDENTIALS_JSON Secret 재등록

---

### ❌ 이미지가 표시되지 않음

**원인**: Storage Rules가 읽기를 허용하지 않음

**해결**:
```javascript
// Storage Rules
match /screenshots/{allPaths=**} {
  allow read: if true;  // 모든 사용자 읽기 허용
  allow write: if request.auth != null;
}
```

---

## 🔒 보안

### Private 저장소 장점

- ✅ 소스 코드 비공개
- ✅ API Keys/Secrets 안전
- ✅ 워크플로우 비공개
- ✅ 커밋 히스토리 비공개

### Firebase Storage 보안

- ✅ 이미지만 Public 제공
- ✅ 쓰기 권한은 인증 필요
- ✅ 삭제 권한 없음
- ✅ CDN 캐싱으로 안정적

---

## 🎯 최종 구조

```
Private GitHub Repository
        ↓ (GitHub Actions)
Firebase Storage (이미지 저장)
        ↓
Firebase Hosting (웹 호스팅)
        ↓
Public URL: https://mlb-datalab-reporter.web.app/
```

**외부에 공개되는 것**:
- ✅ 대시보드 웹페이지
- ✅ 이미지 파일
- ❌ 소스 코드 (Private 유지)
- ❌ GitHub Actions 워크플로우 (Private 유지)

---

## 🚀 다음 단계

1. **Firebase Storage 활성화 및 Rules 설정**
2. **Service Account JSON 생성**
3. **GitHub Secrets 3개 등록**
4. **GitHub Actions 실행**
5. **Firebase URL 접속 확인**

---

**Private 저장소를 유지하면서 완전 무료로 운영할 수 있습니다!** 🔒💰✅


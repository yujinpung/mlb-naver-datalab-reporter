# 🔗 Webhook + GitHub Raw URL 설정 가이드

이 가이드는 **Slack Webhook**을 사용하여 **GitHub Raw URL**로 이미지를 전송하는 방법을 설명합니다.

---

## 📋 개요

### 방식 비교

| 방식 | 이미지 전송 | 설정 난이도 | 비용 |
|------|------------|------------|------|
| **Bot Token** | 파일 직접 업로드 | 어려움 | 무료 |
| **Webhook + Firebase** | URL 포함 | 중간 | Firebase 무료 티어 |
| **Webhook + GitHub Raw** | URL 포함 | 쉬움 | 완전 무료 ✅ |

### GitHub Raw URL 방식의 장점

- ✅ **완전 무료**: Firebase Storage 불필요
- ✅ **설정 간단**: Webhook URL만 있으면 됨
- ✅ **자동화**: GitHub Actions에서 자동 커밋
- ✅ **안정적**: GitHub 인프라 사용

---

## 🚀 작동 방식

```
1. 스크린샷 캡처
   └─> screenshots/NaverDatalab_2025-11-26_MLB.png
       
2. GitHub Raw URL 생성
   └─> https://raw.githubusercontent.com/yujinpung/mlb-naver-datalab-reporter/main/screenshots/NaverDatalab_2025-11-26_MLB.png
       
3. Slack Webhook으로 이미지 URL 전송
   └─> 슬랙 메시지에 이미지 표시
```

---

## ⚙️ 설정 방법

### 1단계: Slack Webhook URL 등록

GitHub Secrets에 `SLACK_WEBHOOK_URL` 등록:

```
Settings → Secrets and variables → Actions → New repository secret

Name: SLACK_WEBHOOK_URL
Secret: https://hooks.slack.com/services/YOUR/WEBHOOK/URL
```

자세한 방법: [`WEBHOOK_SETUP.md`](WEBHOOK_SETUP.md)

---

### 2단계: 자동 실행 확인

GitHub Actions가 다음 작업을 자동으로 수행합니다:

1. **스크린샷 캡처**
   - 8개 키워드 스크린샷 생성
   - `screenshots/` 폴더에 저장

2. **GitHub Raw URL 생성**
   - 각 스크린샷의 GitHub Raw URL 자동 생성
   - Firebase 없이도 작동

3. **슬랙 전송**
   - Webhook으로 이미지 URL 포함 메시지 전송
   - 슬랙에서 이미지 자동 표시

4. **GitHub 커밋 & 푸시**
   - 스크린샷을 GitHub에 자동 커밋
   - Raw URL 즉시 사용 가능

---

## 🔍 GitHub Raw URL 구조

### URL 형식

```
https://raw.githubusercontent.com/{username}/{repo}/{branch}/screenshots/{filename}
```

### 실제 예시

```
https://raw.githubusercontent.com/yujinpung/mlb-naver-datalab-reporter/main/screenshots/NaverDatalab_2025-11-26_MLB.png
```

### 구성 요소

- **username**: `yujinpung` (GitHub 사용자명)
- **repo**: `mlb-naver-datalab-reporter` (저장소명)
- **branch**: `main` (브랜치명)
- **filename**: `NaverDatalab_2025-11-26_MLB.png` (파일명)

---

## 📝 환경변수 설정

### GitHub Actions 환경변수 (자동 설정)

워크플로우에서 자동으로 설정됩니다:

```yaml
env:
  GITHUB_USERNAME: ${{ github.repository_owner }}
  GITHUB_REPO: ${{ github.event.repository.name }}
  GITHUB_BRANCH: main
```

### 로컬 테스트 환경변수 (.env)

로컬에서 테스트하려면 `.env` 파일에 추가:

```env
GITHUB_USERNAME=yujinpung
GITHUB_REPO=mlb-naver-datalab-reporter
GITHUB_BRANCH=main
```

---

## 🔄 실행 흐름

### GitHub Actions 실행 순서

```
1. 스크린샷 캡처
   ↓
2. GitHub Raw URL 생성
   ↓
3. 슬랙 전송 (이미지 URL 포함)
   ↓
4. GitHub 커밋 & 푸시
   ↓
5. GitHub Pages 배포
```

### 코드 흐름

```python:92:121:main.py
# 2. 이미지 URL 생성 (Webhook 사용 시 필요)
image_urls = {}

# 2-1. Firebase Storage 업로드 (선택사항)
if FIREBASE_AVAILABLE and os.getenv("FIREBASE_STORAGE_BUCKET"):
    try:
        logger.info("\n☁️  STEP 2-1: Firebase Storage 업로드")
        firebase_urls = upload_all_screenshots(config.OUTPUT_DIR)
        if firebase_urls:
            logger.info(f"✅ Firebase Storage 업로드 완료: {len(firebase_urls)}개")
            image_urls.update(firebase_urls)
            for keyword, url in firebase_urls.items():
                logger.info(f"   - {keyword}: {url}")
    except Exception as e:
        logger.warning(f"⚠️  Firebase Storage 업로드 실패 (무시): {str(e)}")

# 2-2. GitHub Raw URL 생성 (Firebase 없을 때 사용)
if not image_urls:
    logger.info("\n🔗 STEP 2-2: GitHub Raw URL 생성")
    for screenshot in all_screenshots:
        keyword = screenshot['keyword']
        filename = os.path.basename(screenshot['path'])
        github_url = config.get_github_raw_url(filename)
        image_urls[keyword] = github_url
        logger.info(f"   - {keyword}: {github_url}")
    logger.info(f"✅ GitHub Raw URL 생성 완료: {len(image_urls)}개")
```

---

## 🎯 우선순위

시스템은 다음 우선순위로 이미지를 전송합니다:

1. **Bot Token** (설정된 경우)
   - 이미지 파일 직접 업로드

2. **Firebase Storage** (설정된 경우)
   - Firebase Storage URL 사용

3. **GitHub Raw URL** (기본)
   - GitHub Raw URL 사용 (무료)

---

## ✅ 필수 설정

### GitHub Secrets

| Secret | 필수 여부 | 설명 |
|--------|----------|------|
| `SLACK_WEBHOOK_URL` | ✅ 필수 | Slack Webhook URL |
| `SLACK_CHANNEL` | ⚪ 선택 | 슬랙 채널 (기본값: `#datalab-report`) |

### 선택 설정

| Secret | 설명 |
|--------|------|
| `SLACK_BOT_TOKEN` | Bot Token 방식 사용 시 |
| `FIREBASE_STORAGE_BUCKET` | Firebase Storage 사용 시 |

---

## 🔍 로그 확인

GitHub Actions 실행 로그에서 다음을 확인하세요:

```
🔗 STEP 2-2: GitHub Raw URL 생성
   - MLB: https://raw.githubusercontent.com/.../NaverDatalab_2025-11-26_MLB.png
   - MLB키즈: https://raw.githubusercontent.com/.../NaverDatalab_2025-11-26_MLB키즈.png
   ...
✅ GitHub Raw URL 생성 완료: 8개

📤 STEP 3: 슬랙 전송
  키워드 'MLB' 전송 중...
  ✅ 'MLB' 전송 완료
  ...
✅ 슬랙 전송 완료: 8/8개
```

---

## 🐛 문제 해결

### ❌ 이미지가 표시되지 않음

**원인**: GitHub Raw URL이 아직 활성화되지 않음

**해결**:
1. GitHub Actions 로그 확인
2. "Commit and push screenshots" 단계 완료 확인
3. GitHub 저장소에서 스크린샷 파일 확인

---

### ❌ "이미지 URL 없음" 메시지

**원인**: `SLACK_WEBHOOK_URL`이 설정되지 않음

**해결**:
1. GitHub Secrets에 `SLACK_WEBHOOK_URL` 등록
2. Webhook URL 생성 방법: [`WEBHOOK_SETUP.md`](WEBHOOK_SETUP.md)

---

### ❌ 슬랙 메시지가 안 옴

**원인**: Webhook URL 오류

**해결**:
1. Webhook URL 확인
2. 슬랙 채널 확인
3. 자세한 방법: [`SLACK_TROUBLESHOOTING.md`](SLACK_TROUBLESHOOTING.md)

---

## 💡 장점 요약

### GitHub Raw URL 방식

- ✅ **완전 무료**: 추가 비용 없음
- ✅ **설정 간단**: Webhook URL만 필요
- ✅ **안정적**: GitHub 인프라 사용
- ✅ **자동화**: GitHub Actions에서 자동 처리
- ✅ **유지보수 간편**: Firebase 설정 불필요

### Firebase Storage 방식 (선택)

- ✅ **더 빠른 로딩**: CDN 사용
- ✅ **더 나은 캐싱**: Firebase Storage 최적화
- ⚠️  **무료 티어 제한**: 1GB 저장소, 10GB 전송량/월

---

## 🎯 권장 설정

### 개인/소규모 프로젝트

**Webhook + GitHub Raw URL** (현재 설정)
- 완전 무료
- 설정 간단
- 충분한 성능

### 대규모 프로젝트

**Webhook + Firebase Storage**
- 더 빠른 로딩
- 더 나은 캐싱
- 스케일링 용이

---

## 📚 관련 문서

- [`WEBHOOK_SETUP.md`](WEBHOOK_SETUP.md): Webhook 설정 가이드
- [`WEBHOOK_SETUP_DETAILED.md`](WEBHOOK_SETUP_DETAILED.md): 상세 Webhook 설정
- [`SLACK_TROUBLESHOOTING.md`](SLACK_TROUBLESHOOTING.md): 슬랙 문제 해결
- [`FIREBASE_SETUP.md`](FIREBASE_SETUP.md): Firebase Storage 설정 (선택)

---

## ✅ 체크리스트

- [ ] GitHub Secrets에 `SLACK_WEBHOOK_URL` 등록
- [ ] GitHub Actions 워크플로우 실행 확인
- [ ] 로그에서 "GitHub Raw URL 생성 완료" 확인
- [ ] 로그에서 "슬랙 전송 완료" 확인
- [ ] 슬랙 채널에서 메시지 및 이미지 확인

---

**완료되었습니다!** 🎉

이제 매일 오전 9시에 자동으로 스크린샷이 캡처되고, GitHub Raw URL을 통해 슬랙으로 이미지가 전송됩니다.

Firebase 설정 없이도 완전 무료로 운영할 수 있습니다!


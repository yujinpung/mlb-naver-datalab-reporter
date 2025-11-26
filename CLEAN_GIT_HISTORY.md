# 🔐 Git 히스토리에서 민감한 정보 제거 가이드

## ⚠️ 중요 경고

**이 작업은 Git 히스토리를 다시 작성합니다!**
- 협업 중인 저장소라면 팀원에게 알려야 합니다
- 백업을 먼저 만들어야 합니다
- Force push가 필요합니다

---

## 🎯 방법 1: BFG Repo-Cleaner 사용 (권장)

### 1단계: BFG 다운로드

1. **BFG 다운로드**:
   ```
   https://rtyley.github.io/bfg-repo-cleaner/
   ```

2. **Java 설치 확인** (BFG는 Java가 필요):
   ```powershell
   java -version
   ```

### 2단계: 저장소 클론 (미러)

```powershell
cd C:\Users\MADUP\Desktop
git clone --mirror https://github.com/yujinpung/mlb-naver-datalab-reporter.git
cd mlb-naver-datalab-reporter.git
```

### 3단계: 민감한 정보 제거

```powershell
# 특정 텍스트 제거
java -jar bfg.jar --replace-text passwords.txt

# passwords.txt 파일 내용:
# xoxb-EXAMPLE-TOKEN-REPLACE-WITH-YOURS===> *** REMOVED ***
```

### 4단계: Git 정리 및 푸시

```powershell
git reflog expire --expire=now --all
git gc --prune=now --aggressive
git push --force
```

---

## 🎯 방법 2: git filter-branch 사용

### 1단계: 백업 생성

```powershell
cd C:\Users\MADUP\Desktop\projectpung
git branch backup-before-cleanup
```

### 2단계: 해당 파일 전체 히스토리 제거

```powershell
git filter-branch --force --index-filter "git rm --cached --ignore-unmatch GITHUB_SETUP.md" --prune-empty --tag-name-filter cat -- --all
```

### 3단계: 정리

```powershell
git for-each-ref --format="delete %(refname)" refs/original | git update-ref --stdin
git reflog expire --expire=now --all
git gc --prune=now --aggressive
```

### 4단계: Force Push

```powershell
git push origin --force --all
git push origin --force --tags
```

---

## 🎯 방법 3: 특정 커밋만 수정 (가장 간단)

### 1단계: 백업 생성

```powershell
git branch backup-before-cleanup
```

### 2단계: Interactive Rebase

```powershell
# 최근 10개 커밋 확인
git log --oneline -10

# 문제가 있는 커밋 이전부터 rebase
git rebase -i HEAD~10
```

### 3단계: 해당 커밋을 'edit'로 변경

에디터가 열리면 문제가 있는 커밋 앞의 `pick`을 `edit`으로 변경:

```
edit abc1234 Add GitHub setup guide
pick def5678 ...
```

### 4단계: 파일 수정

```powershell
# 파일 수정
notepad GITHUB_SETUP.md

# 수정 완료 후
git add GITHUB_SETUP.md
git commit --amend
git rebase --continue
```

### 5단계: Force Push

```powershell
git push origin --force
```

---

## 🎯 방법 4: 저장소 새로 시작 (가장 확실)

### 1단계: 현재 상태 백업

```powershell
cd C:\Users\MADUP\Desktop
cp -r projectpung projectpung-backup
```

### 2단계: Git 히스토리 삭제

```powershell
cd projectpung
rm -rf .git
```

### 3단계: 새로 초기화

```powershell
git init
git add .
git commit -m "Initial commit (cleaned history)"
```

### 4단계: Remote 재설정

```powershell
git remote add origin https://github.com/yujinpung/mlb-naver-datalab-reporter.git
git push origin main --force
```

---

## ⚠️ Force Push 후 주의사항

### 다른 컴퓨터에서 작업 중이라면

```powershell
# 기존 저장소 백업
cd path/to/old/repo
cd ..
mv old/repo old/repo-backup

# 새로 클론
git clone https://github.com/yujinpung/mlb-naver-datalab-reporter.git
```

---

## ✅ 작업 완료 확인

### 히스토리에서 토큰 검색

```powershell
# 전체 히스토리에서 검색
git log --all --full-history --source --pretty=format:"%H" | ForEach-Object { git show $_ | Select-String "xoxb-183311941203" }
```

아무것도 나오지 않으면 성공! ✅

---

## 🔒 추가 보안 조치

### 1. Slack Token 즉시 무효화

```
https://api.slack.com/apps
→ 앱 선택 → OAuth & Permissions → Revoke Token
```

### 2. GitHub Secrets 확인

```
https://github.com/yujinpung/mlb-naver-datalab-reporter/settings/secrets/actions
```

### 3. .env 파일 확인

로컬 `.env` 파일에 토큰이 있다면 새 토큰으로 교체

---

## 💡 앞으로 방지하는 방법

### 1. Pre-commit Hook 설정

`.git/hooks/pre-commit` 파일 생성:

```bash
#!/bin/sh
# 민감한 정보 체크
if git diff --cached | grep -E "xoxb-|hooks\.slack\.com/services/T[A-Z0-9]+/B[A-Z0-9]+"; then
    echo "❌ Error: Slack token detected!"
    echo "Please remove sensitive information before committing."
    exit 1
fi
```

### 2. .gitignore 확인

```
.env
firebase-credentials.json
*.secret
*.private
```

### 3. GitHub Secret Scanning 활성화

GitHub에서 자동으로 활성화되어 있지만, 확인:

```
Settings → Security → Code security and analysis
→ Secret scanning: Enabled
```

---

## 🆘 문제 발생 시

### 백업에서 복구

```powershell
git checkout backup-before-cleanup
git branch -D main
git checkout -b main
git push origin main --force
```

---

## 📋 권장 순서

1. **백업 생성** ✅
2. **Slack Token 무효화** ✅ (가장 중요!)
3. **Git 히스토리 정리** (이 문서의 방법 중 하나 선택)
4. **Force Push** ✅
5. **확인** ✅

---

**가장 중요한 것은 Slack Token을 즉시 무효화하는 것입니다!** 🚨

Git 히스토리 정리는 그 다음입니다.


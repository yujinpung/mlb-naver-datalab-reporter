# 🔐 Git 히스토리에서 토큰 제거 가이드

## 🎯 3가지 방법

---

## 방법 1: BFG Repo-Cleaner (가장 쉽고 빠름) ⭐ 권장

### 준비사항

1. **Java 설치 확인**:
   ```powershell
   java -version
   ```
   
   없다면 다운로드: https://www.java.com/download/

2. **BFG 다운로드**:
   ```
   https://rtyley.github.io/bfg-repo-cleaner/
   ```
   
   → `bfg-1.14.0.jar` 파일 다운로드
   → `C:\Users\MADUP\Desktop\` 에 저장

### 실행 단계

#### 1. 제거할 텍스트 파일 생성

`passwords.txt` 파일을 메모장으로 만듭니다:

```
xoxb-EXAMPLE-TOKEN-REPLACE-WITH-YOURS
```

저장 위치: `C:\Users\MADUP\Desktop\passwords.txt`

#### 2. 저장소 미러 클론

```powershell
cd C:\Users\MADUP\Desktop
git clone --mirror https://github.com/yujinpung/mlb-naver-datalab-reporter.git repo-mirror
```

#### 3. BFG 실행

```powershell
java -jar bfg-1.14.0.jar --replace-text passwords.txt repo-mirror
```

#### 4. Git 정리

```powershell
cd repo-mirror
git reflog expire --expire=now --all
git gc --prune=now --aggressive
```

#### 5. Force Push

```powershell
git push --force
```

#### 6. 로컬 저장소 다시 클론

```powershell
cd C:\Users\MADUP\Desktop
rm -r -fo projectpung
git clone https://github.com/yujinpung/mlb-naver-datalab-reporter.git projectpung
```

---

## 방법 2: 저장소 새로 시작 (가장 확실) ⭐⭐

### 장점
- ✅ 100% 확실하게 제거
- ✅ 복잡한 명령어 불필요
- ✅ 실수 위험 없음

### 단점
- ❌ 모든 커밋 히스토리 삭제됨

### 실행 단계

#### 1. 현재 파일 백업

```powershell
cd C:\Users\MADUP\Desktop
cp -r projectpung projectpung-backup
```

#### 2. Git 히스토리 삭제

```powershell
cd projectpung
rm -r -fo .git
```

#### 3. 새로 초기화

```powershell
git init
git add .
git commit -m "Initial commit: Naver Datalab Capture System (cleaned history)"
```

#### 4. Remote 재설정 및 Force Push

```powershell
git remote add origin https://github.com/yujinpung/mlb-naver-datalab-reporter.git
git branch -M main
git push -u origin main --force
```

✅ **완료!** 모든 히스토리가 깨끗하게 정리됩니다.

---

## 방법 3: Git Bash에서 sed 사용

### 실행 단계

#### 1. Git Bash 열기

```
C:\Program Files\Git\git-bash.exe
```

#### 2. 프로젝트 폴더로 이동

```bash
cd /c/Users/MADUP/Desktop/projectpung
```

#### 3. Filter-branch 실행

```bash
git filter-branch --force --tree-filter '
if [ -f GITHUB_SETUP.md ]; then
  sed -i "s/xoxb-EXAMPLE-TOKEN-REPLACE-WITH-YOURS/xoxb-YOUR-BOT-TOKEN-HERE/g" GITHUB_SETUP.md
fi
' --prune-empty --tag-name-filter cat -- --all
```

#### 4. 정리 및 Push

```bash
git for-each-ref --format="delete %(refname)" refs/original | git update-ref --stdin
git reflog expire --expire=now --all
git gc --prune=now --aggressive
git push origin --force --all
```

---

## 🎯 권장 방법

### Private 저장소 + 히스토리 중요하지 않음
→ **방법 2** (저장소 새로 시작) ⭐⭐⭐

### Public 저장소 + 히스토리 유지 필요
→ **방법 1** (BFG) ⭐⭐

### Git Bash 사용 가능
→ **방법 3** (sed) ⭐

---

## 🚨 가장 중요한 것!

**Git 히스토리 정리보다 더 중요한 것:**

### 즉시 Slack Token 무효화!

1. **Slack API 페이지**:
   ```
   https://api.slack.com/apps
   ```

2. **앱 선택** → **"OAuth & Permissions"**

3. **"Revoke Token"** 클릭

4. **새 토큰 생성** (필요시)

→ 노출된 토큰을 무효화하면 히스토리에 남아있어도 사용할 수 없습니다!

---

## 📋 체크리스트

우선순위 순서:

1. [ ] **Slack Token 무효화** ← 가장 중요! 🚨
2. [ ] 방법 선택 (1, 2, 3 중 하나)
3. [ ] Git 히스토리 정리 실행
4. [ ] Force Push 완료
5. [ ] 히스토리 검증
6. [ ] 다른 컴퓨터에서 저장소 다시 클론

---

## 💡 제 권장

### 가장 간단하고 확실한 방법

**방법 2: 저장소 새로 시작**

이유:
- ✅ 5분 안에 완료
- ✅ 100% 확실하게 제거
- ✅ 복잡한 명령어 불필요
- ✅ 현재 프로젝트는 히스토리가 중요하지 않음

명령어:
```powershell
# 백업
cd C:\Users\MADUP\Desktop
cp -r projectpung projectpung-backup

# Git 히스토리 삭제 및 재시작
cd projectpung
rm -r -fo .git
git init
git add .
git commit -m "Initial commit (cleaned)"
git remote add origin https://github.com/yujinpung/mlb-naver-datalab-reporter.git
git branch -M main
git push -u origin main --force
```

---

**어떤 방법을 선택하시겠습니까?** 

1번 (BFG), 2번 (새로 시작), 또는 3번 (Git Bash) 중 원하시는 방법을 알려주시면 단계별로 도와드리겠습니다!


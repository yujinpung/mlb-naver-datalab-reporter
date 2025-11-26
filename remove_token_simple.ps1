# Git 히스토리에서 토큰 제거 (간단한 방법)
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Git History Token Remover" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "이 스크립트는 Git 히스토리를 다시 작성합니다." -ForegroundColor Yellow
Write-Host "백업 브랜치를 먼저 생성합니다." -ForegroundColor Yellow
Write-Host ""

# 백업 생성
Write-Host "[1/5] 백업 브랜치 생성 중..." -ForegroundColor Green
git branch backup-before-cleanup 2>$null
if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ 백업 완료: backup-before-cleanup" -ForegroundColor Green
} else {
    Write-Host "⚠️  백업 브랜치가 이미 존재합니다" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "[2/5] Git 히스토리에서 민감한 정보 제거 중..." -ForegroundColor Green
Write-Host "   제거할 토큰: xoxb-183311941203-9934684663665-y4J8hFGLFuGL8Ls2DFKXu7vk" -ForegroundColor Red
Write-Host ""

# 환경변수 설정
$env:FILTER_BRANCH_SQUELCH_WARNING = "1"

# Git filter-branch 실행
git filter-branch --force --tree-filter "if (Test-Path GITHUB_SETUP.md) { (Get-Content GITHUB_SETUP.md -Raw -Encoding UTF8) -replace 'xoxb-183311941203-9934684663665-y4J8hFGLFuGL8Ls2DFKXu7vk', 'xoxb-YOUR-BOT-TOKEN-HERE' | Set-Content GITHUB_SETUP.md -NoNewline -Encoding UTF8 }" --prune-empty --tag-name-filter cat -- --all

if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Filter-branch 실패!" -ForegroundColor Red
    Write-Host "   다른 방법을 시도하세요." -ForegroundColor Yellow
    exit 1
}

Write-Host "✅ 히스토리 필터링 완료" -ForegroundColor Green
Write-Host ""

Write-Host "[3/5] Git 정리 중..." -ForegroundColor Green
git for-each-ref --format="delete %(refname)" refs/original | git update-ref --stdin
git reflog expire --expire=now --all
git gc --prune=now --aggressive

Write-Host "✅ Git 정리 완료" -ForegroundColor Green
Write-Host ""

Write-Host "[4/5] 원격 저장소에 Force Push 중..." -ForegroundColor Green
Write-Host "   ⚠️  이 작업은 되돌릴 수 없습니다!" -ForegroundColor Yellow
Write-Host ""

$confirm = Read-Host "계속하시겠습니까? (yes/no)"
if ($confirm -ne "yes") {
    Write-Host "취소되었습니다." -ForegroundColor Yellow
    Write-Host "백업에서 복구하려면: git checkout backup-before-cleanup" -ForegroundColor Cyan
    exit
}

git push origin --force --all

if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Force Push 완료" -ForegroundColor Green
} else {
    Write-Host "❌ Push 실패!" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "[5/5] 검증 중..." -ForegroundColor Green

# 히스토리에서 토큰 검색
$found = git log --all --source --pretty=format:"%H" | ForEach-Object { 
    git show $_ 2>$null | Select-String "xoxb-183311941203" -Quiet
}

if ($found) {
    Write-Host "⚠️  토큰이 여전히 히스토리에 남아있습니다" -ForegroundColor Yellow
} else {
    Write-Host "✅ 토큰이 히스토리에서 완전히 제거되었습니다!" -ForegroundColor Green
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "  작업 완료!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "다음 단계:" -ForegroundColor Cyan
Write-Host "1. Slack에서 노출된 Bot Token 무효화" -ForegroundColor White
Write-Host "   → https://api.slack.com/apps" -ForegroundColor Gray
Write-Host "2. GitHub Actions Secrets 확인" -ForegroundColor White
Write-Host "   → https://github.com/yujinpung/mlb-naver-datalab-reporter/settings/secrets/actions" -ForegroundColor Gray
Write-Host ""


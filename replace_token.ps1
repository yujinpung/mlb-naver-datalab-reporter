# Git 히스토리에서 민감한 정보 제거 스크립트
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Git History Token Remover" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "WARNING: This will rewrite Git history!" -ForegroundColor Yellow
Write-Host ""
Write-Host "Removing token: xoxb-EXAMPLE-TOKEN-REPLACE-WITH-YOURS" -ForegroundColor Red
Write-Host ""

$continue = Read-Host "Continue? (yes/no)"
if ($continue -ne "yes") {
    Write-Host "Cancelled." -ForegroundColor Yellow
    exit
}

Write-Host ""
Write-Host "Step 1: Creating backup branch..." -ForegroundColor Green
git branch backup-before-cleanup 2>$null

Write-Host ""
Write-Host "Step 2: Filtering Git history..." -ForegroundColor Green

# filter-branch를 사용하여 특정 텍스트 교체
git filter-branch --force --tree-filter "if (Test-Path GITHUB_SETUP.md) { (Get-Content GITHUB_SETUP.md -Raw) -replace 'xoxb-EXAMPLE-TOKEN-REPLACE-WITH-YOURS', 'xoxb-YOUR-BOT-TOKEN-HERE' | Set-Content GITHUB_SETUP.md -NoNewline }" --tag-name-filter cat -- --all

Write-Host ""
Write-Host "Step 3: Cleaning up references..." -ForegroundColor Green
git for-each-ref --format="delete %(refname)" refs/original | git update-ref --stdin
git reflog expire --expire=now --all
git gc --prune=now --aggressive

Write-Host ""
Write-Host "Step 4: Force pushing to remote..." -ForegroundColor Green
git push origin --force --all
git push origin --force --tags

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "Cleanup Complete!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "Backup branch 'backup-before-cleanup' created." -ForegroundColor Cyan
Write-Host "If needed, restore with: git checkout backup-before-cleanup" -ForegroundColor Cyan


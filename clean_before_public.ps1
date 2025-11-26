# ═══════════════════════════════════════════════════════════════════
#  Public 저장소 전환 전 불필요한 파일 자동 삭제 스크립트
# ═══════════════════════════════════════════════════════════════════

Write-Host "`n" -NoNewline
Write-Host "╔════════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║     Public 저장소 전환 준비 - 파일 정리 스크립트      ║" -ForegroundColor Cyan
Write-Host "╚════════════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""

# 현재 위치 확인
$projectPath = "C:\Users\MADUP\Desktop\projectpung"
if (-not (Test-Path $projectPath)) {
    Write-Host "❌ 프로젝트 폴더를 찾을 수 없습니다: $projectPath" -ForegroundColor Red
    exit 1
}

cd $projectPath
Write-Host "📂 작업 경로: $projectPath`n" -ForegroundColor Green

# 삭제할 파일 목록
$filesToDelete = @(
    # 슬랙 관련 (13개)
    "slack_sender.py",
    "check_slack_issue.py",
    "diagnose_slack.py",
    "test_slack_token.py",
    "test_slack_webhook.py",
    "check_slack_app_status.md",
    "CHECK_SLACK_LOGS.md",
    "SLACK_FIX_GUIDE.md",
    "SLACK_TROUBLESHOOTING.md",
    "SLACK_WEBHOOK_DETAILED_GUIDE.md",
    "SLACK_WEBHOOK_SETUP_QUICK.md",
    "WEBHOOK_GITHUB_URL.md",
    "WEBHOOK_SETUP_DETAILED.md",
    "WEBHOOK_SETUP.md",
    
    # Firebase 관련 (6개)
    "firebase_uploader.py",
    "firebase.json",
    "storage.rules",
    "FIREBASE_HOSTING_SETUP.md",
    "FIREBASE_PRIVATE_SETUP.md",
    "FIREBASE_SETUP.md",
    
    # 테스트/임시 파일 (6개)
    "test_github_url.py",
    "clean_git_history.bat",
    "replace_token.ps1",
    "remove_token_simple.ps1",
    "CLEAN_GIT_HISTORY.md",
    "REMOVE_TOKEN_GUIDE.md",
    
    # 기타 (2개)
    ".firebaserc",
    "run_datalab.bat"
)

# 삭제할 폴더 목록
$foldersToDelete = @(
    "public"
)

Write-Host "🗑️  삭제할 파일 목록:" -ForegroundColor Yellow
Write-Host "   - 슬랙 관련: 14개" -ForegroundColor Gray
Write-Host "   - Firebase 관련: 6개" -ForegroundColor Gray
Write-Host "   - 테스트/임시: 6개" -ForegroundColor Gray
Write-Host "   - 기타: 2개" -ForegroundColor Gray
Write-Host "   - 폴더: 1개 (public/)" -ForegroundColor Gray
Write-Host "   ─────────────────────" -ForegroundColor Gray
Write-Host "   총 29개 항목`n" -ForegroundColor Gray

# 사용자 확인
$confirmation = Read-Host "정말 삭제하시겠습니까? (Y/N)"
if ($confirmation -ne "Y" -and $confirmation -ne "y") {
    Write-Host "`n❌ 취소되었습니다." -ForegroundColor Red
    exit 0
}

Write-Host "`n🚀 파일 삭제 시작...`n" -ForegroundColor Green

# 파일 삭제
$deletedCount = 0
$notFoundCount = 0

foreach ($file in $filesToDelete) {
    if (Test-Path $file) {
        Remove-Item $file -Force
        Write-Host "   ✅ 삭제: $file" -ForegroundColor Green
        $deletedCount++
    } else {
        Write-Host "   ⚠️  없음: $file" -ForegroundColor DarkGray
        $notFoundCount++
    }
}

# 폴더 삭제
foreach ($folder in $foldersToDelete) {
    if (Test-Path $folder) {
        Remove-Item $folder -Recurse -Force
        Write-Host "   ✅ 삭제: $folder/" -ForegroundColor Green
        $deletedCount++
    } else {
        Write-Host "   ⚠️  없음: $folder/" -ForegroundColor DarkGray
        $notFoundCount++
    }
}

Write-Host "`n" -NoNewline
Write-Host "╔════════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║                    삭제 완료!                           ║" -ForegroundColor Cyan
Write-Host "╚════════════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""
Write-Host "   ✅ 삭제된 항목: $deletedCount 개" -ForegroundColor Green
Write-Host "   ⚠️  없던 항목: $notFoundCount 개" -ForegroundColor Gray
Write-Host ""

# Git 작업 여부 확인
$gitConfirm = Read-Host "Git에 변경사항을 커밋하시겠습니까? (Y/N)"
if ($gitConfirm -eq "Y" -or $gitConfirm -eq "y") {
    Write-Host "`n📦 Git 작업 시작...`n" -ForegroundColor Green
    
    git add -A
    git commit -m "Clean up unused files before public release"
    
    $pushConfirm = Read-Host "`nGitHub에 푸시하시겠습니까? (Y/N)"
    if ($pushConfirm -eq "Y" -or $pushConfirm -eq "y") {
        git push
        Write-Host "`n✅ GitHub 푸시 완료!" -ForegroundColor Green
    }
}

Write-Host "`n" -NoNewline
Write-Host "╔════════════════════════════════════════════════════════════╗" -ForegroundColor Yellow
Write-Host "║              다음 단계: Public 전환                     ║" -ForegroundColor Yellow
Write-Host "╚════════════════════════════════════════════════════════════╝" -ForegroundColor Yellow
Write-Host ""
Write-Host "1. GitHub 저장소 접속:" -ForegroundColor White
Write-Host "   https://github.com/yujinpung/mlb-naver-datalab-reporter" -ForegroundColor Cyan
Write-Host ""
Write-Host "2. Settings 탭 클릭" -ForegroundColor White
Write-Host ""
Write-Host "3. 하단 'Danger Zone' → 'Change visibility' 클릭" -ForegroundColor White
Write-Host ""
Write-Host "4. 'Change to public' 선택" -ForegroundColor White
Write-Host ""
Write-Host "5. 저장소 이름 입력: mlb-naver-datalab-reporter" -ForegroundColor White
Write-Host ""
Write-Host "6. 'I understand, change repository visibility' 클릭" -ForegroundColor White
Write-Host ""

Write-Host "✅ 모든 작업 완료!" -ForegroundColor Green
Write-Host ""


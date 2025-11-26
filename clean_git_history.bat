@echo off
echo ========================================
echo Git History Cleaner
echo ========================================
echo.
echo WARNING: This will rewrite Git history!
echo.
echo This script will:
echo 1. Remove the exposed Slack token from all Git history
echo 2. Force push to remote repository
echo.
echo Press Ctrl+C to cancel, or
pause

echo.
echo Step 1: Creating backup...
git branch backup-before-cleanup

echo.
echo Step 2: Removing sensitive data from history...
git filter-branch --force --index-filter ^
"git ls-files -z GITHUB_SETUP.md | xargs -0 git rm --cached --ignore-unmatch" ^
--prune-empty --tag-name-filter cat -- --all

echo.
echo Step 3: Cleaning up...
git for-each-ref --format="delete %(refname)" refs/original | git update-ref --stdin
git reflog expire --expire=now --all
git gc --prune=now --aggressive

echo.
echo Step 4: Force pushing to remote...
git push origin --force --all

echo.
echo ========================================
echo Cleanup Complete!
echo ========================================
echo.
echo The backup branch 'backup-before-cleanup' has been created.
echo If something goes wrong, you can restore it with:
echo   git checkout backup-before-cleanup
echo.
pause


@echo off
REM 네이버 데이터랩 자동 리포팅 실행 배치 파일
REM Windows Task Scheduler에서 이 파일을 등록하세요

echo ========================================
echo   Naver Datalab Auto Reporter
echo ========================================
echo.

REM 스크립트 디렉토리로 이동
cd /d "%~dp0"

REM Python 가상환경 활성화 (있는 경우)
if exist "venv\Scripts\activate.bat" (
    echo Activating virtual environment...
    call venv\Scripts\activate.bat
)

REM 메인 스크립트 실행
echo Running main script...
python main.py

REM 결과 출력
if %ERRORLEVEL% EQU 0 (
    echo.
    echo [SUCCESS] Report completed successfully!
) else (
    echo.
    echo [ERROR] Report failed with error code: %ERRORLEVEL%
)

echo.
echo ========================================
echo   Execution finished
echo ========================================

REM 작업 스케줄러에서 실행 시 창이 바로 닫히지 않게 (디버깅용)
REM 실제 운영 시에는 아래 줄 주석 처리
timeout /t 5


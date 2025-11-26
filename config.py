# -*- coding: utf-8 -*-
"""
네이버 데이터랩 자동 리포팅 시스템 - 설정 파일
"""
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

# ==================== 키워드 및 URL 설정 ====================
# 각 키워드별 데이터랩 URL 매핑
# 환경변수가 있으면 우선 사용, 없으면 기본값 사용 (로컬 개발용)
KEYWORD_URLS = {
    "MLB": os.getenv("MLB_URL", "https://datalab.naver.com/keyword/trendResult.naver?hashKey=N_5422d72450d3c367ca4fefc5d74524a3"),
    "MLB키즈": os.getenv("MLB_KIDS_URL", "https://datalab.naver.com/keyword/trendResult.naver?hashKey=N_1e264dc137a94b75c129002965cd45be"),
    "패딩": os.getenv("PADDING_URL", "https://datalab.naver.com/keyword/trendResult.naver?hashKey=N_c5184aac11432a4daed599107c939117"),
    "방한화": os.getenv("WINTER_SHOES_URL", "https://datalab.naver.com/keyword/trendResult.naver?hashKey=N_8118629102d305df645d358077fe350b"),
    "키즈책가방": os.getenv("KIDS_BACKPACK_URL", "https://datalab.naver.com/keyword/trendResult.naver?hashKey=N_41a8388f40e62f71b6f1b2eb1278caeb"),
    "커브러너": os.getenv("CURVE_RUNNER_URL", "https://datalab.naver.com/keyword/trendResult.naver?hashKey=N_5bd081e20a696586c10441cb7b6eb653"),
    "카리나MLB": os.getenv("KARINA_MLB_URL", "https://datalab.naver.com/keyword/trendResult.naver?hashKey=N_f27df0c45f89393aef554251e742698d"),
    "비니": os.getenv("BEANIE_URL", "https://datalab.naver.com/keyword/trendResult.naver?hashKey=N_7e29205ed6bd997bfb3b35416e689bad")
}

# 키워드 리스트 (순서대로 캡처됨)
KEYWORDS = list(KEYWORD_URLS.keys())

# ==================== 날짜 설정 ====================
START_DATE = "2025-01-01"  # 시작일 (고정)
# 종료일은 전일(어제)로 자동 계산

def get_date_range():
    """
    검색 기간 계산
    - 시작일: 2025-01-01 (고정)
    - 종료일: 어제 (전일)
    """
    from datetime import datetime, timedelta
    
    today = datetime.now()
    yesterday = today - timedelta(days=1)
    
    start_date = START_DATE
    end_date = yesterday.strftime("%Y-%m-%d")
    
    return start_date, end_date

# ==================== 데이터랩 검색 조건 ====================
DATALAB_SETTINGS = {
    "device": "",        # 전체 (빈 문자열 = MO/PC 전체)
    "gender": "",        # 전체 (빈 문자열 = 전체)
    "age": "",           # 전체 (빈 문자열 = 전체)
}

# 네이버 데이터랩 URL 가져오기 함수
def get_datalab_url(keyword):
    """
    특정 키워드의 데이터랩 URL 반환
    """
    return KEYWORD_URLS.get(keyword, KEYWORD_URLS[KEYWORDS[0]])

# ==================== GitHub 설정 ====================
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME", "yujinpung")
GITHUB_REPO = os.getenv("GITHUB_REPO", "mlb-naver-datalab-reporter")
GITHUB_BRANCH = os.getenv("GITHUB_BRANCH", "main")

# GitHub Raw URL 생성 함수
def get_github_raw_url(filename):
    """
    GitHub Raw 파일 URL 생성
    예: https://raw.githubusercontent.com/yujinpung/mlb-naver-datalab-reporter/main/screenshots/NaverDatalab_2025-11-26_MLB.png
    """
    return f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{GITHUB_REPO}/{GITHUB_BRANCH}/screenshots/{filename}"

# GitHub Pages URL 생성 함수
def get_github_pages_url(filename):
    """
    GitHub Pages 파일 URL 생성
    예: https://yujinpung.github.io/mlb-naver-datalab-reporter/screenshots/NaverDatalab_2025-11-26_MLB.png
    """
    return f"https://{GITHUB_USERNAME}.github.io/{GITHUB_REPO}/screenshots/{filename}"

# ==================== 슬랙 설정 ====================
SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL", "")
SLACK_CHANNEL = os.getenv("SLACK_CHANNEL", "#datalab-report")

# ==================== 파일 저장 설정 ====================
OUTPUT_DIR = "screenshots"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 파일명 포맷: NaverDatalab_2025-11-15_MLB_MLB키즈_모자_패딩.png
def get_filename(keyword=None):
    """
    파일명 생성: NaverDatalab_2025-11-14_MLB.png
    데이터 수집 종료일(전일)을 파일명으로 사용
    """
    from datetime import timedelta
    
    # 전일(어제) 날짜 = 데이터가 수집된 마지막 날
    yesterday = datetime.now() - timedelta(days=1)
    date_str = yesterday.strftime("%Y-%m-%d")
    
    # 키워드가 지정되지 않으면 첫 번째 키워드 사용
    main_keyword = keyword if keyword else (KEYWORDS[0] if KEYWORDS else "trend")
    return f"NaverDatalab_{date_str}_{main_keyword}.png"

# ==================== 브라우저 설정 ====================
HEADLESS_MODE = True  # True: 백그라운드 실행, False: 브라우저 보이게
BROWSER_TIMEOUT = 30000  # 30초

# ==================== 로그 설정 ====================
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

def get_log_filename():
    date_str = datetime.now().strftime("%Y-%m-%d")
    return os.path.join(LOG_DIR, f"datalab_{date_str}.log")

# ==================== 재시도 설정 ====================
MAX_RETRIES = 3
RETRY_DELAY = 5  # 초

# ==================== 이미지 히스토리 관리 ====================
KEEP_HISTORY_DAYS = 30  # 30일 이상 된 파일 자동 삭제


# -*- coding: utf-8 -*-
"""
GitHub Raw URL 생성 테스트 스크립트
"""
import os
import sys
from datetime import datetime, timedelta
import config

# UTF-8 인코딩 설정 (Windows)
if sys.platform == 'win32':
    os.system('chcp 65001 > nul')
    sys.stdout.reconfigure(encoding='utf-8')

def test_github_url_generation():
    """GitHub Raw URL 생성 테스트"""
    print("=" * 70)
    print("  GitHub Raw URL 생성 테스트")
    print("=" * 70)
    print()
    
    # 1. 설정 확인
    print("1️⃣ GitHub 설정 확인")
    print(f"   - Username: {config.GITHUB_USERNAME}")
    print(f"   - Repository: {config.GITHUB_REPO}")
    print(f"   - Branch: {config.GITHUB_BRANCH}")
    print()
    
    # 2. 어제 날짜 계산
    yesterday = datetime.now() - timedelta(days=1)
    date_str = yesterday.strftime("%Y-%m-%d")
    print(f"2️⃣ 날짜 정보")
    print(f"   - 어제: {date_str}")
    print()
    
    # 3. 각 키워드별 GitHub Raw URL 생성
    print("3️⃣ GitHub Raw URL 생성")
    print()
    
    for i, keyword in enumerate(config.KEYWORDS, 1):
        # 파일명 생성
        filename = f"NaverDatalab_{date_str}_{keyword}.png"
        
        # GitHub Raw URL 생성
        raw_url = config.get_github_raw_url(filename)
        
        # GitHub Pages URL 생성
        pages_url = config.get_github_pages_url(filename)
        
        print(f"{i}. {keyword}")
        print(f"   📄 파일명: {filename}")
        print(f"   🔗 Raw URL: {raw_url}")
        print(f"   🌐 Pages URL: {pages_url}")
        print()
    
    # 4. URL 복사 안내
    print("=" * 70)
    print("✅ URL 생성 완료!")
    print()
    print("💡 사용 방법:")
    print("   1. GitHub Actions 실행 후 스크린샷이 커밋되면 Raw URL 사용 가능")
    print("   2. 슬랙 Webhook이 자동으로 Raw URL을 사용하여 이미지 전송")
    print("   3. 대시보드에서는 Pages URL 또는 상대 경로 사용")
    print()
    print("🔍 URL 테스트:")
    print("   브라우저에서 위 URL을 열어 이미지가 보이는지 확인하세요.")
    print("=" * 70)

if __name__ == "__main__":
    test_github_url_generation()


# -*- coding: utf-8 -*-
"""
네이버 데이터랩 자동 캡처 시스템 - 메인 실행 스크립트
"""
import asyncio
import logging
import os
from datetime import datetime, timedelta
from pathlib import Path

import config
from datalab_scraper import NaverDatalabScraper

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(config.get_log_filename(), encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)



def clean_old_screenshots():
    """오래된 스크린샷 파일 삭제"""
    try:
        screenshot_dir = Path(config.OUTPUT_DIR)
        if not screenshot_dir.exists():
            return
        
        cutoff_date = datetime.now() - timedelta(days=config.KEEP_HISTORY_DAYS)
        deleted_count = 0
        
        for file_path in screenshot_dir.glob("*.png"):
            file_time = datetime.fromtimestamp(file_path.stat().st_mtime)
            if file_time < cutoff_date:
                file_path.unlink()
                deleted_count += 1
                logger.info(f"오래된 파일 삭제: {file_path.name}")
        
        if deleted_count > 0:
            logger.info(f"총 {deleted_count}개 파일 삭제 완료")
            
    except Exception as e:
        logger.warning(f"파일 정리 중 오류 (무시): {str(e)}")


async def run_datalab_capture():
    """
    데이터랩 스크린샷 캡처 실행 (재시도 로직 포함)
    - 모든 키워드를 순차적으로 캡처
    """
    all_screenshots = []
    
    for attempt in range(1, config.MAX_RETRIES + 1):
        try:
            logger.info(f"\n{'='*60}")
            logger.info(f"  네이버 데이터랩 자동 캡처 시작 (시도 {attempt}/{config.MAX_RETRIES})")
            logger.info(f"  키워드: {', '.join(config.KEYWORDS)}")
            logger.info(f"{'='*60}\n")
            
            # 1. 네이버 데이터랩 캡처 (모든 키워드)
            logger.info("📸 STEP 1: 네이버 데이터랩 스크린샷 캡처")
            scraper = NaverDatalabScraper()
            results = await scraper.run_all_keywords()
            
            # 성공한 스크린샷만 필터링
            all_screenshots = [r for r in results if r['success']]
            
            # 캡처 성공 확인
            if not all_screenshots:
                raise Exception("모든 키워드 캡처 실패")
            
            logger.info(f"\n✅ 총 {len(all_screenshots)}개 키워드 캡처 완료:")
            for result in all_screenshots:
                if os.path.exists(result['path']):
                    file_size = os.path.getsize(result['path']) / 1024
                    logger.info(f"   - {result['keyword']}: {result['path']} ({file_size:.1f} KB)")
            
            # 2. 오래된 파일 정리
            logger.info("\n🧹 STEP 2: 오래된 스크린샷 정리")
            clean_old_screenshots()
            
            # 성공
            logger.info(f"\n{'='*60}")
            logger.info("  ✅ 모든 작업 완료!")
            logger.info(f"{'='*60}\n")
            
            return True
            
        except Exception as e:
            logger.error(f"\n❌ 실행 실패 (시도 {attempt}/{config.MAX_RETRIES}): {str(e)}")
            
            # 마지막 시도가 아니면 재시도
            if attempt < config.MAX_RETRIES:
                logger.info(f"⏳ {config.RETRY_DELAY}초 후 재시도...")
                import time
                time.sleep(config.RETRY_DELAY)
            else:
                # 모든 시도 실패
                logger.error("❌ 모든 재시도 실패")
                return False
    
    return False


def main():
    """메인 실행 함수"""
    start_time = datetime.now()
    logger.info(f"\n{'#'*60}")
    logger.info(f"  네이버 데이터랩 자동 캡처 시스템")
    logger.info(f"  시작 시각: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info(f"{'#'*60}\n")
    
    # 비동기 실행
    success = asyncio.run(run_datalab_capture())
    
    # 실행 시간 계산
    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds()
    
    logger.info(f"\n{'#'*60}")
    logger.info(f"  종료 시각: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info(f"  소요 시간: {duration:.1f}초")
    logger.info(f"  결과: {'✅ 성공' if success else '❌ 실패'}")
    logger.info(f"{'#'*60}\n")
    
    return 0 if success else 1


if __name__ == "__main__":
    exit(main())


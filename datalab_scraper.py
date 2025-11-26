# -*- coding: utf-8 -*-
"""
네이버 데이터랩 스크래핑 모듈
Playwright를 사용한 자동 캡처
"""
import asyncio
import logging
from datetime import datetime
from playwright.async_api import async_playwright
import config

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


class NaverDatalabScraper:
    """네이버 데이터랩 자동 스크래핑 클래스"""
    
    def __init__(self, keyword=None):
        self.keywords = config.KEYWORDS
        self.current_keyword = keyword  # 현재 캡처할 키워드
        self.output_path = None
        self.start_date, self.end_date = config.get_date_range()
        
    def build_datalab_url(self, keyword=None):
        """
        키워드별 네이버 데이터랩 URL 반환
        - 기간: 2025-01-01 ~ 전일
        - 범위: MO/PC 전체
        - 성별: 전체
        - 연령: 전체
        """
        keyword = keyword or self.current_keyword or self.keywords[0]
        return config.get_datalab_url(keyword)
    
    async def capture_datalab(self, keyword=None):
        """
        네이버 데이터랩 페이지 접속 및 그래프 캡처
        """
        keyword = keyword or self.current_keyword
        
        try:
            logger.info("=" * 50)
            logger.info(f"네이버 데이터랩 캡처: {keyword}")
            logger.info(f"기간: {self.start_date} ~ {self.end_date} (전일까지)")
            logger.info(f"범위: MO/PC 전체 | 성별: 전체 | 연령: 전체")
            logger.info("=" * 50)
            
            async with async_playwright() as p:
                # 브라우저 실행
                browser = await p.chromium.launch(
                    headless=config.HEADLESS_MODE,
                    args=['--start-maximized']
                )
                
                # 새 페이지 생성 (최대화 상태)
                context = await browser.new_context(
                    viewport={'width': 1920, 'height': 1080}
                )
                page = await context.new_page()
                
                # 타임아웃 설정
                page.set_default_timeout(config.BROWSER_TIMEOUT)
                
                logger.info(f"네이버 데이터랩 페이지 접속 중: {keyword}")
                
                # 네이버 데이터랩 접속 (키워드별 URL)
                url = self.build_datalab_url(keyword)
                await page.goto(url)
                
                # 페이지 로딩 대기
                await page.wait_for_load_state('networkidle')
                await asyncio.sleep(2)
                
                # URL에 이미 검색 조건이 포함되어 있으므로 바로 그래프 로딩 대기
                logger.info("📊 그래프 페이지 로딩 중...")
                logger.info(f"📅 조회 기간: {self.start_date} ~ {self.end_date} (전일까지)")
                logger.info(f"🔍 키워드: {keyword}")
                
                try:
                    # 그래프 로딩 대기
                    logger.info("⏳ 그래프 데이터 로딩 중...")
                    await asyncio.sleep(3)
                    
                    # 그래프 영역이 나타날 때까지 대기
                    graph_selectors = [
                        '.chart_area',
                        '#content_chart',
                        '.graph_area',
                        'canvas',
                        'svg'
                    ]
                    
                    for selector in graph_selectors:
                        try:
                            await page.wait_for_selector(selector, timeout=5000)
                            logger.info(f"✓ 그래프 영역 감지됨: {selector}")
                            break
                        except:
                            continue
                    
                    # 추가 로딩 대기
                    await asyncio.sleep(2)
                    logger.info("✓ 그래프 로딩 완료!")
                    
                except Exception as e:
                    logger.error(f"❌ 검색 조건 설정 중 오류: {str(e)}")
                    logger.warning("현재 페이지 상태로 캡처를 진행합니다.")
                    await asyncio.sleep(2)
                
                # 스크린샷 경로 설정 (키워드별)
                self.output_path = config.get_filename(keyword)
                full_path = f"{config.OUTPUT_DIR}/{self.output_path}"
                
                logger.info(f"📸 스크린샷 캡처 중: {full_path}")
                
                # 그래프 영역만 캡처 시도
                graph_captured = False
                graph_area_selectors = [
                    '.chart_area',
                    '#content_chart', 
                    '.graph_area',
                    '#chart_div',
                    '.result_area'
                ]
                
                for selector in graph_area_selectors:
                    try:
                        graph_element = await page.query_selector(selector)
                        if graph_element and await graph_element.is_visible():
                            await graph_element.screenshot(path=full_path)
                            logger.info(f"✓ 그래프 영역 캡처 완료: {selector}")
                            graph_captured = True
                            break
                    except:
                        continue
                
                # 그래프 영역을 찾지 못한 경우 전체 페이지 캡처
                if not graph_captured:
                    logger.warning("⚠️  그래프 영역을 찾지 못해 전체 페이지 캡처")
                    await page.screenshot(path=full_path, full_page=True)
                
                logger.info("✅ 스크린샷 캡처 완료!")
                
                # 브라우저 종료
                await browser.close()
                
                return full_path
                
        except Exception as e:
            logger.error(f"❌ 캡처 실패: {str(e)}")
            raise
    
    async def run(self, keyword=None):
        """실행 메인 함수"""
        return await self.capture_datalab(keyword)
    
    async def run_all_keywords(self):
        """모든 키워드에 대해 순차 실행"""
        results = []
        for keyword in self.keywords:
            try:
                logger.info(f"\n{'='*60}")
                logger.info(f"  키워드 '{keyword}' 처리 중...")
                logger.info(f"{'='*60}")
                screenshot_path = await self.capture_datalab(keyword)
                results.append({
                    'keyword': keyword,
                    'success': True,
                    'path': screenshot_path
                })
                # 키워드 간 대기 (너무 빠르면 차단될 수 있음)
                await asyncio.sleep(2)
            except Exception as e:
                logger.error(f"❌ 키워드 '{keyword}' 캡처 실패: {str(e)}")
                results.append({
                    'keyword': keyword,
                    'success': False,
                    'error': str(e)
                })
        return results


async def main():
    """테스트용 메인 함수"""
    scraper = NaverDatalabScraper()
    screenshot_path = await scraper.run()
    print(f"캡처 완료: {screenshot_path}")


if __name__ == "__main__":
    asyncio.run(main())


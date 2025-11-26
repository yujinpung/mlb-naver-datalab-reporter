# -*- coding: utf-8 -*-
"""
슬랙 메시지 전송 모듈
"""
import logging
import os
from datetime import datetime
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from slack_sdk.webhook import WebhookClient
import config

logger = logging.getLogger(__name__)


class SlackSender:
    """슬랙 메시지 전송 클래스"""
    
    def __init__(self):
        self.webhook_url = config.SLACK_WEBHOOK_URL
        self.channel = config.SLACK_CHANNEL
        self.bot_token = os.getenv("SLACK_BOT_TOKEN")
        
        # Webhook 또는 Bot Token 중 하나는 필수
        if not self.webhook_url and not self.bot_token:
            raise ValueError("SLACK_WEBHOOK_URL 또는 SLACK_BOT_TOKEN이 설정되어야 합니다. .env 파일을 확인하세요.")
    
    def send_image(self, image_path=None, image_url=None, message=None):
        """
        이미지를 슬랙으로 전송
        - Bot Token이 있으면 이미지 파일 직접 업로드
        - Webhook만 있으면 이미지 URL을 포함한 메시지 전송
        """
        try:
            # Bot Token이 있으면 이미지 파일 직접 업로드
            if self.bot_token and image_path:
                return self.send_image_with_bot(image_path, self.bot_token, message)
            
            # Webhook으로 메시지 전송 (이미지 URL 포함)
            if not self.webhook_url:
                logger.warning("Webhook URL이 없어 메시지 전송 불가")
                return False
            
            if not message:
                from datetime import timedelta
                today = datetime.now()
                yesterday = today - timedelta(days=1)
                
                keywords_text = " / ".join(config.KEYWORDS)
                start_date, end_date = config.get_date_range()
                
                message = f"📊 네이버 검색 트렌드 리포트\n"
                message += f"📅 기간: {start_date} ~ {end_date}\n"
                message += f"🔍 키워드: {keywords_text}\n"
                message += f"📱 범위: MO/PC 전체 | 성별/연령: 전체"
            
            # Webhook 방식
            webhook = WebhookClient(self.webhook_url)
            
            # 블록 구성
            blocks = [
                {
                    "type": "header",
                    "text": {
                        "type": "plain_text",
                        "text": "📊 네이버 데이터랩 일일 리포트",
                        "emoji": True
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": message
                    }
                }
            ]
            
            # 이미지 URL이 있으면 이미지 블록 추가
            if image_url:
                blocks.append({
                    "type": "image",
                    "image_url": image_url,
                    "alt_text": "네이버 검색 트렌드 그래프"
                })
            
            blocks.append({
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": f"생성 시각: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
                    }
                ]
            })
            
            # 메시지 전송
            response = webhook.send(
                text=message,
                blocks=blocks
            )
            
            if image_url:
                logger.info(f"✅ 슬랙 메시지 전송 완료 (이미지 URL 포함)")
            else:
                logger.info(f"✅ 슬랙 메시지 전송 완료 (텍스트만)")
            
            return True
            
        except Exception as e:
            logger.error(f"❌ 슬랙 전송 실패: {str(e)}")
            return False
    
    def send_image_with_bot(self, image_path, bot_token, message=None):
        """
        Bot Token을 사용한 이미지 업로드
        
        Bot Token 생성 방법:
        1. https://api.slack.com/apps 접속
        2. 앱 생성
        3. OAuth & Permissions > Bot Token Scopes 추가:
           - chat:write
           - files:write
        4. Install to Workspace
        5. Bot User OAuth Token 복사
        """
        try:
            client = WebClient(token=bot_token)
            
            if not message:
                from datetime import timedelta
                today = datetime.now()
                yesterday = today - timedelta(days=1)
                
                keywords_text = " / ".join(config.KEYWORDS)
                start_date, end_date = config.get_date_range()
                
                message = f"📊 네이버 검색 트렌드 리포트\n"
                message += f"📅 {start_date} ~ {end_date}\n"
                message += f"🔍 {keywords_text}"
            
            # 파일 업로드
            import os as os_module
            filename = os_module.path.basename(image_path)
            
            # channels는 문자열 또는 리스트로 전달
            channel_param = self.channel if isinstance(self.channel, list) else [self.channel]
            
            # 메시지를 UTF-8로 명시적으로 인코딩
            if isinstance(message, str):
                message = message.encode('utf-8').decode('utf-8')
            
            response = client.files_upload_v2(
                channels=channel_param,
                file=image_path,
                filename=filename,
                initial_comment=message
            )
            
            logger.info(f"✅ 슬랙 이미지 업로드 완료: {self.channel}")
            return True
            
        except SlackApiError as e:
            logger.error(f"❌ 슬랙 API 오류: {e.response['error']}")
            return False
        except Exception as e:
            logger.error(f"❌ 슬랙 전송 실패: {str(e)}")
            return False
    
    def send_error_notification(self, error_message):
        """에러 알림 전송"""
        try:
            webhook = WebhookClient(self.webhook_url)
            
            message = f"⚠️ 네이버 데이터랩 자동 리포팅 실패\n\n```{error_message}```"
            
            webhook.send(
                text=message,
                blocks=[
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": message
                        }
                    }
                ]
            )
            
            logger.info("에러 알림 전송 완료")
            return True
            
        except Exception as e:
            logger.error(f"에러 알림 전송 실패: {str(e)}")
            return False


def main():
    """테스트용 메인 함수"""
    sender = SlackSender()
    
    # 테스트 메시지 전송
    result = sender.send_image(
        image_path="test.png",
        message="테스트 메시지입니다."
    )
    
    if result:
        print("✅ 슬랙 전송 성공")
    else:
        print("❌ 슬랙 전송 실패")


if __name__ == "__main__":
    main()


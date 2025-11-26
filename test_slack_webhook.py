# -*- coding: utf-8 -*-
"""
슬랙 Webhook 테스트 스크립트
GitHub Secrets 환경변수 확인용
"""
import os
import sys

# UTF-8 인코딩 설정 (Windows)
if sys.platform == 'win32':
    os.system('chcp 65001 > nul')
    sys.stdout.reconfigure(encoding='utf-8')

def test_webhook():
    """Webhook URL 및 환경변수 확인"""
    print("=" * 70)
    print("  슬랙 Webhook 테스트")
    print("=" * 70)
    print()
    
    # 1. 환경변수 확인
    print("1️⃣ 환경변수 확인")
    webhook_url = os.getenv("SLACK_WEBHOOK_URL", "")
    bot_token = os.getenv("SLACK_BOT_TOKEN", "")
    channel = os.getenv("SLACK_CHANNEL", "#mlb-naver-datalab-reporter")
    
    print(f"   SLACK_WEBHOOK_URL: ", end="")
    if webhook_url:
        print(f"✅ 설정됨 (길이: {len(webhook_url)}자)")
        print(f"      시작: {webhook_url[:30]}...")
        print(f"      형식: ", end="")
        if webhook_url.startswith("https://hooks.slack.com/services/"):
            print("✅ 올바름")
        else:
            print("❌ 잘못됨 (https://hooks.slack.com/services/로 시작해야 함)")
    else:
        print("❌ 설정되지 않음")
    print()
    
    print(f"   SLACK_BOT_TOKEN: ", end="")
    if bot_token:
        print(f"✅ 설정됨 (길이: {len(bot_token)}자)")
        print(f"      시작: {bot_token[:20]}...")
    else:
        print("❌ 설정되지 않음")
    print()
    
    print(f"   SLACK_CHANNEL: {channel}")
    print()
    
    # 2. 필수 조건 확인
    print("2️⃣ 필수 조건 확인")
    if webhook_url or bot_token:
        print("   ✅ WEBHOOK_URL 또는 BOT_TOKEN 중 하나 설정됨")
    else:
        print("   ❌ WEBHOOK_URL 또는 BOT_TOKEN이 필요합니다!")
        print("   💡 GitHub Secrets에 SLACK_WEBHOOK_URL을 등록하세요")
        return False
    print()
    
    # 3. Webhook 테스트 메시지 전송
    if webhook_url:
        print("3️⃣ Webhook 테스트 메시지 전송")
        try:
            from slack_sdk.webhook import WebhookClient
            
            webhook = WebhookClient(webhook_url)
            response = webhook.send(
                text="🧪 테스트 메시지입니다!",
                blocks=[
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "*🧪 슬랙 Webhook 테스트*\n\n이 메시지가 보인다면 Webhook이 정상적으로 작동합니다!"
                        }
                    }
                ]
            )
            
            if response.status_code == 200:
                print("   ✅ 테스트 메시지 전송 성공!")
                print("   💡 슬랙 채널에서 메시지를 확인하세요")
                return True
            else:
                print(f"   ❌ 전송 실패: HTTP {response.status_code}")
                print(f"   응답: {response.body}")
                return False
                
        except Exception as e:
            print(f"   ❌ 오류 발생: {str(e)}")
            return False
    
    print()
    print("=" * 70)
    print("  테스트 완료")
    print("=" * 70)
    return True

if __name__ == "__main__":
    success = test_webhook()
    sys.exit(0 if success else 1)


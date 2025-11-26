# -*- coding: utf-8 -*-
"""
Slack Bot Token 유효성 검사 스크립트
"""
import os
import sys
from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# UTF-8 인코딩 설정 (Windows)
if sys.platform == 'win32':
    os.system('chcp 65001 > nul')
    sys.stdout.reconfigure(encoding='utf-8')

# .env 파일 로드
load_dotenv()

def test_slack_token():
    """Slack Bot Token 유효성 검사"""
    bot_token = os.getenv("SLACK_BOT_TOKEN")
    
    if not bot_token:
        print("❌ SLACK_BOT_TOKEN이 .env 파일에 설정되지 않았습니다.")
        return False
    
    print(f"🔍 토큰 확인 중...")
    print(f"   토큰 앞 20자: {bot_token[:20]}...")
    print()
    
    try:
        client = WebClient(token=bot_token)
        
        # 1. auth.test API로 토큰 유효성 확인
        print("1️⃣ auth.test API 호출 중...")
        auth_response = client.auth_test()
        
        print(f"✅ 토큰 유효성 확인 성공!")
        print(f"   워크스페이스: {auth_response['team']}")
        print(f"   사용자: {auth_response['user']}")
        print(f"   Bot ID: {auth_response['bot_id']}")
        print()
        
        # 2. conversations.list로 채널 목록 확인
        print("2️⃣ 채널 목록 확인 중...")
        channels_response = client.conversations_list(types="public_channel,private_channel")
        
        channel_names = [ch['name'] for ch in channels_response['channels']]
        print(f"✅ 접근 가능한 채널 수: {len(channel_names)}")
        print(f"   채널 목록: {', '.join(channel_names[:10])}")
        print()
        
        # 3. 특정 채널 확인
        target_channel = os.getenv("SLACK_CHANNEL", "#mlb-naver-datalab-reporter")
        print(f"3️⃣ 대상 채널 확인: {target_channel}")
        
        # 채널 이름에서 # 제거
        channel_name = target_channel.lstrip('#')
        
        # 채널 찾기
        found_channel = None
        for channel in channels_response['channels']:
            if channel['name'] == channel_name:
                found_channel = channel
                break
        
        if found_channel:
            print(f"✅ 채널 발견: #{found_channel['name']}")
            print(f"   채널 ID: {found_channel['id']}")
            print(f"   멤버 수: {found_channel.get('num_members', 'N/A')}")
            
            # Bot이 채널에 있는지 확인
            if found_channel.get('is_member'):
                print(f"   ✅ Bot이 채널 멤버입니다")
            else:
                print(f"   ⚠️  Bot이 채널 멤버가 아닙니다. 채널에 초대해주세요.")
        else:
            print(f"❌ 채널을 찾을 수 없습니다: {target_channel}")
            print(f"   채널이 존재하는지, Bot이 접근 권한이 있는지 확인하세요.")
        
        return True
        
    except SlackApiError as e:
        error_code = e.response['error']
        print(f"❌ Slack API 오류 발생!")
        print(f"   오류 코드: {error_code}")
        print(f"   오류 메시지: {e.response.get('error_description', 'N/A')}")
        print()
        
        if error_code == 'account_inactive':
            print("🔍 'account_inactive' 오류 원인:")
            print("   1. Bot Token이 만료되었거나 비활성화됨")
            print("   2. Bot이 워크스페이스에서 제거됨")
            print("   3. 앱이 워크스페이스에서 제거됨")
            print()
            print("💡 해결 방법:")
            print("   1. https://api.slack.com/apps 접속")
            print("   2. 해당 앱 선택")
            print("   3. 'OAuth & Permissions' 탭 확인")
            print("   4. 'Reinstall to Workspace' 클릭하여 재설치")
            print("   5. 새로운 Bot Token 생성 후 .env 파일 업데이트")
        
        return False
        
    except Exception as e:
        print(f"❌ 예상치 못한 오류: {str(e)}")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("  Slack Bot Token 유효성 검사")
    print("=" * 60)
    print()
    
    test_slack_token()
    
    print()
    print("=" * 60)


# -*- coding: utf-8 -*-
"""
슬랙 전송 문제 진단 스크립트
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

def check_slack_config():
    """슬랙 설정 확인"""
    print("=" * 60)
    print("  슬랙 전송 문제 진단")
    print("=" * 60)
    print()
    
    # 1. 환경변수 확인
    print("1️⃣ 환경변수 확인")
    bot_token = os.getenv("SLACK_BOT_TOKEN")
    channel = os.getenv("SLACK_CHANNEL", "#mlb-naver-datalab-reporter")
    
    if bot_token:
        print(f"   ✅ SLACK_BOT_TOKEN: {bot_token[:20]}...")
    else:
        print(f"   ❌ SLACK_BOT_TOKEN: 없음")
    
    print(f"   ✅ SLACK_CHANNEL: {channel}")
    print()
    
    # 2. Bot Token 유효성 확인
    if not bot_token:
        print("❌ SLACK_BOT_TOKEN이 설정되지 않았습니다.")
        print("   GitHub Secrets에 SLACK_BOT_TOKEN이 등록되어 있는지 확인하세요.")
        return False
    
    print("2️⃣ Bot Token 유효성 확인")
    try:
        client = WebClient(token=bot_token)
        auth_response = client.auth_test()
        print(f"   ✅ 토큰 유효: {auth_response['team']} / {auth_response['user']}")
    except SlackApiError as e:
        error_code = e.response['error']
        print(f"   ❌ 토큰 오류: {error_code}")
        if error_code == 'account_inactive':
            print("   💡 Bot Token이 비활성화되었습니다.")
            print("   💡 https://api.slack.com/apps 에서 앱을 재설치하세요.")
        return False
    except Exception as e:
        print(f"   ❌ 예상치 못한 오류: {str(e)}")
        return False
    print()
    
    # 3. 채널 확인
    print("3️⃣ 채널 확인")
    try:
        client = WebClient(token=bot_token)
        
        # 채널 이름에서 # 제거
        channel_name = channel.lstrip('#')
        
        # 채널 목록 가져오기
        channels_response = client.conversations_list(types="public_channel,private_channel")
        
        found_channel = None
        for ch in channels_response['channels']:
            if ch['name'] == channel_name:
                found_channel = ch
                break
        
        if found_channel:
            print(f"   ✅ 채널 발견: #{found_channel['name']}")
            print(f"   채널 ID: {found_channel['id']}")
            
            # Bot이 채널 멤버인지 확인
            if found_channel.get('is_member'):
                print(f"   ✅ Bot이 채널 멤버입니다")
            else:
                print(f"   ⚠️  Bot이 채널 멤버가 아닙니다!")
                print(f"   💡 슬랙 채널에서 Bot을 초대하세요: /invite @[Bot이름]")
                return False
        else:
            print(f"   ❌ 채널을 찾을 수 없습니다: #{channel_name}")
            print(f"   💡 채널이 존재하는지, Bot이 접근 권한이 있는지 확인하세요.")
            return False
    except SlackApiError as e:
        print(f"   ❌ API 오류: {e.response['error']}")
        return False
    except Exception as e:
        print(f"   ❌ 예상치 못한 오류: {str(e)}")
        return False
    print()
    
    # 4. 테스트 메시지 전송
    print("4️⃣ 테스트 메시지 전송")
    try:
        client = WebClient(token=bot_token)
        
        # 채널 ID 가져오기
        channel_name = channel.lstrip('#')
        channels_response = client.conversations_list(types="public_channel,private_channel")
        channel_id = None
        for ch in channels_response['channels']:
            if ch['name'] == channel_name:
                channel_id = ch['id']
                break
        
        if not channel_id:
            print("   ❌ 채널 ID를 찾을 수 없습니다.")
            return False
        
        # 테스트 메시지 전송
        response = client.chat_postMessage(
            channel=channel_id,
            text="🧪 슬랙 전송 테스트 메시지입니다."
        )
        
        if response['ok']:
            print(f"   ✅ 테스트 메시지 전송 성공!")
            print(f"   💡 슬랙 채널에서 메시지를 확인하세요.")
        else:
            print(f"   ❌ 메시지 전송 실패: {response.get('error', 'Unknown')}")
            return False
    except SlackApiError as e:
        print(f"   ❌ API 오류: {e.response['error']}")
        if e.response['error'] == 'channel_not_found':
            print("   💡 채널을 찾을 수 없습니다. 채널 이름을 확인하세요.")
        elif e.response['error'] == 'not_in_channel':
            print("   💡 Bot이 채널에 없습니다. 채널에 Bot을 초대하세요.")
        return False
    except Exception as e:
        print(f"   ❌ 예상치 못한 오류: {str(e)}")
        return False
    print()
    
    print("=" * 60)
    print("  ✅ 모든 확인 완료!")
    print("=" * 60)
    return True

if __name__ == "__main__":
    check_slack_config()


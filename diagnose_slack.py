# -*- coding: utf-8 -*-
"""
슬랙 전송 문제 진단 스크립트 (GitHub Actions 환경 시뮬레이션)
"""
import os
import sys

# UTF-8 인코딩 설정 (Windows)
if sys.platform == 'win32':
    os.system('chcp 65001 > nul')
    sys.stdout.reconfigure(encoding='utf-8')

def diagnose_slack_issue():
    """슬랙 전송 문제 진단"""
    print("=" * 60)
    print("  슬랙 전송 문제 진단")
    print("=" * 60)
    print()
    
    # 1. 환경변수 확인
    print("1️⃣ 환경변수 확인")
    webhook_url = os.getenv("SLACK_WEBHOOK_URL", "")
    bot_token = os.getenv("SLACK_BOT_TOKEN", "")
    channel = os.getenv("SLACK_CHANNEL", "#mlb-naver-datalab-reporter")
    
    print(f"   SLACK_WEBHOOK_URL: {'✅ 설정됨' if webhook_url else '❌ 없음'}")
    if webhook_url:
        print(f"      앞 30자: {webhook_url[:30]}...")
    
    print(f"   SLACK_BOT_TOKEN: {'✅ 설정됨' if bot_token else '❌ 없음'}")
    if bot_token:
        print(f"      앞 20자: {bot_token[:20]}...")
    
    print(f"   SLACK_CHANNEL: {channel}")
    print()
    
    # 2. 필수 설정 확인
    print("2️⃣ 필수 설정 확인")
    if not webhook_url and not bot_token:
        print("   ❌ SLACK_WEBHOOK_URL 또는 SLACK_BOT_TOKEN이 필요합니다!")
        print("   💡 GitHub Secrets에 다음 중 하나를 등록하세요:")
        print("      - SLACK_WEBHOOK_URL (추천)")
        print("      - SLACK_BOT_TOKEN")
        return False
    else:
        print("   ✅ 필수 설정 완료")
    print()
    
    # 3. Webhook URL 유효성 확인
    if webhook_url:
        print("3️⃣ Webhook URL 유효성 확인")
        if webhook_url.startswith("https://hooks.slack.com/services/"):
            print("   ✅ Webhook URL 형식 올바름")
        else:
            print("   ⚠️  Webhook URL 형식이 올바르지 않을 수 있습니다")
            print("   💡 올바른 형식: https://hooks.slack.com/services/T.../B.../...")
        print()
    
    # 4. Bot Token 유효성 확인
    if bot_token:
        print("4️⃣ Bot Token 유효성 확인")
        if bot_token.startswith("xoxb-"):
            print("   ✅ Bot Token 형식 올바름")
        else:
            print("   ⚠️  Bot Token 형식이 올바르지 않을 수 있습니다")
            print("   💡 올바른 형식: xoxb-...")
        print()
    
    # 5. Firebase Storage 확인 (이미지 전송용)
    print("5️⃣ Firebase Storage 설정 확인 (이미지 전송용)")
    firebase_bucket = os.getenv("FIREBASE_STORAGE_BUCKET", "")
    firebase_creds = os.getenv("FIREBASE_CREDENTIALS_JSON", "")
    
    if firebase_bucket:
        print(f"   ✅ FIREBASE_STORAGE_BUCKET: {firebase_bucket}")
    else:
        print("   ⚠️  FIREBASE_STORAGE_BUCKET: 없음")
        print("   💡 Webhook 방식 사용 시 이미지 전송을 위해 Firebase Storage가 필요합니다")
    
    if firebase_creds:
        print("   ✅ FIREBASE_CREDENTIALS_JSON: 설정됨")
    else:
        print("   ⚠️  FIREBASE_CREDENTIALS_JSON: 없음")
    print()
    
    # 6. 권장 설정 확인
    print("6️⃣ 권장 설정 확인")
    if webhook_url and firebase_bucket:
        print("   ✅ 권장 설정 완료 (Webhook + Firebase Storage)")
        print("   💡 이미지를 포함한 메시지를 전송할 수 있습니다")
    elif webhook_url and not firebase_bucket:
        print("   ⚠️  Webhook만 설정됨 (Firebase Storage 없음)")
        print("   💡 텍스트 메시지만 전송됩니다")
        print("   💡 이미지를 전송하려면 Firebase Storage를 설정하세요")
    elif bot_token:
        print("   ✅ Bot Token 설정됨")
        print("   💡 이미지 파일을 직접 업로드할 수 있습니다")
    print()
    
    # 7. 종합 진단
    print("=" * 60)
    print("  종합 진단 결과")
    print("=" * 60)
    
    if not webhook_url and not bot_token:
        print("❌ 슬랙 전송 불가: Webhook URL 또는 Bot Token이 필요합니다")
        print()
        print("💡 해결 방법:")
        print("   1. GitHub Secrets에 SLACK_WEBHOOK_URL 등록")
        print("   2. 또는 GitHub Secrets에 SLACK_BOT_TOKEN 등록")
        return False
    elif webhook_url and not firebase_bucket:
        print("⚠️  슬랙 전송 가능: 텍스트 메시지만 전송됩니다")
        print()
        print("💡 이미지를 전송하려면:")
        print("   1. Firebase Storage 설정")
        print("   2. GitHub Secrets에 Firebase 관련 Secrets 등록")
        return True
    else:
        print("✅ 슬랙 전송 설정 완료!")
        return True

if __name__ == "__main__":
    diagnose_slack_issue()



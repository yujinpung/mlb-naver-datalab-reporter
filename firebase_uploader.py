# -*- coding: utf-8 -*-
"""
Firebase Storage에 스크린샷 업로드
"""
import os
import sys
from pathlib import Path
from firebase_admin import credentials, initialize_app, storage
import firebase_admin

# Firebase Admin SDK 초기화
def init_firebase():
    """Firebase Admin SDK 초기화"""
    # 환경변수에서 Firebase 인증 정보 가져오기
    firebase_creds_json = os.getenv("FIREBASE_CREDENTIALS_JSON")
    
    if not firebase_creds_json:
        # 로컬 파일에서 읽기 (개발용)
        cred_path = os.getenv("FIREBASE_CREDENTIALS_PATH", "firebase-credentials.json")
        if os.path.exists(cred_path):
            cred = credentials.Certificate(cred_path)
        else:
            raise ValueError("Firebase 인증 정보가 없습니다. FIREBASE_CREDENTIALS_JSON 또는 firebase-credentials.json 파일이 필요합니다.")
    else:
        # JSON 문자열에서 직접 로드
        import json
        cred_dict = json.loads(firebase_creds_json)
        cred = credentials.Certificate(cred_dict)
    
    # Firebase 앱 초기화 (이미 초기화되어 있으면 스킵)
    try:
        firebase_admin.get_app()
    except ValueError:
        initialize_app(cred, {
            'storageBucket': os.getenv("FIREBASE_STORAGE_BUCKET")
        })

def upload_screenshot(file_path, keyword_name):
    """
    스크린샷을 Firebase Storage에 업로드
    
    Args:
        file_path: 업로드할 파일 경로
        keyword_name: 키워드 이름 (파일명에 사용)
    
    Returns:
        업로드된 파일의 공개 URL
    """
    init_firebase()
    
    # 파일명 생성
    filename = os.path.basename(file_path)
    storage_path = f"screenshots/{filename}"
    
    # Firebase Storage 버킷 참조
    bucket = storage.bucket()
    blob = bucket.blob(storage_path)
    
    # 파일 업로드
    blob.upload_from_filename(file_path)
    
    # 공개 URL 생성 (읽기 권한 설정)
    blob.make_public()
    
    # 공개 URL 반환
    public_url = blob.public_url
    print(f"✅ Firebase Storage 업로드 완료: {keyword_name}")
    print(f"   URL: {public_url}")
    
    return public_url

def upload_all_screenshots(screenshots_dir="screenshots"):
    """
    screenshots 폴더의 모든 PNG 파일을 Firebase Storage에 업로드
    
    Args:
        screenshots_dir: 스크린샷 폴더 경로
    
    Returns:
        업로드된 파일들의 URL 딕셔너리 {키워드명: URL}
    """
    screenshots_path = Path(screenshots_dir)
    if not screenshots_path.exists():
        print(f"❌ 스크린샷 폴더를 찾을 수 없습니다: {screenshots_dir}")
        return {}
    
    uploaded_urls = {}
    png_files = list(screenshots_path.glob("*.png"))
    
    if not png_files:
        print("❌ 업로드할 스크린샷이 없습니다.")
        return uploaded_urls
    
    print(f"\n📤 Firebase Storage 업로드 시작 ({len(png_files)}개 파일)...")
    
    for png_file in png_files:
        # 파일명에서 키워드 추출
        filename = png_file.stem
        # NaverDatalab_2025-11-14_MLB.png -> MLB
        parts = filename.split("_")
        if len(parts) >= 3:
            keyword = parts[-1]  # 마지막 부분이 키워드
        else:
            keyword = filename
        
        try:
            url = upload_screenshot(str(png_file), keyword)
            uploaded_urls[keyword] = url
        except Exception as e:
            print(f"❌ 업로드 실패 ({keyword}): {str(e)}")
    
    print(f"\n✅ 총 {len(uploaded_urls)}개 파일 업로드 완료")
    return uploaded_urls

if __name__ == "__main__":
    # 테스트 실행
    if len(sys.argv) > 1:
        screenshots_dir = sys.argv[1]
    else:
        screenshots_dir = "screenshots"
    
    upload_all_screenshots(screenshots_dir)


from youtube_transcript_api import YouTubeTranscriptApi
import re
from day4_summarizer import summarize_text

def get_video_id(url):
    """유튜브 URL에서 video ID만 뽑아내는 함수"""
    match = re.search(r"(?:v=|youtu\.be/)([a-zA-Z0-9_-]{11})", url)
    if match:
        return match.group(1)
    return None

def get_transcript_text(video_id):
    """자막을 가져와서 하나의 문자열로 합치는 함수"""
    ytt_api = YouTubeTranscriptApi()
    fetched_transcript = ytt_api.fetch(video_id, languages=['ko', 'en'])
    full_text = " ".join([snippet.text for snippet in fetched_transcript])
    return full_text

def summarize_youtube(url):
    video_id = get_video_id(url)
    if not video_id:
        print("잘못된 URL입니다.")
        return

    try:
        text = get_transcript_text(video_id)
    except Exception as e:
        print(f"자막을 가져올 수 없습니다: {e}")
        return

    summary = summarize_text(text)
    print(summary)

if __name__ == "__main__":
    url = input("유튜브 URL 입력: ")
    summarize_youtube(url)
from day5_youtube_summarizer import get_video_id, get_transcript_text
from day5_whisper_summarizer import download_audio, transcribe_audio
from day4_summarizer import summarize_text

def summarize_youtube_smart(url):
    video_id = get_video_id(url)
    if not video_id:
        print("잘못된 URL입니다.")
        return

    try:
        print("자막 시도 중...")
        text = get_transcript_text(video_id)
        print("자막으로 처리함")
    except Exception:
        print("자막 없음 - Whisper로 전환")
        audio_path = download_audio(url)
        text = transcribe_audio(audio_path)

    print("요약 중...")
    summary = summarize_text(text)
    print(summary)

if __name__ == "__main__":
    url = input("유튜브 URL 입력: ")
    summarize_youtube_smart(url)
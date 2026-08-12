import yt_dlp
import whisper
from day4_summarizer import summarize_text

def download_audio(url, output_path="audio"):
    """유튜브 URL에서 오디오만 다운로드하는 함수"""
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_path + '.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    return output_path + ".mp3"

def transcribe_audio(audio_path):
    """오디오 파일을 텍스트로 변환하는 함수"""
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    return result["text"]

def summarize_youtube_whisper(url):
    print("오디오 다운로드 중...")
    audio_path = download_audio(url)

    print("음성 인식 중... (시간 좀 걸림)")
    text = transcribe_audio(audio_path)

    print("요약 중...")
    summary = summarize_text(text)  # 빈칸: 기존 요약 함수 호출

    print(summary)

if __name__ == "__main__":
    url = input("유튜브 URL 입력: ")
    summarize_youtube_whisper(url)
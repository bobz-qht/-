import { NextResponse } from "next/server";
import { YoutubeTranscript } from "youtube-transcript";
import { summarizeText } from "@/lib/anthropic";

export async function POST(request: Request) {
  const body = await request.json();
  const { url } = body;

  if (!url) {
    return NextResponse.json({ error: "URL이 없습니다" }, { status: 400 });
  }

  try {
    const transcript = await YoutubeTranscript.fetchTranscript(url);
    const text = transcript.map((t) => t.text).join(" ");

    if (!text) {
      return NextResponse.json(
        { error: "자막을 찾을 수 없습니다. 자막이 없는 영상은 지원하지 않습니다." },
        { status: 400 }
      );
    }

    const summary = await summarizeText(text);
    return NextResponse.json({ summary });
  } catch (e) {
    return NextResponse.json(
      { error: `자막을 가져오지 못했습니다: ${e}` },
      { status: 500 }
    );
  }
}

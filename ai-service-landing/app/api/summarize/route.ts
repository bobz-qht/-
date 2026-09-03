import { NextResponse } from "next/server";
import { summarizeText } from "@/lib/anthropic";

export async function POST(request: Request) {
  const body = await request.json();
  const text = body.text;

  if (!text) {
    return NextResponse.json({ error: "text가 없습니다" }, { status: 400 });
  }

  try {
    const summary = await summarizeText(text);
    return NextResponse.json({ summary });
  } catch (e) {
    return NextResponse.json({ error: `요약 중 오류: ${e}` }, { status: 500 });
  }
}

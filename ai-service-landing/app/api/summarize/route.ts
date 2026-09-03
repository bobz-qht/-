import { NextResponse } from "next/server";
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env.ANTHROPIC_API_KEY,
});

export async function POST(request: Request) {
  const body = await request.json();
  const text = body.text;

  if (!text) {
    return NextResponse.json({ error: "text가 없습니다" }, { status: 400 });
  }

  try {
    const response = await client.messages.create({
      model: "claude-sonnet-4-6",
      max_tokens: 1000,
      messages: [
        { role: "user", content: `다음 글을 3줄로 요약해줘:\n\n${text}` },
      ],
    });

    const block = response.content[0];
    const summary = block.type === "text" ? block.text : "";

    return NextResponse.json({ summary });
  } catch (e) {
    return NextResponse.json({ error: `요약 중 오류: ${e}` }, { status: 500 });
  }
}
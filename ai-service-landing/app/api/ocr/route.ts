import { NextResponse } from "next/server";
import { client } from "@/lib/anthropic";

export async function POST(request: Request) {
  const body = await request.json();
  const { image, mediaType } = body;

  if (!image) {
    return NextResponse.json({ error: "이미지가 없습니다" }, { status: 400 });
  }

  try {
    const response = await client.messages.create({
      model: "claude-sonnet-4-6",
      max_tokens: 1000,
      messages: [
        {
          role: "user",
          content: [
            {
              type: "image",
              source: { type: "base64", media_type: mediaType, data: image },
            },
            {
              type: "text",
              text: "이 이미지에 있는 텍스트를 전부 그대로 추출해줘. 텍스트만 출력하고 다른 설명은 붙이지 마.",
            },
          ],
        },
      ],
    });

    const block = response.content[0];
    const text = block.type === "text" ? block.text : "";

    return NextResponse.json({ text });
  } catch (e) {
    return NextResponse.json({ error: `OCR 중 오류: ${e}` }, { status: 500 });
  }
}

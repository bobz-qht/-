import Anthropic from "@anthropic-ai/sdk";

export const client = new Anthropic({
  apiKey: process.env.ANTHROPIC_API_KEY,
});

export async function summarizeText(text: string) {
  const response = await client.messages.create({
    model: "claude-sonnet-4-6",
    max_tokens: 1000,
    messages: [
      { role: "user", content: `다음 글을 3줄로 요약해줘:\n\n${text}` },
    ],
  });

  const block = response.content[0];
  return block.type === "text" ? block.text : "";
}

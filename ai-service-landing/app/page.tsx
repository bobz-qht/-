import Link from "next/link";

export default function Home() {
  const tools = [
    { name: "텍스트 요약기", desc: "긴 글을 3줄로 요약해주는 도구", href: "/summarize" },
    { name: "OCR 추출기", desc: "이미지 속 텍스트를 뽑아내는 도구", href: "/ocr" },
    { name: "유튜브 요약기", desc: "유튜브 자막을 요약 메모로 바꿔주는 도구", href: "/youtube" },
  ];

  return (
    <main className="container">
      <section className="hero">
        <h1>내가 만든 AI 도구들</h1>
        <p>Claude Code로 하나씩 직접 만든 자동화 도구 모음입니다.</p>
        <button className="cta-button">더 알아보기</button>
      </section>

      <section className="tools">
        {tools.map((tool) => (
          <Link href={tool.href} className="tool-card" key={tool.name}>
            <h2>{tool.name}</h2>
            <p>{tool.desc}</p>
          </Link>
        ))}
      </section>
    </main>
  );
}

"use client";

import { useState } from "react";

export default function SummarizePage() {
  const [text, setText] = useState("");
  const [summary, setSummary] = useState("");
  const [loading, setLoading] = useState(false);
  const [errorMsg, setErrorMsg] = useState("");

  async function handleSummarize() {
    setErrorMsg("");
    setSummary("");
    setLoading(true);

    try {
      const response = await fetch("/api/summarize", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text }),
      });

      const data = await response.json();

      if (!response.ok) {
        setErrorMsg(data.error || "요약 중 오류가 발생했습니다.");
        return;
      }

      setSummary(data.summary);
    } catch (err) {
      setErrorMsg("서버에 연결할 수 없습니다.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="container">
      <section className="hero">
        <h1>텍스트 요약기</h1>
        <p>긴 글을 붙여넣으면 3줄로 요약해줍니다.</p>
      </section>

      <textarea
        className="summarize-textarea"
        placeholder="여기에 요약할 텍스트를 붙여넣으세요"
        value={text}
        onChange={(e) => setText(e.target.value)}
        rows={10}
      />

      <button
        className="cta-button"
        onClick={handleSummarize}
        disabled={loading || !text}
      >
        {loading ? "요약 중..." : "요약하기"}
      </button>

      {errorMsg && <p className="error-text">{errorMsg}</p>}

      {summary && (
        <section className="summary-result">
          <h2>요약 결과</h2>
          <p>{summary}</p>
        </section>
      )}
    </main>
  );
}
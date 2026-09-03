"use client";

import { useState } from "react";
import { saveResult } from "@/lib/supabase";

export default function YoutubePage() {
  const [url, setUrl] = useState("");
  const [summary, setSummary] = useState("");
  const [loading, setLoading] = useState(false);
  const [errorMsg, setErrorMsg] = useState("");

  async function handleSummarize() {
    setErrorMsg("");
    setSummary("");
    setLoading(true);

    try {
      const response = await fetch("/api/youtube", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ url }),
      });

      const data = await response.json();

      if (!response.ok) {
        setErrorMsg(data.error || "요약 중 오류가 발생했습니다.");
        return;
      }

      setSummary(data.summary);
      saveResult("유튜브 요약기", data.summary);
    } catch (err) {
      setErrorMsg("서버에 연결할 수 없습니다.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="container">
      <section className="hero">
        <h1>유튜브 요약기</h1>
        <p>자막이 있는 유튜브 영상 링크를 넣으면 요약해줍니다.</p>
      </section>

      <input
        type="text"
        placeholder="https://www.youtube.com/watch?v=..."
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        className="summarize-textarea"
      />

      <button
        className="cta-button"
        onClick={handleSummarize}
        disabled={loading || !url}
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

"use client";

import { useState } from "react";
import { saveResult } from "@/lib/supabase";

export default function OcrPage() {
  const [preview, setPreview] = useState("");
  const [extractedText, setExtractedText] = useState("");
  const [loading, setLoading] = useState(false);
  const [errorMsg, setErrorMsg] = useState("");

  function handleFileChange(e: React.ChangeEvent<HTMLInputElement>) {
    const file = e.target.files?.[0];
    if (!file) return;

    setErrorMsg("");
    setExtractedText("");

    const reader = new FileReader();
    reader.onload = async () => {
      const dataUrl = reader.result as string;
      setPreview(dataUrl);

      const [header, base64] = dataUrl.split(",");
      const mediaType = header.match(/data:(.*);base64/)?.[1] || "image/png";

      setLoading(true);
      try {
        const response = await fetch("/api/ocr", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ image: base64, mediaType }),
        });

        const data = await response.json();

        if (!response.ok) {
          setErrorMsg(data.error || "추출 중 오류가 발생했습니다.");
          return;
        }

        setExtractedText(data.text);
        saveResult("OCR 추출기", data.text);
      } catch (err) {
        setErrorMsg("서버에 연결할 수 없습니다.");
      } finally {
        setLoading(false);
      }
    };
    reader.readAsDataURL(file);
  }

  return (
    <main className="container">
      <section className="hero">
        <h1>OCR 추출기</h1>
        <p>이미지를 올리면 안의 텍스트를 뽑아줍니다.</p>
      </section>

      <input type="file" accept="image/*" onChange={handleFileChange} />

      {preview && (
        <img
          src={preview}
          alt="미리보기"
          style={{ maxWidth: "100%", marginTop: 16, borderRadius: 8 }}
        />
      )}

      {loading && <p>추출 중...</p>}
      {errorMsg && <p className="error-text">{errorMsg}</p>}

      {extractedText && (
        <section className="summary-result">
          <h2>추출된 텍스트</h2>
          <p style={{ whiteSpace: "pre-wrap" }}>{extractedText}</p>
        </section>
      )}
    </main>
  );
}

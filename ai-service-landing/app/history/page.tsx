"use client";

import { useEffect, useState } from "react";
import { supabase } from "@/lib/supabase";

type Result = {
  id: string;
  tool: string;
  output: string;
  created_at: string;
};

export default function HistoryPage() {
  const [results, setResults] = useState<Result[]>([]);
  const [loading, setLoading] = useState(true);
  const [errorMsg, setErrorMsg] = useState("");

  useEffect(() => {
    async function load() {
      const { data: sessionData } = await supabase.auth.getSession();

      if (!sessionData.session) {
        setErrorMsg("로그인 후 이용할 수 있습니다.");
        setLoading(false);
        return;
      }

      const { data, error } = await supabase
        .from("results")
        .select("*")
        .order("created_at", { ascending: false });

      if (error) {
        setErrorMsg(error.message);
      } else {
        setResults(data as Result[]);
      }

      setLoading(false);
    }

    load();
  }, []);

  return (
    <main className="container">
      <section className="hero">
        <h1>내 기록</h1>
        <p>지금까지 저장된 도구 사용 결과입니다.</p>
      </section>

      {loading && <p>불러오는 중...</p>}
      {errorMsg && <p className="error-text">{errorMsg}</p>}

      {!loading && !errorMsg && results.length === 0 && (
        <p>아직 저장된 기록이 없습니다.</p>
      )}

      {results.map((r) => (
        <section key={r.id} className="summary-result">
          <span className="badge">{r.tool}</span>
          <p style={{ whiteSpace: "pre-wrap", marginTop: 8 }}>{r.output}</p>
          <p style={{ fontSize: 12, color: "#888", marginTop: 8 }}>
            {new Date(r.created_at).toLocaleString("ko-KR")}
          </p>
        </section>
      ))}
    </main>
  );
}

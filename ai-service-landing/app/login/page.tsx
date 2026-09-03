"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { supabase } from "@/lib/supabase";

export default function LoginPage() {
  const [mode, setMode] = useState<"login" | "signup">("login");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errorMsg, setErrorMsg] = useState("");
  const [infoMsg, setInfoMsg] = useState("");
  const [loading, setLoading] = useState(false);
  const router = useRouter();

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    setErrorMsg("");
    setInfoMsg("");
    setLoading(true);

    if (mode === "login") {
      const { error } = await supabase.auth.signInWithPassword({ email, password });
      setLoading(false);

      if (error) {
        setErrorMsg("이메일 또는 비밀번호가 올바르지 않습니다.");
        return;
      }

      router.push("/");
      router.refresh();
    } else {
      const { data, error } = await supabase.auth.signUp({ email, password });
      setLoading(false);

      if (error) {
        setErrorMsg(error.message);
        return;
      }

      if (data.session) {
        // Confirm email이 꺼져있으면 가입과 동시에 로그인된 상태로 세션이 온다.
        router.push("/");
        router.refresh();
      } else {
        // Confirm email이 켜져있으면 세션 없이 가입만 되고, 메일 확인이 필요하다.
        setInfoMsg("가입 확인 이메일을 보냈습니다. 메일함을 확인해주세요.");
      }
    }
  }

  return (
    <main className="container">
      <section className="hero">
        <h1>{mode === "login" ? "로그인" : "회원가입"}</h1>
      </section>

      <form onSubmit={handleSubmit} className="login-form">
        <input
          type="email"
          placeholder="이메일"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
        <input
          type="password"
          placeholder="비밀번호 (6자 이상)"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
        <button type="submit" className="cta-button" disabled={loading}>
          {loading ? "처리 중..." : mode === "login" ? "로그인" : "회원가입"}
        </button>
        {errorMsg && <p className="error-text">{errorMsg}</p>}
        {infoMsg && <p className="info-text">{infoMsg}</p>}
      </form>

      <button
        type="button"
        className="link-button"
        onClick={() => {
          setMode(mode === "login" ? "signup" : "login");
          setErrorMsg("");
          setInfoMsg("");
        }}
      >
        {mode === "login" ? "계정이 없으신가요? 회원가입" : "이미 계정이 있으신가요? 로그인"}
      </button>
    </main>
  );
}

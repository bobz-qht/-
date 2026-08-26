"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { supabase } from "@/lib/supabase";

export default function LoginPage() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errorMsg, setErrorMsg] = useState("");
  const [loading, setLoading] = useState(false);
  const router = useRouter();

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    setErrorMsg("");
    setLoading(true);

    const { error } = await supabase.auth.signInWithPassword({
      email,
      password,
    });

    setLoading(false);

    if (error) {
      setErrorMsg("이메일 또는 비밀번호가 올바르지 않습니다.");
      return;
    }

    router.push("/");
  }

  return (
    <main className="container">
      <section className="hero">
        <h1>로그인</h1>
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
          placeholder="비밀번호"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
        <button type="submit" className="cta-button" disabled={loading}>
          {loading ? "로그인 중..." : "로그인"}
        </button>
        {errorMsg && <p className="error-text">{errorMsg}</p>}
      </form>
    </main>
  );
}
"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { supabase } from "@/lib/supabase";
import type { Session } from "@supabase/supabase-js";

export default function AuthNav() {
  const [session, setSession] = useState<Session | null>(null);
  const router = useRouter();

  useEffect(() => {
    supabase.auth.getSession().then(({ data }) => {
      setSession(data.session);
    });

    const { data: listener } = supabase.auth.onAuthStateChange((_event, newSession) => {
      setSession(newSession);
    });

    return () => {
      listener.subscription.unsubscribe();
    };
  }, []);

  async function handleLogout() {
    await supabase.auth.signOut();
    router.push("/");
    router.refresh();
  }

  if (session) {
    return (
      <div className="site-nav-right">
        <span className="site-nav-email">{session.user.email}</span>
        <button onClick={handleLogout} className="site-nav-link site-nav-button">
          로그아웃
        </button>
      </div>
    );
  }

  return (
    <Link href="/login" className="site-nav-link">로그인</Link>
  );
}

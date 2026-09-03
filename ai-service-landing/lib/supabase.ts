import { createClient } from "@supabase/supabase-js";

const supabaseUrl = process.env.NEXT_PUBLIC_SUPABASE_URL!;
const supabaseAnonKey = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!;

export const supabase = createClient(supabaseUrl, supabaseAnonKey);

export async function saveResult(tool: string, output: string) {
  const { data } = await supabase.auth.getSession();
  if (!data.session) return; // 로그인 안 했으면 저장 안 함

  await supabase.from("results").insert({ tool, output });
}
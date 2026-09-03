import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import Link from "next/link";
import AuthNav from "./components/AuthNav";
import "./globals.css";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "AI 도구 모음 | 내가 만든 자동화 도구들",
  description: "Claude Code로 직접 만든 텍스트 요약기, OCR 추출기, 유튜브 요약기 모음",
};

export default function RootLayout({ children }: LayoutProps<"/">) {
  return (
    <html lang="ko" className={`${geistSans.variable} ${geistMono.variable}`}>
      <body>
        <nav className="site-nav">
          <Link href="/" className="site-nav-logo">AI 도구 모음</Link>
          <AuthNav />
        </nav>
        {children}
      </body>
    </html>
  );
}
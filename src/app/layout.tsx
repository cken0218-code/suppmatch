import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";

const inter = Inter({
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "SuppMatch - 症狀揀選 → 營養補充品推薦",
  description: "選擇您的症狀，獲取iHerb營養補充品推薦",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="zh-HK">
      <body className={inter.className}>
        {children}
      </body>
    </html>
  );
}

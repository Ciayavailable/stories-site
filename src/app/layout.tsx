import type { Metadata } from "next";
import { Manrope } from "next/font/google";
import "./globals.css";

const manrope = Manrope({
  variable: "--font-sans-inter",
  subsets: ["latin", "cyrillic"],
  weight: ["400", "500", "600", "700", "800"],
});

export const metadata: Metadata = {
  title: "Stories — кафе в Сочи | ул. Виноградная, 2/3Б",
  description:
    "Кафе Stories в центре Сочи: завтраки, домашние десерты, авторские рафы и горячая кухня. Открыто ежедневно до 21:00. Рейтинг 5.0 ★",
  keywords: [
    "Stories",
    "кафе Сочи",
    "кофейня Сочи",
    "завтраки Сочи",
    "раф Сочи",
    "Виноградная 2/3Б",
  ],
  openGraph: {
    title: "Stories — кафе в Сочи",
    description:
      "Кофейня с характером в центре Сочи. Завтраки, домашние десерты, авторский кофе. Ежедневно до 21:00.",
    type: "website",
    locale: "ru_RU",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="ru" suppressHydrationWarning>
      <body
        className={`${manrope.variable} antialiased bg-black text-white`}
      >
        {children}
      </body>
    </html>
  );
}

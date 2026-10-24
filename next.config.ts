import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  // Обычный запуск (npm run dev / npm start) — standalone;
  // статическая сборка для хостинга: NEXT_OUTPUT_EXPORT=1 npm run build
  output: process.env.NEXT_OUTPUT_EXPORT === "1" ? "export" : "standalone",
  typescript: {
    ignoreBuildErrors: true,
  },
  reactStrictMode: false,
};

export default nextConfig;

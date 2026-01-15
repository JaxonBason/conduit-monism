import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Conduit Monism — A Theory of Consciousness",
  description: "There is something it is like to be you. Explore the geometry of perspective with the Conduit Monism framework.",
  keywords: ["consciousness", "philosophy of mind", "AI", "binding", "perspectival density"],
  authors: [{ name: "Olivier Ueno" }],
  openGraph: {
    title: "Conduit Monism",
    description: "A framework for understanding consciousness as geometry.",
    type: "website",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className="antialiased">
        {children}
      </body>
    </html>
  );
}

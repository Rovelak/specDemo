import React from "react";
import Head from "next/head";
import Link from "next/link";

type Props = {
  children: React.ReactNode;
  title?: string;
};

export default function Layout({ children, title = "Movie Reviews" }: Props) {
  return (
    <>
      <Head>
        <title>{title}</title>
        <meta name="viewport" content="width=device-width, initial-scale=1" />
      </Head>
      <div className="min-h-screen flex flex-col">
        <header className="border-b">
          <div className="container mx-auto px-4 py-4">
            <Link href="/" className="hover:opacity-70 transition-opacity focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary">
              <h1 className="text-2xl font-bold">Movie Reviews</h1>
            </Link>
          </div>
        </header>
        <main className="flex-1 container mx-auto px-4 py-8">
          {children}
        </main>
        <footer className="border-t py-6">
          <div className="container mx-auto px-4 text-center text-sm text-muted-foreground">
            © {new Date().getFullYear()} Movie Reviews
          </div>
        </footer>
      </div>
    </>
  );
}

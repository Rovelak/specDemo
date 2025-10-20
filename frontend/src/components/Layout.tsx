import React from "react";
import Head from "next/head";

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
      <div className="site-container">
        <header className="site-header">
          <h1 className="site-title">Movie Reviews</h1>
        </header>
        <main className="site-main">{children}</main>
        <footer className="site-footer">
          © {new Date().getFullYear()} Movie Reviews
        </footer>
      </div>
    </>
  );
}

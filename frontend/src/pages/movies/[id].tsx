import React from "react";
import MovieDetail from "../../components/MovieDetail.tsx";
import { loadMovies } from "../../lib/fixtures.ts";
import type { Movie } from "../../types/models.ts";
import Layout from "../../components/Layout.tsx";

type Props = {
  movie?: Movie;
};

export default function MoviePage({ movie }: Props) {
  if (!movie) {
    return (
      <Layout>
        <p>Movie not found.</p>
      </Layout>
    );
  }

  return (
    <Layout title={movie.title}>
      <MovieDetail movie={movie} />
    </Layout>
  );
}

export async function getStaticPaths() {
  const movies = loadMovies();
  const paths = movies.map((m: Movie) => ({ params: { id: m.id } }));

  return { paths, fallback: false };
}

export async function getStaticProps(context: { params?: { id?: string } }) {
  const id = context.params?.id || "";
  const movies = loadMovies();
  const movie = movies.find((m: Movie) => m.id === id) || null;

  return { props: { movie } };
}

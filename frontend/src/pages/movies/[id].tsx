import React from "react";
import { GetStaticPaths, GetStaticProps } from "next";
import MovieDetail from "../../components/MovieDetail";
import { loadMovies } from "../../lib/fixtures";
import type { Movie } from "../../types/models";
import Layout from "../../components/Layout";

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

export const getStaticPaths: GetStaticPaths = async () => {
  const movies = loadMovies();
  const paths = movies.map((m) => ({ params: { id: m.id } }));

  return { paths, fallback: false };
};

export const getStaticProps: GetStaticProps = async (context) => {
  const { id } = context.params as { id: string };
  const movies = loadMovies();
  const movie = movies.find((m) => m.id === id) || null;

  return { props: { movie } };
};

import React, { useState, useMemo } from "react";
import Layout from "../components/Layout";
import MovieCard from "../components/MovieCard";
import EmptyState from "../components/EmptyState";
import SearchBar from "../components/SearchBar";
import { loadMovies } from "../lib/fixtures";

export default function Home() {
  const allMovies = loadMovies();
  const [query, setQuery] = useState("");
  const movies = useMemo(() => {
    if (!query) return allMovies;
    const q = query.toLowerCase();
    return allMovies.filter(
      (m) =>
        m.title.toLowerCase().includes(q) || String(m.releaseYear).includes(q)
    );
  }, [query, allMovies]);

  if (!movies || movies.length === 0) {
    return (
      <Layout>
        <EmptyState message="No movies available." />
      </Layout>
    );
  }

  return (
    <Layout>
      <SearchBar onSearch={setQuery} />
      {movies.length === 0 ? (
        <EmptyState message={`No results for '${query}'.`} />
      ) : (
        <section className="movie-list">
          {movies.map((m) => (
            <MovieCard key={m.id} movie={m} />
          ))}
        </section>
      )}
    </Layout>
  );
}

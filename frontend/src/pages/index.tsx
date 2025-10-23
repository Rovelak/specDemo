import React, { useState, useMemo } from "react";
import Layout from "../components/Layout.tsx";
import MovieCard from "../components/MovieCard.tsx";
import EmptyState from "../components/EmptyState.tsx";
import SearchBar from "../components/SearchBar.tsx";
import { Button } from "../components/ui/index";
import { loadMovies } from "../lib/fixtures.ts";

export default function Home() {
  const allMovies = loadMovies();
  const [query, setQuery] = useState("");
  const movies = useMemo((): import("../types/models.js").Movie[] => {
    if (!query) return allMovies;
    const q = query.toLowerCase();
    return allMovies.filter(
      (m: import("../types/models.js").Movie) =>
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
      <div style={{ marginTop: "0.5rem" }}>
        <Button onClick={() => alert("Example button clicked")}>
          Add movie
        </Button>
      </div>
      {movies.length === 0 ? (
        <EmptyState message={`No results for '${query}'.`} />
      ) : (
        <section className="movie-list">
          {movies.map((m: import("../types/models.js").Movie) => (
            <MovieCard key={m.id} movie={m} />
          ))}
        </section>
      )}
    </Layout>
  );
}

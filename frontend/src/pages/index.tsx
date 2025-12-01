import React, { useState, useMemo } from "react";
import Layout from "../components/Layout";
import MovieCard from "../components/MovieCard";
import EmptyState from "../components/EmptyState";
import SearchBar from "../components/SearchBar";
import { Button } from "@/components/ui/button";
import { Plus } from "lucide-react";
import { loadMovies } from "../lib/fixtures";
import type { Movie } from "../types/models";

export default function Home() {
  const allMovies = loadMovies();
  const [query, setQuery] = useState("");

  const movies = useMemo((): Movie[] => {
    if (!query) return allMovies;
    const q = query.toLowerCase();
    return allMovies.filter(
      (m: Movie) =>
        m.title.toLowerCase().includes(q) || String(m.releaseYear).includes(q)
    );
  }, [query, allMovies]);

  if (!allMovies || allMovies.length === 0) {
    return (
      <Layout>
        <EmptyState message="No movies available." />
      </Layout>
    );
  }

  return (
    <Layout>
      <div className="space-y-6">
        <div className="flex flex-col sm:flex-row gap-4 items-start sm:items-center justify-between">
          <SearchBar onSearch={setQuery} />
          <Button onClick={() => alert("Example button clicked")}>
            <Plus className="h-4 w-4 mr-2" aria-hidden="true" />
            Add Movie
          </Button>
        </div>

        {movies.length === 0 ? (
          <EmptyState message={`No results for '${query}'.`} />
        ) : (
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
            {movies.map((m: Movie) => (
              <MovieCard key={m.id} movie={m} />
            ))}
          </div>
        )}
      </div>
    </Layout>
  );
}

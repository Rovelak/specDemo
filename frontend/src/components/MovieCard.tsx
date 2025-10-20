import React from "react";
import Link from "next/link";
import type { Movie } from "../types/models";

type Props = {
  movie: Movie;
};

export default function MovieCard({ movie }: Props) {
  return (
    <article className="movie-card">
      <Link
        href={`/movies/${movie.id}`}
        aria-label={`View details for ${movie.title}`}
      >
        <img
          src={movie.posterUrl ?? "/posters/placeholder.png"}
          alt={movie.title + " poster"}
          width={150}
          height={225}
        />
        <div className="movie-meta">
          <h2>{movie.title}</h2>
          <p className="movie-year">{movie.releaseYear}</p>
        </div>
      </Link>
    </article>
  );
}

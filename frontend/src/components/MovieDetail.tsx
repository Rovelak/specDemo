import React from "react";
import type { Movie } from "../types/models";
import ReviewList from "./ReviewList";

type Props = {
  movie: Movie;
};

export default function MovieDetail({ movie }: Props) {
  return (
    <article className="movie-detail">
      <div className="movie-detail-grid">
        <img
          src={movie.posterUrl ?? "/posters/placeholder.png"}
          alt={`${movie.title} poster`}
          width={300}
          height={450}
        />
        <div className="movie-detail-meta">
          <h1>{movie.title}</h1>
          <p className="movie-year">{movie.releaseYear}</p>
          {movie.synopsis && (
            <section>
              <h2>Synopsis</h2>
              <p>{movie.synopsis}</p>
            </section>
          )}

          {movie.cast && movie.cast.length > 0 && (
            <section>
              <h3>Cast</h3>
              <ul>
                {movie.cast.map((c) => (
                  <li key={c}>{c}</li>
                ))}
              </ul>
            </section>
          )}
        </div>
      </div>

      <section className="movie-reviews">
        <h2>Reviews</h2>
        <ReviewList reviews={movie.reviews} />
      </section>
    </article>
  );
}

import React from "react";
import { Badge } from "@/components/ui/badge";
import { Separator } from "@/components/ui/separator";
import type { Movie } from "../types/models";
import ReviewList from "./ReviewList";

type Props = {
  movie: Movie;
};

export default function MovieDetail({ movie }: Props) {
  return (
    <div className="space-y-8">
      <div className="grid md:grid-cols-[300px_1fr] gap-8">
        <div className="w-full aspect-[2/3] relative overflow-hidden rounded-lg">
          <img
            src={movie.posterUrl ?? "/posters/placeholder.png"}
            alt={`${movie.title} poster`}
            className="object-cover w-full h-full"
            width={300}
            height={450}
          />
        </div>

        <div className="space-y-6">
          <div>
            <h1 className="text-4xl font-bold mb-2">{movie.title}</h1>
            <Badge variant="secondary" className="text-base" aria-label={`Released in ${movie.releaseYear}`}>
              {movie.releaseYear}
            </Badge>
          </div>

          {movie.synopsis && (
            <>
              <Separator />
              <div>
                <h2 className="text-xl font-semibold mb-3">Synopsis</h2>
                <p className="text-muted-foreground leading-relaxed">
                  {movie.synopsis}
                </p>
              </div>
            </>
          )}

          {movie.cast && movie.cast.length > 0 && (
            <>
              <Separator />
              <div>
                <h3 className="text-lg font-semibold mb-3">Cast</h3>
                <div className="flex flex-wrap gap-2">
                  {movie.cast.map((c) => (
                    <Badge key={c} variant="outline">
                      {c}
                    </Badge>
                  ))}
                </div>
              </div>
            </>
          )}
        </div>
      </div>

      <Separator className="my-8" />

      <div>
        <h2 className="text-2xl font-semibold mb-4">Reviews</h2>
        <ReviewList reviews={movie.reviews} />
      </div>
    </div>
  );
}

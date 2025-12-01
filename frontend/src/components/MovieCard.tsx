import React from "react";
import Link from "next/link";
import { Card, CardContent } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import type { Movie } from "../types/models";

type Props = {
  movie: Movie;
};

export default function MovieCard({ movie }: Props) {
  return (
    <Link
      href={`/movies/${movie.id}`}
      aria-label={`View details for ${movie.title}`}
      className="group block"
    >
      <Card className="overflow-hidden transition-all hover:shadow-lg hover:scale-[1.02]">
        <div className="relative aspect-[2/3] overflow-hidden">
          <img
            src={movie.posterUrl ?? "/posters/placeholder.png"}
            alt={`${movie.title} poster`}
            className="object-cover w-full h-full group-hover:scale-105 transition-transform duration-300"
            width={150}
            height={225}
          />
        </div>
        <CardContent className="p-4">
          <h2 className="font-semibold text-lg line-clamp-2 mb-2">
            {movie.title}
          </h2>
          <Badge variant="secondary" aria-label={`Released in ${movie.releaseYear}`}>{movie.releaseYear}</Badge>
        </CardContent>
      </Card>
    </Link>
  );
}

export type Review = {
  id: string;
  author: string;
  rating: number;
  text?: string;
};

export type Movie = {
  id: string;
  title: string;
  releaseYear: number;
  posterUrl?: string;
  synopsis?: string;
  cast?: string[];
  reviews?: Review[];
};

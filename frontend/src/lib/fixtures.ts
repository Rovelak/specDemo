import moviesData from "../../fixtures/movies.json";
import { Movie, Review } from "../types/models";

export const movies: Movie[] = moviesData as Movie[];

// Validation logic to ensure fixture integrity
export interface FixtureValidationIssue {
  movieId: string | number;
  path: string;
  message: string;
}

export interface FixtureValidationResult {
  valid: boolean;
  issues: FixtureValidationIssue[];
}

const isNonEmptyString = (v: unknown): v is string =>
  typeof v === "string" && v.trim().length > 0;
const isYear = (v: unknown): v is number =>
  typeof v === "number" && v > 1900 && v < new Date().getFullYear() + 2;

export function validateMoviesFixture(
  data: Movie[] = movies
): FixtureValidationResult {
  const issues: FixtureValidationIssue[] = [];
  data.forEach((m) => {
    if (!isNonEmptyString(m.id)) {
      issues.push({
        movieId: m.id ?? "<missing>",
        path: "id",
        message: "id must be non-empty string",
      });
    }
    if (!isNonEmptyString(m.title)) {
      issues.push({
        movieId: m.id ?? "<missing>",
        path: "title",
        message: "title must be non-empty string",
      });
    }
    if (!isYear(m.releaseYear)) {
      issues.push({
        movieId: m.id ?? "<missing>",
        path: "releaseYear",
        message: "releaseYear must be a plausible number",
      });
    }
    if (m.reviews) {
      m.reviews.forEach((r: Review, idx: number) => {
        if (!isNonEmptyString(r.author)) {
          issues.push({
            movieId: m.id,
            path: `reviews[${idx}].author`,
            message: "author must be non-empty string",
          });
        }
        if (!isNonEmptyString(r.text)) {
          issues.push({
            movieId: m.id,
            path: `reviews[${idx}].text`,
            message: "text must be non-empty string",
          });
        }
        if (typeof r.rating !== "number" || r.rating < 0 || r.rating > 10) {
          issues.push({
            movieId: m.id,
            path: `reviews[${idx}].rating`,
            message: "rating must be 0-10",
          });
        }
      });
    }
  });
  return { valid: issues.length === 0, issues };
}

// Run validation immediately (can be toggled off in production)
export const moviesFixtureValidation = validateMoviesFixture();

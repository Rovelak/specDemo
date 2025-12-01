# API Documentation

This document describes the data models, validation logic, and data access patterns used in the Movie Review Website.

## Table of Contents

- [Data Models](#data-models)
- [Fixture System](#fixture-system)
- [Data Validation](#data-validation)
- [Data Access](#data-access)
- [Error Handling](#error-handling)

## Data Models

### Movie Type

The `Movie` type represents a movie entity with its associated metadata and reviews.

**Location**: [frontend/src/types/models.ts](../frontend/src/types/models.ts)

```typescript
type Movie = {
  id: string;              // Unique identifier (required)
  title: string;           // Movie title (required)
  releaseYear: number;     // Year of release (required)
  posterUrl?: string;      // Poster image URL (optional)
  synopsis?: string;       // Plot summary (optional)
  cast?: string[];        // Array of actor names (optional)
  reviews?: Review[];     // Array of reviews (optional)
}
```

#### Field Specifications

| Field | Type | Required | Validation | Description |
|-------|------|----------|------------|-------------|
| `id` | `string` | Yes | Non-empty string | Unique identifier for the movie |
| `title` | `string` | Yes | Non-empty string | Full movie title |
| `releaseYear` | `number` | Yes | 1900 - (current year + 2) | Year the movie was released |
| `posterUrl` | `string` | No | Valid URL format | URL to movie poster image |
| `synopsis` | `string` | No | - | Brief plot summary |
| `cast` | `string[]` | No | Array of non-empty strings | List of actor names |
| `reviews` | `Review[]` | No | Valid Review objects | Array of user reviews |

#### Example

```json
{
  "id": "inception",
  "title": "Inception",
  "releaseYear": 2010,
  "posterUrl": "https://example.com/inception.jpg",
  "synopsis": "A thief who steals corporate secrets through dream-sharing technology...",
  "cast": [
    "Leonardo DiCaprio",
    "Joseph Gordon-Levitt",
    "Elliot Page"
  ],
  "reviews": [
    {
      "id": "review-1",
      "author": "John Doe",
      "rating": 9,
      "text": "A mind-bending masterpiece!"
    }
  ]
}
```

### Review Type

The `Review` type represents a user review for a movie.

**Location**: [frontend/src/types/models.ts](../frontend/src/types/models.ts)

```typescript
type Review = {
  id: string;          // Unique identifier (required)
  author: string;      // Review author name (required)
  rating: number;      // Rating from 0-10 (required)
  text?: string;       // Review text (optional)
}
```

#### Field Specifications

| Field | Type | Required | Validation | Description |
|-------|------|----------|------------|-------------|
| `id` | `string` | Yes | Non-empty string | Unique identifier for the review |
| `author` | `string` | Yes | Non-empty string | Name of the review author |
| `rating` | `number` | Yes | 0-10 (inclusive) | Numeric rating score |
| `text` | `string` | No | Non-empty string | Review content/commentary |

#### Example

```json
{
  "id": "review-inception-1",
  "author": "Jane Smith",
  "rating": 9.5,
  "text": "Christopher Nolan delivers a visually stunning and intellectually challenging film."
}
```

## Fixture System

The application uses a **fixture-based data architecture** where all movie data is stored in a static JSON file.

### Fixture File

**Location**: [frontend/fixtures/movies.json](../frontend/fixtures/movies.json)

**Format**: JSON array of `Movie` objects

```json
[
  {
    "id": "inception",
    "title": "Inception",
    "releaseYear": 2010,
    "posterUrl": "https://example.com/inception.jpg",
    "synopsis": "...",
    "cast": ["..."],
    "reviews": [...]
  },
  {
    "id": "the-matrix",
    "title": "The Matrix",
    "releaseYear": 1999,
    "posterUrl": "https://example.com/matrix.jpg",
    "synopsis": "...",
    "cast": ["..."],
    "reviews": [...]
  }
]
```

### Fixture Loader

**Location**: [frontend/src/lib/fixtures.ts](../frontend/src/lib/fixtures.ts)

The fixture loader module provides typed access to movie data with built-in validation.

#### Exported Members

```typescript
// Typed movie data array
export const movies: Movie[]

// Load movies function
export function loadMovies(): Movie[]

// Validation function
export function validateMoviesFixture(
  data?: Movie[]
): FixtureValidationResult

// Validation result (run at module load)
export const moviesFixtureValidation: FixtureValidationResult
```

### Adding New Movies

To add movies to the fixture:

1. Edit `frontend/fixtures/movies.json`
2. Add a new movie object following the `Movie` type schema
3. Ensure all required fields are present
4. Run the app to trigger validation: `npm run dev`
5. Check console for validation errors

**Example**:

```json
{
  "id": "unique-movie-id",
  "title": "New Movie Title",
  "releaseYear": 2024,
  "posterUrl": "https://example.com/poster.jpg",
  "synopsis": "A brief description of the movie plot.",
  "cast": [
    "Actor One",
    "Actor Two"
  ],
  "reviews": [
    {
      "id": "review-1",
      "author": "Reviewer Name",
      "rating": 8,
      "text": "Great movie!"
    }
  ]
}
```

## Data Validation

The application includes **runtime validation** to ensure fixture data integrity.

### Validation Types

```typescript
interface FixtureValidationIssue {
  movieId: string | number;  // ID of the problematic movie
  path: string;              // Path to the invalid field
  message: string;           // Human-readable error message
}

interface FixtureValidationResult {
  valid: boolean;                  // Overall validation status
  issues: FixtureValidationIssue[]; // Array of validation issues
}
```

### Validation Rules

The `validateMoviesFixture()` function validates:

#### Movie-Level Validation

| Field | Rule | Error Message |
|-------|------|---------------|
| `id` | Must be non-empty string | "id must be non-empty string" |
| `title` | Must be non-empty string | "title must be non-empty string" |
| `releaseYear` | Must be number between 1900 and (current year + 2) | "releaseYear must be a plausible number" |

#### Review-Level Validation

| Field | Rule | Error Message |
|-------|------|---------------|
| `author` | Must be non-empty string | "author must be non-empty string" |
| `text` | Must be non-empty string (if present) | "text must be non-empty string" |
| `rating` | Must be number between 0 and 10 (inclusive) | "rating must be 0-10" |

### Validation Helper Functions

```typescript
// Check if value is non-empty string
const isNonEmptyString = (v: unknown): v is string =>
  typeof v === "string" && v.trim().length > 0;

// Check if value is a plausible year
const isYear = (v: unknown): v is number =>
  typeof v === "number" && v > 1900 && v < new Date().getFullYear() + 2;
```

### Using Validation

#### Automatic Validation

Validation runs automatically when the fixtures module loads:

```typescript
import { moviesFixtureValidation } from '@/lib/fixtures';

// Check validation result
if (!moviesFixtureValidation.valid) {
  console.error('Fixture validation failed:', moviesFixtureValidation.issues);
}
```

#### Manual Validation

You can also run validation manually:

```typescript
import { validateMoviesFixture } from '@/lib/fixtures';

const result = validateMoviesFixture(customMovieData);

if (!result.valid) {
  result.issues.forEach(issue => {
    console.error(
      `Movie ${issue.movieId}: ${issue.path} - ${issue.message}`
    );
  });
}
```

### Validation Example Output

```javascript
{
  valid: false,
  issues: [
    {
      movieId: "the-matrix",
      path: "reviews[0].rating",
      message: "rating must be 0-10"
    },
    {
      movieId: "inception",
      path: "releaseYear",
      message: "releaseYear must be a plausible number"
    }
  ]
}
```

## Data Access

### Loading All Movies

```typescript
import { loadMovies } from '@/lib/fixtures';

const allMovies = loadMovies();
// Returns: Movie[]
```

### Finding a Movie by ID

```typescript
import { movies } from '@/lib/fixtures';

const movie = movies.find(m => m.id === 'inception');
// Returns: Movie | undefined
```

### Filtering Movies

```typescript
import { movies } from '@/lib/fixtures';

// Filter by year
const movies2010 = movies.filter(m => m.releaseYear === 2010);

// Search by title
const searchResults = movies.filter(m =>
  m.title.toLowerCase().includes(searchQuery.toLowerCase())
);

// Filter by cast member
const moviesWithActor = movies.filter(m =>
  m.cast?.some(actor => actor.includes('Leonardo DiCaprio'))
);
```

### Accessing Reviews

```typescript
import { movies } from '@/lib/fixtures';

const movie = movies.find(m => m.id === 'inception');
const reviews = movie?.reviews ?? [];

// Calculate average rating
const avgRating = reviews.length > 0
  ? reviews.reduce((sum, r) => sum + r.rating, 0) / reviews.length
  : 0;
```

## Error Handling

### Missing Movie

When a movie is not found by ID:

```typescript
import { movies } from '@/lib/fixtures';

const movieId = 'non-existent-movie';
const movie = movies.find(m => m.id === movieId);

if (!movie) {
  // Handle missing movie case
  // Typically: show 404 page or error message
  return {
    notFound: true, // Next.js 404
  };
}
```

### Invalid Fixture Data

When fixture validation fails:

```typescript
import { moviesFixtureValidation } from '@/lib/fixtures';

if (!moviesFixtureValidation.valid) {
  // Log validation errors (development)
  if (process.env.NODE_ENV === 'development') {
    console.error('Fixture validation failed:');
    moviesFixtureValidation.issues.forEach(issue => {
      console.error(`  ${issue.movieId} - ${issue.path}: ${issue.message}`);
    });
  }

  // Handle in production (optional)
  // Could show error page or use default empty array
}
```

### Missing Optional Fields

Always check optional fields before use:

```typescript
const movie = movies.find(m => m.id === 'inception');

// Safe access to optional fields
const posterUrl = movie?.posterUrl ?? '/placeholder.jpg';
const synopsis = movie?.synopsis ?? 'No synopsis available.';
const cast = movie?.cast ?? [];
const reviews = movie?.reviews ?? [];
```

### Type Guards

Use TypeScript type guards for runtime type safety:

```typescript
function hasReviews(movie: Movie): movie is Movie & { reviews: Review[] } {
  return Array.isArray(movie.reviews) && movie.reviews.length > 0;
}

const movie = movies.find(m => m.id === 'inception');

if (movie && hasReviews(movie)) {
  // TypeScript knows movie.reviews is Review[] here
  const avgRating = movie.reviews.reduce((sum, r) => sum + r.rating, 0) / movie.reviews.length;
}
```

## Best Practices

### 1. Always Use Type Imports

```typescript
import { Movie, Review } from '@/types/models';
import { loadMovies } from '@/lib/fixtures';
```

### 2. Validate Before Use

```typescript
import { moviesFixtureValidation } from '@/lib/fixtures';

// Check validation in development
if (process.env.NODE_ENV === 'development' && !moviesFixtureValidation.valid) {
  console.warn('Fixture validation issues detected');
}
```

### 3. Handle Missing Data Gracefully

```typescript
const movie = movies.find(m => m.id === id);

// Always provide fallbacks
const title = movie?.title ?? 'Unknown Movie';
const year = movie?.releaseYear ?? new Date().getFullYear();
```

### 4. Use Optional Chaining

```typescript
// Good: Safe access
const firstReview = movie?.reviews?.[0];

// Bad: Unsafe access
const firstReview = movie.reviews[0]; // May throw error
```

### 5. Maintain Data Consistency

When updating fixtures:
- Update `types/models.ts` if changing data structure
- Update `lib/fixtures.ts` validation if adding new rules
- Update relevant components that consume the data
- Run tests to ensure no regressions

---

## Examples

### Complete Movie Listing Component

```typescript
import { loadMovies } from '@/lib/fixtures';
import { Movie } from '@/types/models';

export default function MovieList() {
  const movies = loadMovies();

  return (
    <div>
      {movies.map(movie => (
        <div key={movie.id}>
          <h2>{movie.title} ({movie.releaseYear})</h2>
          {movie.posterUrl && (
            <img src={movie.posterUrl} alt={movie.title} />
          )}
          <p>{movie.synopsis ?? 'No synopsis available.'}</p>
        </div>
      ))}
    </div>
  );
}
```

### Movie Detail Page with Validation

```typescript
import { GetStaticProps, GetStaticPaths } from 'next';
import { movies } from '@/lib/fixtures';
import { Movie } from '@/types/models';

export const getStaticPaths: GetStaticPaths = async () => {
  const paths = movies.map(movie => ({
    params: { id: movie.id },
  }));

  return { paths, fallback: false };
};

export const getStaticProps: GetStaticProps = async ({ params }) => {
  const movie = movies.find(m => m.id === params?.id);

  if (!movie) {
    return { notFound: true };
  }

  return {
    props: { movie },
  };
};

export default function MovieDetailPage({ movie }: { movie: Movie }) {
  return (
    <div>
      <h1>{movie.title}</h1>
      <p>Released: {movie.releaseYear}</p>
      {movie.cast && (
        <div>
          <h2>Cast</h2>
          <ul>
            {movie.cast.map((actor, i) => (
              <li key={i}>{actor}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}
```

---

For more information, see:
- [Type Definitions](../frontend/src/types/models.ts)
- [Fixture Loader](../frontend/src/lib/fixtures.ts)
- [Movie Fixtures](../frontend/fixtures/movies.json)

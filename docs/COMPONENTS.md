# Component Documentation

This document provides detailed documentation for all React components in the Movie Review Website.

## Table of Contents

- [Component Overview](#component-overview)
- [Layout Components](#layout-components)
  - [Layout](#layout)
  - [Header](#header)
- [Feature Components](#feature-components)
  - [MovieCard](#moviecard)
  - [MovieDetail](#moviedetail)
  - [ReviewList](#reviewlist)
  - [SearchBar](#searchbar)
  - [EmptyState](#emptystate)
- [UI Components](#ui-components)
- [Component Patterns](#component-patterns)
- [Accessibility Guidelines](#accessibility-guidelines)

## Component Overview

All components are located in [frontend/src/components/](../frontend/src/components/).

### Component Architecture

```
components/
├── Layout.tsx          # App wrapper with header/footer
├── Header.tsx          # Navigation header
├── MovieCard.tsx       # Movie thumbnail card
├── MovieDetail.tsx     # Full movie details
├── ReviewList.tsx      # Review display
├── SearchBar.tsx       # Search input with real-time filtering
├── EmptyState.tsx      # Empty state messaging
└── ui/                 # shadcn/ui components
    ├── Button.tsx
    └── index.ts
```

### Technology Stack

- **React 18.2.0** - Functional components with hooks
- **TypeScript** - Full type safety
- **Next.js** - Server-side rendering and routing
- **Tailwind CSS** - Utility-first styling
- **shadcn/ui** - Component library

---

## Layout Components

### Layout

The main layout wrapper that provides consistent structure across all pages.

**Location**: [frontend/src/components/Layout.tsx](../frontend/src/components/Layout.tsx)

#### Props

```typescript
type Props = {
  children: React.ReactNode;  // Page content to render
  title?: string;             // Page title (default: "Movie Reviews")
}
```

#### Usage

```tsx
import Layout from '@/components/Layout';

export default function MyPage() {
  return (
    <Layout title="Movie Detail - Inception">
      <div>Your page content here</div>
    </Layout>
  );
}
```

#### Features

- **Dynamic page title** - Sets `<title>` tag via Next.js `<Head>`
- **Responsive viewport** - Sets viewport meta tag
- **Consistent structure** - Header, main content area, and footer
- **Automatic copyright year** - Displays current year in footer

#### Structure

```html
<Head>
  <title>{title}</title>
  <meta name="viewport" content="width=device-width, initial-scale=1" />
</Head>
<div className="site-container">
  <header className="site-header">
    <h1 className="site-title">Movie Reviews</h1>
  </header>
  <main className="site-main">
    {children}
  </main>
  <footer className="site-footer">
    © {currentYear} Movie Reviews
  </footer>
</div>
```

#### Styling Classes

- `site-container` - Main wrapper
- `site-header` - Header area
- `site-title` - Site title text
- `site-main` - Main content area
- `site-footer` - Footer area

#### Example

```tsx
// pages/index.tsx
import Layout from '@/components/Layout';

export default function HomePage() {
  return (
    <Layout title="Home - Movie Reviews">
      <h1>Welcome to Movie Reviews</h1>
      <p>Browse our collection of movies.</p>
    </Layout>
  );
}
```

---

### Header

Navigation header component (currently simplified).

**Location**: [frontend/src/components/Header.tsx](../frontend/src/components/Header.tsx)

#### Props

None (stateless component)

#### Usage

```tsx
import Header from '@/components/Header';

<Header />
```

#### Features

- **Home navigation** - Link to homepage
- **Semantic HTML** - Uses `<nav>` element

#### Structure

```html
<div className="site-header-inner">
  <nav>
    <a href="/">Home</a>
  </nav>
</div>
```

#### Accessibility

- Wrapped in `<nav>` landmark for screen readers
- Clear link text ("Home")

#### Future Enhancements

This component can be extended to include:
- Mobile menu toggle
- Additional navigation links
- Search integration
- User account dropdown

---

## Feature Components

### MovieCard

Displays a movie as a clickable card with poster, title, and year.

**Location**: [frontend/src/components/MovieCard.tsx](../frontend/src/components/MovieCard.tsx)

#### Props

```typescript
type Props = {
  movie: Movie;  // Movie object from fixtures
}
```

#### Type Dependencies

```typescript
import type { Movie } from '@/types/models';
```

#### Usage

```tsx
import MovieCard from '@/components/MovieCard';
import { loadMovies } from '@/lib/fixtures';

export default function MovieList() {
  const movies = loadMovies();

  return (
    <div className="movie-grid">
      {movies.map(movie => (
        <MovieCard key={movie.id} movie={movie} />
      ))}
    </div>
  );
}
```

#### Features

- **Clickable card** - Links to movie detail page
- **Poster image** - Displays movie poster with fallback
- **Movie metadata** - Shows title and release year
- **Accessible labels** - ARIA labels for screen readers

#### Structure

```html
<article className="movie-card">
  <Link href="/movies/{movie.id}" aria-label="View details for {movie.title}">
    <img
      src={movie.posterUrl ?? "/posters/placeholder.png"}
      alt="{movie.title} poster"
      width={150}
      height={225}
    />
    <div className="movie-meta">
      <h2>{movie.title}</h2>
      <p className="movie-year">{movie.releaseYear}</p>
    </div>
  </Link>
</article>
```

#### Styling Classes

- `movie-card` - Card container
- `movie-meta` - Metadata section
- `movie-year` - Release year text

#### Accessibility

- `<article>` semantic element for each movie
- `aria-label` on link provides context
- `alt` text on image describes poster
- Explicit `width` and `height` prevent layout shift

#### Image Handling

**Poster URL**: Uses `movie.posterUrl` if available, otherwise falls back to `/posters/placeholder.png`

```typescript
src={movie.posterUrl ?? "/posters/placeholder.png"}
```

#### Example

```tsx
const movie = {
  id: "inception",
  title: "Inception",
  releaseYear: 2010,
  posterUrl: "https://example.com/inception.jpg"
};

<MovieCard movie={movie} />
```

---

### MovieDetail

Displays comprehensive movie information including poster, synopsis, cast, and reviews.

**Location**: [frontend/src/components/MovieDetail.tsx](../frontend/src/components/MovieDetail.tsx)

#### Props

```typescript
type Props = {
  movie: Movie;  // Complete movie object with optional fields
}
```

#### Type Dependencies

```typescript
import type { Movie } from '@/types/models';
import ReviewList from '@/components/ReviewList';
```

#### Usage

```tsx
import MovieDetail from '@/components/MovieDetail';
import { movies } from '@/lib/fixtures';

export default function MovieDetailPage({ params }) {
  const movie = movies.find(m => m.id === params.id);

  if (!movie) {
    return <div>Movie not found</div>;
  }

  return <MovieDetail movie={movie} />;
}
```

#### Features

- **Grid layout** - Poster and metadata side-by-side
- **Conditional rendering** - Only shows sections with data
- **Review integration** - Embeds ReviewList component
- **Semantic HTML** - Uses `<article>` and `<section>` elements

#### Structure

```html
<article className="movie-detail">
  <div className="movie-detail-grid">
    <!-- Poster -->
    <img
      src={movie.posterUrl ?? "/posters/placeholder.png"}
      alt="{movie.title} poster"
      width={300}
      height={450}
    />

    <!-- Metadata -->
    <div className="movie-detail-meta">
      <h1>{movie.title}</h1>
      <p className="movie-year">{movie.releaseYear}</p>

      <!-- Synopsis (if available) -->
      {movie.synopsis && (
        <section>
          <h2>Synopsis</h2>
          <p>{movie.synopsis}</p>
        </section>
      )}

      <!-- Cast (if available) -->
      {movie.cast && movie.cast.length > 0 && (
        <section>
          <h3>Cast</h3>
          <ul>
            {movie.cast.map(actor => (
              <li key={actor}>{actor}</li>
            ))}
          </ul>
        </section>
      )}
    </div>
  </div>

  <!-- Reviews -->
  <section className="movie-reviews">
    <h2>Reviews</h2>
    <ReviewList reviews={movie.reviews} />
  </section>
</article>
```

#### Styling Classes

- `movie-detail` - Main container
- `movie-detail-grid` - Grid layout for poster and metadata
- `movie-detail-meta` - Metadata section
- `movie-year` - Release year text
- `movie-reviews` - Reviews section

#### Conditional Rendering

The component only renders sections when data is available:

```tsx
// Synopsis - only if movie.synopsis exists
{movie.synopsis && (
  <section>
    <h2>Synopsis</h2>
    <p>{movie.synopsis}</p>
  </section>
)}

// Cast - only if movie.cast exists and has items
{movie.cast && movie.cast.length > 0 && (
  <section>
    <h3>Cast</h3>
    <ul>
      {movie.cast.map(actor => (
        <li key={actor}>{actor}</li>
      ))}
    </ul>
  </section>
)}
```

#### Accessibility

- `<h1>` for movie title (page heading)
- `<h2>` and `<h3>` for proper heading hierarchy
- `<section>` elements for semantic structure
- `alt` text on poster image

#### Example

```tsx
const movie = {
  id: "inception",
  title: "Inception",
  releaseYear: 2010,
  posterUrl: "https://example.com/inception.jpg",
  synopsis: "A thief who steals corporate secrets...",
  cast: ["Leonardo DiCaprio", "Joseph Gordon-Levitt"],
  reviews: [
    { id: "1", author: "John Doe", rating: 9, text: "Amazing!" }
  ]
};

<MovieDetail movie={movie} />
```

---

### ReviewList

Displays a list of movie reviews with ratings.

**Location**: [frontend/src/components/ReviewList.tsx](../frontend/src/components/ReviewList.tsx)

#### Props

```typescript
type Props = {
  reviews?: Review[];  // Optional array of reviews
}
```

#### Type Dependencies

```typescript
import type { Review } from '@/types/models';
```

#### Usage

```tsx
import ReviewList from '@/components/ReviewList';

const reviews = [
  { id: "1", author: "John Doe", rating: 9, text: "Excellent movie!" },
  { id: "2", author: "Jane Smith", rating: 8.5, text: "Very good." }
];

<ReviewList reviews={reviews} />
```

#### Features

- **Empty state handling** - Shows message when no reviews
- **Optional text** - Handles reviews without text
- **List semantics** - Uses `<ul>` and `<li>` elements

#### Structure

**With reviews**:
```html
<ul className="review-list">
  {reviews.map(review => (
    <li key={review.id} className="review-item">
      <strong>{review.author}</strong> — <span>Rating: {review.rating}</span>
      {review.text && <p>{review.text}</p>}
    </li>
  ))}
</ul>
```

**Without reviews**:
```html
<div>No reviews yet.</div>
```

#### Styling Classes

- `review-list` - List container
- `review-item` - Individual review

#### Empty State

The component handles three cases:

1. **`undefined` reviews**: Shows "No reviews yet."
2. **Empty array**: Shows "No reviews yet."
3. **Array with items**: Renders list

```tsx
if (!reviews || reviews.length === 0) {
  return <div>No reviews yet.</div>;
}
```

#### Conditional Text Rendering

Review text is optional and only rendered if present:

```tsx
{review.text && <p>{review.text}</p>}
```

#### Accessibility

- Uses semantic `<ul>` and `<li>` elements
- Each review has unique `key` prop
- Author emphasized with `<strong>`

#### Example

```tsx
// With reviews
const reviews = [
  {
    id: "review-1",
    author: "Alice Johnson",
    rating: 9.5,
    text: "A masterpiece of modern cinema!"
  },
  {
    id: "review-2",
    author: "Bob Williams",
    rating: 8,
    text: null  // Optional text
  }
];

<ReviewList reviews={reviews} />

// Without reviews
<ReviewList reviews={[]} />  // Shows "No reviews yet."
<ReviewList />              // Shows "No reviews yet."
```

---

### SearchBar

Search input component with real-time filtering.

**Location**: [frontend/src/components/SearchBar.tsx](../frontend/src/components/SearchBar.tsx)

#### Props

```typescript
type Props = {
  onSearch: (query: string) => void;  // Callback fired on search
  placeholder?: string;               // Input placeholder (default: "Search movies...")
}
```

#### Usage

```tsx
import SearchBar from '@/components/SearchBar';
import { useState } from 'react';

export default function MoviePage() {
  const [searchQuery, setSearchQuery] = useState('');

  const handleSearch = (query: string) => {
    setSearchQuery(query);
    // Filter movies based on query
  };

  return (
    <SearchBar
      onSearch={handleSearch}
      placeholder="Search by title or year..."
    />
  );
}
```

#### Features

- **Real-time search** - Fires `onSearch` on every keystroke
- **Form submission** - Handles Enter key via form submit
- **Trimmed values** - Automatically trims whitespace
- **Accessible labels** - Screen reader friendly
- **Controlled input** - Uses React state

#### State Management

```tsx
const [value, setValue] = useState("");
```

#### Structure

```html
<form
  role="search"
  aria-label="Movie search"
  onSubmit={handleSubmit}
  className="search-bar"
>
  <label htmlFor="movie-search" className="visually-hidden">
    Search movies
  </label>
  <input
    id="movie-search"
    name="q"
    type="text"
    value={value}
    placeholder={placeholder}
    onChange={handleChange}
  />
  <button type="submit">Search</button>
</form>
```

#### Event Handlers

**onChange** - Real-time search:
```tsx
onChange={(e) => {
  const v = e.target.value;
  setValue(v);
  onSearch(v.trim());  // Fires callback
}}
```

**onSubmit** - Form submission:
```tsx
onSubmit={(e) => {
  e.preventDefault();
  onSearch(value.trim());
}}
```

#### Styling Classes

- `search-bar` - Form container
- `visually-hidden` - Screen reader only label

#### Accessibility

- `role="search"` - Landmark role for screen readers
- `aria-label="Movie search"` - Form label
- `<label>` element with `htmlFor` - Associates label with input
- `visually-hidden` class - Hides label visually but keeps it for screen readers

#### Example

```tsx
import SearchBar from '@/components/SearchBar';
import { useState } from 'react';
import { movies } from '@/lib/fixtures';

export default function MovieListing() {
  const [filtered, setFiltered] = useState(movies);

  const handleSearch = (query: string) => {
    if (!query) {
      setFiltered(movies);
      return;
    }

    const results = movies.filter(movie =>
      movie.title.toLowerCase().includes(query.toLowerCase()) ||
      movie.releaseYear.toString().includes(query)
    );

    setFiltered(results);
  };

  return (
    <>
      <SearchBar onSearch={handleSearch} />
      <div className="movie-grid">
        {filtered.map(movie => (
          <MovieCard key={movie.id} movie={movie} />
        ))}
      </div>
    </>
  );
}
```

---

### EmptyState

Displays a message when no content is available.

**Location**: [frontend/src/components/EmptyState.tsx](../frontend/src/components/EmptyState.tsx)

#### Props

```typescript
type Props = {
  message?: string;  // Message to display (default: "No movies available.")
}
```

#### Usage

```tsx
import EmptyState from '@/components/EmptyState';

// Default message
<EmptyState />

// Custom message
<EmptyState message="No search results found." />
```

#### Features

- **Configurable message** - Custom text via props
- **Simple styling** - Single class for easy customization

#### Structure

```html
<div className="empty-state">
  {message}
</div>
```

#### Styling Classes

- `empty-state` - Container for styling

#### Example

```tsx
import EmptyState from '@/components/EmptyState';

export default function SearchResults({ results }) {
  if (results.length === 0) {
    return <EmptyState message="No movies match your search." />;
  }

  return (
    <div className="results">
      {results.map(movie => (
        <MovieCard key={movie.id} movie={movie} />
      ))}
    </div>
  );
}
```

---

## UI Components

### shadcn/ui Components

**Location**: [frontend/src/components/ui/](../frontend/src/components/ui/)

The project uses [shadcn/ui](https://ui.shadcn.com/) for pre-built, accessible components.

#### Available Components

- **Button** - [Button.tsx](../frontend/src/components/ui/Button.tsx)

#### Configuration

**Config file**: [components.json](../frontend/components.json)

#### Adding New Components

```bash
npx shadcn-ui@latest add [component-name]
```

Example:
```bash
npx shadcn-ui@latest add dialog
npx shadcn-ui@latest add dropdown-menu
```

#### Usage

```tsx
import { Button } from '@/components/ui/Button';

<Button variant="primary" size="lg">
  Click me
</Button>
```

---

## Component Patterns

### Functional Components

All components use **functional components** with hooks (no class components).

```tsx
export default function MyComponent({ prop1, prop2 }: Props) {
  return <div>...</div>;
}
```

### TypeScript Props

All components have **typed props** for type safety:

```tsx
type Props = {
  required: string;
  optional?: number;
};

export default function Component({ required, optional }: Props) {
  // ...
}
```

### Conditional Rendering

Use **logical AND** for optional content:

```tsx
{movie.synopsis && (
  <p>{movie.synopsis}</p>
)}
```

Use **ternary** for either/or:

```tsx
{reviews.length > 0 ? (
  <ReviewList reviews={reviews} />
) : (
  <EmptyState message="No reviews yet." />
)}
```

### Nullish Coalescing

Use **`??`** for default values:

```tsx
const posterUrl = movie.posterUrl ?? "/placeholder.png";
const title = movie.title ?? "Unknown";
```

### Optional Chaining

Use **`?.`** for safe property access:

```tsx
const firstReview = movie.reviews?.[0];
const authorName = review?.author;
```

### Map with Keys

Always provide **unique keys** when mapping:

```tsx
{movies.map(movie => (
  <MovieCard key={movie.id} movie={movie} />
))}
```

---

## Accessibility Guidelines

### Semantic HTML

Use semantic elements for meaning:

- `<article>` - Self-contained content (movie cards, detail pages)
- `<section>` - Thematic grouping (synopsis, cast, reviews)
- `<nav>` - Navigation links
- `<main>` - Primary content
- `<header>` - Page header
- `<footer>` - Page footer

### ARIA Labels

Provide context for screen readers:

```tsx
<Link
  href={`/movies/${movie.id}`}
  aria-label={`View details for ${movie.title}`}
>
  {/* ... */}
</Link>
```

### Form Accessibility

- Use `<label>` elements with `htmlFor`
- Add `role="search"` to search forms
- Provide `aria-label` for forms

```tsx
<form role="search" aria-label="Movie search">
  <label htmlFor="movie-search" className="visually-hidden">
    Search movies
  </label>
  <input id="movie-search" type="text" />
</form>
```

### Image Alt Text

Always provide descriptive `alt` attributes:

```tsx
<img
  src={movie.posterUrl}
  alt={`${movie.title} poster`}
  width={300}
  height={450}
/>
```

### Heading Hierarchy

Maintain proper heading order:

- `<h1>` - Page title (one per page)
- `<h2>` - Major sections
- `<h3>` - Subsections
- Never skip levels

### Keyboard Navigation

All interactive elements should be keyboard accessible:

- Links and buttons are focusable by default
- Test with Tab key
- Ensure visible focus indicators

### Screen Reader Testing

Test with screen readers:

- NVDA (Windows)
- JAWS (Windows)
- VoiceOver (macOS/iOS)
- TalkBack (Android)

---

## Component Testing

### Unit Tests

All components have corresponding test files in [frontend/src/tests/](../frontend/src/tests/):

- [MovieCard.test.tsx](../frontend/src/tests/MovieCard.test.tsx)
- [MovieDetail.test.tsx](../frontend/src/tests/MovieDetail.test.tsx)
- [SearchBar.test.tsx](../frontend/src/tests/SearchBar.test.tsx)

### Testing Example

```tsx
import { render, screen } from '@testing-library/react';
import MovieCard from '@/components/MovieCard';

test('renders movie title', () => {
  const movie = {
    id: "1",
    title: "Test Movie",
    releaseYear: 2024
  };

  render(<MovieCard movie={movie} />);

  expect(screen.getByText("Test Movie")).toBeInTheDocument();
  expect(screen.getByText("2024")).toBeInTheDocument();
});
```

---

## Best Practices

1. **Type all props** - Always define TypeScript types for props
2. **Handle optional data** - Use `??` and `?.` for optional fields
3. **Provide keys** - Use unique keys in `.map()`
4. **Use semantic HTML** - Choose appropriate HTML elements
5. **Add ARIA labels** - Enhance accessibility
6. **Test components** - Write unit tests for each component
7. **Keep components focused** - Single responsibility principle
8. **Extract reusable logic** - Use custom hooks for shared logic
9. **Document complex logic** - Add comments for non-obvious code
10. **Follow naming conventions** - PascalCase for components, camelCase for functions

---

For more information, see:
- [Type Definitions](../frontend/src/types/models.ts)
- [Component Tests](../frontend/src/tests/)
- [API Documentation](API.md)

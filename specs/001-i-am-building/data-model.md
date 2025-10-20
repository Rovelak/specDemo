# data-model.md

**Feature**: Movie Review Website — Landing + Movie Pages
**Created**: 2025-10-15

## Entities

### Movie

- id: string (unique identifier, slug or UUID)
- title: string (required)
- releaseYear: integer (required)
- posterUrl: string (optional)
- synopsis: string (optional)
- cast: array of strings (optional)
- reviews: array of Review (optional)

Validation rules:

- id: non-empty, URL-safe if used in paths
- title: non-empty, max length 200
- releaseYear: four-digit year between 1888 and current year +1
- posterUrl: if present, valid URL or relative path to `public/`
- synopsis: max length 5000 (UI may truncate)
- cast entries: non-empty strings, max 100 per cast member name

### Review

- id: string (unique)
- author: string (required)
- rating: integer (1-5, required)
- text: string (optional)

Validation rules:

- rating: integer between 1 and 5
- author: non-empty, max length 100
- text: max length 2000

## Relationships

- Movie.reviews -> [Review]

## Notes on storage

- Data is embedded in fixtures (JSON files) and loaded at build/runtime as static data. No persistence required for MVP.

# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **Next.js movie review website** built from a Specify template. The project uses **static mock data** (no backend/API) and implements a landing page with movie listings and individual movie detail pages. The codebase is structured with specifications in `specs/` and a frontend-only implementation.

## Development Commands

All commands are run from the `frontend/` directory:

```bash
cd frontend

# Development server (runs on localhost:3000)
npm run dev

# Production build
npm run build

# Start production server
npm run start

# Run linting
npm run lint

# Run Jest unit tests
npm test

# Run Playwright E2E tests (auto-starts dev server)
npm run test:e2e
```

## Architecture

### Data Flow

The application uses a **fixture-based data architecture** with no external API:

1. **Source of truth**: `frontend/fixtures/movies.json` contains all movie data
2. **Data loader**: `frontend/src/lib/fixtures.ts` loads and validates fixture data
3. **Type safety**: `frontend/src/types/models.ts` defines `Movie` and `Review` types
4. **Validation**: The fixtures module includes runtime validation (`validateMoviesFixture()`) that checks data integrity on load

### Key Architectural Patterns

- **Pages Router**: Uses Next.js Pages Router (not App Router)

  - Landing: `src/pages/index.tsx`
  - Movie detail: `src/pages/movies/[id].tsx` (dynamic route)
  - App wrapper: `src/pages/_app.tsx`

- **Component Structure**:

  - Presentational components in `src/components/`
  - shadcn/ui components in `src/components/ui/` (Tailwind-based)
  - Layout wrapper: `src/components/Layout.tsx`

- **Styling**: Tailwind CSS with shadcn/ui design system
  - Config: `tailwind.config.js`, `components.json`
  - Utilities: `src/lib/utils.ts` (cn() helper for className merging)

### Security Configuration

`next.config.js` includes strict security headers (CSP, HSTS, X-Frame-Options, etc.). When modifying the config:

- Current CSP allows `'unsafe-inline'` and `'unsafe-eval'` for scripts (noted as temporary)
- Adding external image domains requires updating `images.domains` array
- Adding external APIs requires updating CSP `connect-src` directive

## Testing Strategy

### Unit Tests (Jest)

- Config: `jest.config.js`
- Setup: `tests/setupTests.ts`
- Test files colocated with source: `src/tests/`
- Uses `@testing-library/react` and `@testing-library/jest-dom`

### E2E Tests (Playwright)

- Config: `playwright.config.ts`
- Test directory: `tests/e2e/`
- Automatically starts dev server on port 3000
- Retries failed tests once
- Generates traces on first retry

### Running a Single Test

```bash
# Jest - specific file
npm test -- path/to/file.test.ts

# Playwright - specific test file
npx playwright test tests/e2e/specific-test.spec.ts

# Playwright - specific test by name
npx playwright test -g "test name pattern"
```

## Specify Integration

This project was built from a Specify template and uses specification-driven development:

- **Specs location**: `specs/001-i-am-building/`
- **Active spec**: `spec.md` defines user stories, requirements, and acceptance criteria
- **Supporting docs**: `plan.md`, `tasks.md`, `test-plan.md`, `security.md`, `a11y-report.md`
- **Copilot guidance**: `.github/copilot-instructions.md` (auto-generated from feature plans)

When implementing new features, refer to the spec documents for context on requirements, priorities, and test scenarios.

## Important Constraints

1. **No backend**: All data comes from `fixtures/movies.json` - do not attempt to fetch from external APIs
2. **Node.js 22+**: Locked via `.nvmrc` and `engines` in `package.json`
3. **Static export compatibility**: Next.js config should support static export (no server-side runtime dependencies)
4. **Fixture validation**: When modifying movie data structure, update both `types/models.ts` and `lib/fixtures.ts` validation logic

## Working with Movie Data

To modify the movie dataset:

1. Edit `frontend/fixtures/movies.json`
2. Ensure data matches the `Movie` type in `src/types/models.ts`
3. Run `npm run dev` and check console for validation errors from `validateMoviesFixture()`
4. If adding new fields, update:
   - Type definitions in `src/types/models.ts`
   - Validation logic in `src/lib/fixtures.ts`
   - Relevant components that display the data

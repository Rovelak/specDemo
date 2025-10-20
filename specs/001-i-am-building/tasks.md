# Tasks: Movie Review Website — Landing + Movie Pages

**Feature**: Movie Review Website — Landing + Movie Pages
**Spec**: spec.md
**Plan**: plan.md

## Phase 1: Setup (project initialization)

- [x] T001 Initialize Next.js + TypeScript project at `frontend/` with Node 22 settings (create package.json, tsconfig.json, .nvmrc)
- [x] T002 Create `fixtures/movies.json` with example mock data and place under `frontend/fixtures/movies.json`
- [x] T003 Add basic project files: `.gitignore`, `README.md`, and `next.config.js` in `frontend/`
- [x] T004 Add ESLint and Prettier configs and a lint script in `frontend/package.json`

## Phase 2: Foundational (blocking prerequisites)

- [x] T005 [P] Create shared UI components directory `frontend/src/components/` and add `Layout.tsx` and `Header.tsx`
- [x] T006 [P] Add styling setup: `frontend/src/styles/globals.css` and link to `Layout.tsx`
- [x] T007 Add fixture loader utility at `frontend/src/lib/fixtures.ts` that reads `fixtures/movies.json` and exports typed models
- [x] T008 [P] Add basic TypeScript types for entities at `frontend/src/types/models.ts` (Movie, Review) based on `data-model.md`

## Phase 3: User Story 1 - Browse movies on landing (Priority: P1)

Story goal: Render a landing page that lists movies with title, release year, and thumbnail. Independent test: Open `/` and confirm list renders from fixtures.

- [x] T009 [US1] Create landing page at `frontend/src/pages/index.tsx` that imports fixtures and renders movie list
- [x] T010 [US1] Create `frontend/src/components/MovieCard.tsx` to display title, year, and thumbnail with accessible markup
- [x] T011 [US1] Implement routing from `MovieCard` to movie detail page (link to `/movies/[id]`) in `frontend/src/components/MovieCard.tsx`
- [x] T012 [US1] Add empty-state UI and tests: create `frontend/src/components/EmptyState.tsx` and use it when fixtures list is empty
- [x] T013 [US1] Add unit tests for `MovieCard` and `EmptyState` in `frontend/src/tests/` (jest + testing-library)

- [x] T026 [US1] Add Playwright smoke test in `frontend/tests/e2e/` that verifies landing page and one movie detail page render end-to-end

## Phase 4: User Story 2 - View movie details (Priority: P1)

Story goal: Display movie detail page with title, poster, synopsis, cast, and mocked reviews. Independent test: Open `/movies/{id}` and confirm fields render.

- [x] T014 [US2] Create dynamic movie page at `frontend/src/pages/movies/[id].tsx` using static generation from `fixtures/movies.json`
- [x] T015 [US2] Create `frontend/src/components/MovieDetail.tsx` to render title, poster, synopsis, cast, and reviews
- [x] T016 [US2] Create `frontend/src/components/ReviewList.tsx` and `frontend/src/components/ReviewItem.tsx` to display mocked reviews
- [x] T017 [US2] Add not-found handling: `frontend/src/pages/404.tsx` or inline handling in `[id].tsx` to show "Movie not found" and link to `/`
- [x] T018 [US2] Add unit tests for `MovieDetail` and `ReviewList` in `frontend/src/tests/`

## Phase 5: User Story 3 - Search and filter (Priority: P2)

Story goal: Provide a search input to filter movies by title (and optionally year). Independent test: Enter query and confirm list filters.

- [x] T019 [US3] Add `SearchBar` component at `frontend/src/components/SearchBar.tsx` and include on landing page
- [x] T020 [US3] Implement client-side filtering logic in `frontend/src/pages/index.tsx` or `frontend/src/lib/filter.ts`
- [x] T021 [US3] Add unit tests for `SearchBar` and filter logic in `frontend/src/tests/`

## Phase 6: Polish & Cross-Cutting Concerns

- [x] T022 Accessibility audit: run basic a11y checks and fix issues in components (report in `specs/001-i-am-building/a11y-report.md`)
- [x] T023 Performance checks: verify images are optimized and page load meets SC-001; document steps in `specs/001-i-am-building/perf.md`
- [x] T024 Add CI workflow file `.github/workflows/ci.yml` to run `npm ci`, `npm run build`, `npm run lint`, and `npm test` on pull requests
- [x] T025 Prepare PR from branch `001-i-am-building` with all changes and link to spec and plan
- [ ] T028 Add security headers & CSP documentation and host config in `specs/001-i-am-building/security.md` and include Vercel header settings
- [x] T028 Add security headers & CSP documentation and host config in `specs/001-i-am-building/security.md` and include Vercel header settings
- [x] T027 Add fixture validation utility and tests to ensure `movies.json` schema integrity

## Dependencies (story completion order)

1. Phase 1 (T001-T004) must complete before Phase 2
2. Phase 2 (T005-T008) must complete before Phase 3 and Phase 4
3. Phase 3 (US1) should be implemented first as MVP
4. Phase 4 (US2) depends on Phase 3 for navigation links
5. Phase 5 (US3) is independent but relies on Phase 3 components

## Parallel execution examples

- Parallelizable: T005, T006, T008 (components, styles, types) can be worked on in parallel by different engineers
- Parallelizable: T009 and T010 can be implemented simultaneously (page and card component)

## Implementation strategy

- MVP scope: Implement only User Story 1 (Phase 3) + essential foundational tasks (Phase 1 & 2). This yields a deployable, testable product.
- Incremental delivery: After MVP, implement User Story 2, then search/filter (US3), then polish tasks.

## Summary

- Total tasks: 25
- Tasks per story: US1=5 (T009-T013), US2=5 (T014-T018), US3=3 (T019-T021)
- Parallel opportunities: component creation and tests
- Independent test criteria included for each story phase

- Total tasks: 28
- Tasks per story: US1=6 (T009-T013, T026), US2=5 (T014-T018), US3=3 (T019-T021)
- Additional foundational/polish tasks: T024-T025, T027-T028

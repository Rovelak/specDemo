# test-plan.md

**Feature**: Movie Review Website — Landing + Movie Pages
**Created**: 2025-10-15

## Purpose

Provide explicit verification steps for the measurable success criteria SC-001 and SC-003.

## SC-001: Page load performance (2s)

- Environment: Developer machine or CI runner with Node 22, cold build; test in Chromium via Playwright.
- Measurement method: Use Playwright to navigate to `/` and record time from navigation start to `domcontentloaded` and `load` events. Use `performance.timing` if needed.
- Verification script: `frontend/tests/e2e/perf.spec.ts` should assert `domcontentloaded <= 2000ms` for landing page under cold conditions.
- Notes: Report the measured times in `specs/001-i-am-building/perf.md`.

## SC-003: Fallback/malformed data handling (95% rule)

- Procedure: Introduce a small set of malformed fixtures (missing posterUrl, missing synopsis, invalid year) into a test fixture file and run the app in test mode. Use Playwright to navigate through a sample of movie pages and assert no uncaught exceptions in the console and that fallback UI appears for missing fields.
- Pass criteria: At least 95% of tested pages show fallback UI correctly and no uncaught exceptions are reported.
- Implementation: Add `frontend/tests/fixtures/malformed-movies.json` and an E2E test `frontend/tests/e2e/fallback.spec.ts`.

## Running tests locally

```powershell
# from repo root
cd frontend
npm install
npm run build
npx playwright test frontend/tests/e2e --project=chromium
```

## Notes

- Tests should be added to CI and run on PRs. See `.github/workflows/ci.yml` (T024).

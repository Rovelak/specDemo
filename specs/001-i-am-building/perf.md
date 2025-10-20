# Performance & Fallback Verification

**Feature**: Movie Review Website — Landing + Movie Pages  
**Date**: 2025-10-20

## Success Criteria Referenced

- SC-001: Landing page static HTML should load (DOMContentLoaded) within ~2s on a typical developer machine (cold build, local dev) and <1s on production CDN for repeat visits.
- SC-003: Fallback behavior (empty fixtures or missing poster) displays graceful UI (EmptyState or placeholder image) without console errors.

## Measurement Procedure (Local)

1. Run `npm run build` then `npm start`.
2. Use Chrome DevTools Performance panel:
   - Record navigation to `/` (clear cache, disable cache).
   - Note `DOMContentLoaded` and `load` timestamps.
3. Repeat with disabled cache & throttled "Fast 3G" to estimate worst-case.
4. Record metrics in table below.

## Measurement Procedure (Fallback)

1. Temporarily rename `fixtures/movies.json` to `movies.bak.json` or modify loader to return `[]`.
2. Start app, navigate to `/` and confirm EmptyState renders and no runtime errors appear in console.
3. Restore fixtures.
4. For poster fallback: remove `posterUrl` from first movie; rebuild and confirm placeholder image renders.

## Metrics Log

| Date       | Env             | DCL (ms) | Load (ms) | Fast3G DCL (ms) | Notes                        |
| ---------- | --------------- | -------- | --------- | --------------- | ---------------------------- |
| 2025-10-20 | local dev build | TBD      | TBD       | TBD             | Initial baseline pending run |

## Optimization Opportunities (Initial)

- Use `next/image` for automatic image optimization once images exist.
- Preload hero font if custom fonts added later.
- Consider splitting SearchBar logic into dynamic import only if heavy (currently negligible).

## Status

Initial perf doc created (T023). Await baseline measurements.

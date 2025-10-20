# Accessibility Audit Report

**Feature**: Movie Review Website — Landing + Movie Pages  
**Date**: 2025-10-20  
**Scope**: Landing (`/`), Movie Detail (`/movies/[id]`), Search functionality

## Method

- Manual inspection of semantic elements (headings hierarchy, landmarks)
- Keyboard navigation test (Tab / Shift+Tab order)
- Basic color contrast spot check (body text vs background)
- ARIA usage review (none added yet; reliance on native semantics)

## Findings (Initial Pass)

| Area           | Status  | Notes                                                                                                                                                                   |
| -------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Headings       | OK      | Landing uses `h1` for site title (in Layout) and cards use `h2`; detail page uses `h1` for movie title.                                                                 |
| Images         | WARN    | Posters use `alt="<title> poster"`; consider more descriptive alt (e.g. just the movie title). Placeholder poster alt acceptable.                                       |
| Forms          | OK      | SearchBar has hidden label and role="search"; ensure visually-hidden CSS class exists.                                                                                  |
| Keyboard       | OK      | All interactive elements reachable; no custom key handlers required.                                                                                                    |
| Focus styling  | TODO    | Default browser outline present; consider explicit focus styles in CSS.                                                                                                 |
| Landmarks      | OK      | Layout wraps content; could add `header`, `main`, and `footer` semantic elements instead of divs for enhanced structure.                                                |
| Color contrast | TODO    | Need automated or manual contrast measurement; body text (#111) on white is fine, secondary text (#666) vs white borderline but acceptable (passes AA for normal text). |
| Skip link      | MISSING | Add a skip-to-content link for improved keyboard usability.                                                                                                             |

## Recommended Improvements

1. Replace structural divs in `Layout.tsx` with semantic elements: `<header>`, `<main>`, `<footer>`.
2. Add a global "Skip to content" link positioned absolutely at top when focused.
3. Introduce focus styles: e.g. `outline: 2px solid #005fcc; outline-offset: 2px;`.
4. Adjust poster `alt` to just the movie title (screen readers can infer it's an image).
5. Add visually-hidden utility class if not present to ensure `SearchBar` label is accessible.
6. Document contrast checks (run later with tooling like axe or Lighthouse).

## Next Steps

- Implement improvements in a follow-up polish commit.
- Re-run audit using an automated tool (axe DevTools / Lighthouse) and append results.
- Mark this report updated after changes.

## Audit Status

Initial audit complete; improvements identified (T022).

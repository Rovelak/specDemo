# Spec: React / Next.js App Constitution (Minimal)

Minimal, non-negotiable rules for building and maintaining a React app using Next.js. Keep changes small and explicit; follow this baseline for all releases.

## Core Principles

### I. Framework & Routing

Use Next.js (stable release). Prefer the App Router for new pages unless a clear reason requires the Pages Router. Explicitly document the router choice.

### II. Rendering & Data Fetching

Choose the simplest correct rendering strategy per page: Static (SSG) by default, Incremental Static Regeneration (ISR) when content can be stale-tolerant, Server-side Rendering (SSR) only when necessary, and Client-side fetching for purely interactive pieces.

### III. Minimal dependencies & Type Safety

Prefer TypeScript. Keep third-party dependencies minimal and reviewed. Avoid heavy client-side frameworks beyond React unless justified.

### IV. Accessibility & Content-first

Core content must render without client-side JS where feasible. Follow basic a11y practices (semantic HTML, alt text, keyboard focus, color contrast).

### V. Performance & Best Practices

Optimize images (Next/Image or pre-optimized assets), use code-splitting, avoid large client bundles, apply caching and compression, and use content-hash filenames for static assets.

### VI. Security & Privacy

No secrets in repo. Enforce HTTPS, use platform secrets for API keys, and follow CSP and secure headers. Avoid embedding third-party trackers without approval.

## Minimum Tech & Deployment Constraints

- Target hosting/platform: Vercel preferred (first-class Next.js support). Alternative hosts (Netlify, Cloudflare Pages, S3+CDN) are allowed if they meet SSR/edge function requirements used by the app.
- Use Next.js build (next build) and a reproducible build command in package.json (scripts.build). Lock node/npm versions in engines or use an .nvmrc.
- Environment variables: runtime vs build-time must be documented. Use NEXT*PUBLIC* for client-exposed variables and platform secret stores for private keys.
- CI must run the production build and a static analysis step (lint + typecheck) before merge.

## Development Workflow & Quality Gates

- Branching: Feature branches + pull request for main changes.
- CI checks (required):
  - TypeScript typecheck (if using TS)
  - ESLint
  - next build (production build) — fails on build errors
  - Optional: jest/unit tests for critical logic, and Playwright/Chromium smoke test for at least the root page
- PR reviews: Every PR requires a reviewer and a brief description of the impact (performance, SEO, APIs).

## Security & Operational Notes

- Secrets: Use host platform secret storage; never commit credentials. Scan for accidental secrets in CI.
- CSP and Security Headers: Add and document a Content Security Policy, HSTS, X-Frame-Options, and other headers via the host or middleware.
- Rate limits and error handling: Document expected API rate-limits and graceful fallback behavior for data-fetching failures.

## Observability & Monitoring

- Basic monitoring: deploy status and error reporting for server/edge functions. Avoid adding heavy analytics by default; document any analytics used.

## Governance

- This file is the baseline. Projects may add stricter rules but cannot relax these rules without documented approval from maintainers.
- Amendments: Edit this file and reference the rationale + migration steps in the PR. Minor wording edits require 1 maintainer sign-off; breaking changes require 2.

**Version**: 1.0.0 | **Ratified**: 2025-10-15 | **Last Amended**: 2025-10-15

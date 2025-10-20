# research.md

**Feature**: Movie Review Website — Landing + Movie Pages
**Created**: 2025-10-15

## Decisions

### Decision: TypeScript

- Decision: Adopt TypeScript for this feature
- Rationale: Provides early type safety for components and fixtures and aligns with the project's constitution that "prefers TypeScript".
- Alternatives considered: JavaScript only (faster to start) — rejected because type errors may slow future development and tests.

### Decision: Hosting target

- Decision: Target Vercel for initial deployments
- Rationale: First-class Next.js support and easy static deployments; simplifies CI and preview URLs.
- Alternatives considered: Netlify, Cloudflare Pages — viable but may require extra config for any SSR/edge in future.

### Decision: Node.js version

- Decision: Node.js 22.x (target)
  - Rationale: Use latest stable Node 22 to leverage modern language features and match the user's clarified target. Verify host support on Vercel and pin the version via `.nvmrc` or `engines` in package.json to ensure reproducible builds.
  - Alternatives considered: Node 18/20 — compatible, but Node 22 is chosen per clarification.

## Research tasks

- Implement TypeScript starter template for Next.js and add minimal tsconfig and types for fixtures
- Add `.nvmrc` or engines in package.json to lock Node 22
- Prepare Vercel deployment settings (build command: `npm run build`, output: static files)

## Consolidated findings

- Adopt TypeScript, lock Node 22, target Vercel for deployments. These choices resolve the main technical unknowns and keep the implementation aligned with the constitution.

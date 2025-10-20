# quickstart.md

**Feature**: Movie Review Website — Landing + Movie Pages

## Quickstart (local)

1. Install dependencies (Node 22.x recommended):

```powershell
npm install
```

2. Build the static site (uses mocked fixtures):

```powershell
npm run build
```

3. Run a local static server for preview (or use `npm run start` if Next dev server is used):

```powershell
npm run start
```

4. Open http://localhost:3000 and verify:

- Landing page shows a list of movies (title, year, thumbnail)
- Clicking a movie opens the movie detail page with synopsis and mocked reviews

## Notes

- Fixtures are located under `fixtures/` and are bundled with the app for the MVP.
- This feature targets Vercel for deployment. Ensure Vercel is configured to use Node 22 and to run `npm run build` as the build command.
- To run tests (if present): `npm test` or `npx playwright test` for E2E smoke tests.

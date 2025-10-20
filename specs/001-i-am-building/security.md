# security.md

**Feature**: Movie Review Website — Landing + Movie Pages
**Created**: 2025-10-15

## Purpose

Document minimal security headers and Content Security Policy (CSP) guidance for the static site deployment (Vercel recommended).

## Required headers (minimum)

- Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
- X-Frame-Options: DENY
- X-Content-Type-Options: nosniff
- Referrer-Policy: no-referrer-when-downgrade
- Permissions-Policy: geolocation=(), microphone=()

## Content Security Policy (example)

Add a conservative CSP that allows resources only from the same origin and trusted CDNs. Example:

```
Content-Security-Policy: default-src 'self'; img-src 'self' data: https:; script-src 'self' 'unsafe-inline' 'unsafe-eval' https://cdn.example.com; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com; connect-src 'self';
```

Notes:

- Avoid `unsafe-inline` and `unsafe-eval` where possible. If inline styles are required, use hashed nonces or move styles to external sheets.
- Adjust `script-src` to include third-party analytics only after approval.

## Vercel configuration

In `vercel.json` or Vercel dashboard, add headers config for static files. Example `vercel.json` snippet:

```json
{
  "headers": [
    {
      "source": "(.*)",
      "headers": [
        {
          "key": "Strict-Transport-Security",
          "value": "max-age=63072000; includeSubDomains; preload"
        },
        { "key": "X-Frame-Options", "value": "DENY" },
        { "key": "X-Content-Type-Options", "value": "nosniff" },
        { "key": "Referrer-Policy", "value": "no-referrer-when-downgrade" }
      ]
    }
  ]
}
```

## Verification

- Add a CI step to verify headers are present in production preview URLs (or run curl checks in a PR preview).
- Document any exceptions in `specs/001-i-am-building/security.md` and obtain maintainers' approval for additional external hosts.

## Implementation Status

Implemented in `frontend/next.config.js` via `headers()` export adding:

```
Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
X-Frame-Options: DENY
X-Content-Type-Options: nosniff
Referrer-Policy: no-referrer-when-downgrade
Permissions-Policy: geolocation=(), microphone=()
Content-Security-Policy: default-src 'self'; img-src 'self' data: https:; script-src 'self' 'unsafe-inline' 'unsafe-eval'; style-src 'self' 'unsafe-inline'; font-src 'self' data:; connect-src 'self'
```

Future tightening tasks:

- Remove `'unsafe-inline'` and `'unsafe-eval'` by refactoring inline styles/scripts.
- Add hashes/nonces for any remaining inline snippets.
- Introduce reporting with `report-to` / `report-uri` if needed.

## Curl Check Example (optional)

Run after deployment (replace URL):

```
curl -I https://example.vercel.app | findstr /R "Strict-Transport-Security\|Content-Security-Policy\|Permissions-Policy"
```

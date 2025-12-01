# Deployment Guide

This guide covers building, deploying, and hosting the Movie Review Website.

## Table of Contents

- [Build Process](#build-process)
- [Deployment Options](#deployment-options)
- [Static Export](#static-export)
- [Vercel Deployment](#vercel-deployment)
- [Netlify Deployment](#netlify-deployment)
- [GitHub Pages](#github-pages)
- [Docker Deployment](#docker-deployment)
- [Environment Configuration](#environment-configuration)
- [Performance Optimization](#performance-optimization)
- [Troubleshooting](#troubleshooting)

## Build Process

### Development Build

For local development with hot reloading:

```bash
cd frontend
npm run dev
```

This starts the development server on [http://localhost:3000](http://localhost:3000).

### Production Build

To create an optimized production build:

```bash
cd frontend
npm run build
```

This command:
1. Compiles TypeScript to JavaScript
2. Bundles and minifies code
3. Optimizes images and assets
4. Generates static pages
5. Creates build output in `.next/` directory

**Output**:
```
✓ Creating an optimized production build
✓ Compiled successfully
✓ Linting and checking validity of types
✓ Collecting page data
✓ Generating static pages (3/3)
✓ Finalizing page optimization

Route (pages)                Size     First Load JS
┌ ○ /                       1.2 kB          80 kB
├ ○ /404                    182 B          77.9 kB
├ ○ /movies/[id]            1.5 kB          82 kB
└ ○ /movies/inception       1.5 kB          82 kB

○  (Static)  automatically rendered as static HTML
```

### Start Production Server

To test the production build locally:

```bash
npm run start
```

This starts the production server on [http://localhost:3000](http://localhost:3000).

### Build Analysis

To analyze the build size:

```bash
# Install analyzer
npm install --save-dev @next/bundle-analyzer

# Add to next.config.js
const withBundleAnalyzer = require('@next/bundle-analyzer')({
  enabled: process.env.ANALYZE === 'true',
});

module.exports = withBundleAnalyzer(nextConfig);

# Run analysis
ANALYZE=true npm run build
```

## Deployment Options

The Movie Review Website is a **static Next.js application** that can be deployed to any static hosting service.

### Compatibility

✅ **Compatible with**:
- Vercel (recommended)
- Netlify
- GitHub Pages
- AWS S3 + CloudFront
- Azure Static Web Apps
- Google Cloud Storage
- Cloudflare Pages
- Any CDN or static host

❌ **Not required**:
- Node.js server
- Database
- Backend API
- Server-side functions

## Static Export

Next.js can export a fully static website that runs without a Node.js server.

### Enable Static Export

The application is already configured for static export in [next.config.js](../frontend/next.config.js):

```javascript
/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'export',  // Enable static export
  trailingSlash: true,
  images: {
    unoptimized: true,  // Required for static export
  },
};
```

### Generate Static Export

```bash
cd frontend
npm run build
```

This creates a static export in the `out/` directory with:
- HTML files for each page
- JavaScript bundles
- CSS files
- Static assets (images, fonts, etc.)

### Serve Static Export

You can serve the static export with any static file server:

```bash
# Using npx serve
npx serve out

# Using Python
python -m http.server 8000 -d out

# Using Node.js http-server
npm install -g http-server
http-server out -p 8000
```

## Vercel Deployment

[Vercel](https://vercel.com) is the recommended hosting platform (created by the Next.js team).

### Method 1: GitHub Integration (Recommended)

1. **Push code to GitHub**:
   ```bash
   git push origin main
   ```

2. **Import project**:
   - Go to [vercel.com/new](https://vercel.com/new)
   - Click "Import Git Repository"
   - Select your repository
   - Click "Import"

3. **Configure project**:
   - **Framework Preset**: Next.js
   - **Root Directory**: `frontend`
   - **Build Command**: `npm run build`
   - **Output Directory**: `.next` (or `out` for static export)
   - **Install Command**: `npm install`

4. **Deploy**:
   - Click "Deploy"
   - Wait for build to complete
   - Your site is live at `https://your-project.vercel.app`

### Method 2: Vercel CLI

```bash
# Install Vercel CLI
npm install -g vercel

# Login
vercel login

# Deploy from frontend directory
cd frontend
vercel

# Deploy to production
vercel --prod
```

### Configuration File

Create `vercel.json` in the frontend directory:

```json
{
  "buildCommand": "npm run build",
  "outputDirectory": ".next",
  "devCommand": "npm run dev",
  "installCommand": "npm install",
  "framework": "nextjs",
  "regions": ["iad1"]
}
```

### Custom Domain

1. Go to project settings in Vercel dashboard
2. Click "Domains"
3. Add your custom domain
4. Update DNS records as instructed
5. Wait for SSL certificate provisioning

## Netlify Deployment

### Method 1: GitHub Integration

1. **Push code to GitHub**:
   ```bash
   git push origin main
   ```

2. **Import project**:
   - Go to [app.netlify.com/start](https://app.netlify.com/start)
   - Click "Import from Git"
   - Select your repository

3. **Configure build settings**:
   - **Base directory**: `frontend`
   - **Build command**: `npm run build`
   - **Publish directory**: `out` (for static export)
   - **Node version**: `22`

4. **Deploy**:
   - Click "Deploy site"
   - Your site is live at `https://random-name.netlify.app`

### Method 2: Netlify CLI

```bash
# Install Netlify CLI
npm install -g netlify-cli

# Login
netlify login

# Initialize site
cd frontend
netlify init

# Deploy
netlify deploy

# Deploy to production
netlify deploy --prod
```

### Configuration File

Create `netlify.toml` in the frontend directory:

```toml
[build]
  base = "frontend"
  command = "npm run build"
  publish = "out"

[build.environment]
  NODE_VERSION = "22"

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200
```

## GitHub Pages

### Setup

1. **Enable GitHub Pages**:
   - Go to repository settings
   - Navigate to "Pages"
   - Source: Deploy from a branch
   - Branch: `gh-pages` / root

2. **Add deployment script** to `package.json`:
   ```json
   {
     "scripts": {
       "deploy": "next build && next export && touch out/.nojekyll && gh-pages -d out"
     }
   }
   ```

3. **Install gh-pages**:
   ```bash
   npm install --save-dev gh-pages
   ```

4. **Update next.config.js** for base path:
   ```javascript
   const nextConfig = {
     output: 'export',
     basePath: '/repo-name',  // Replace with your repo name
     assetPrefix: '/repo-name/',
   };
   ```

5. **Deploy**:
   ```bash
   cd frontend
   npm run deploy
   ```

### GitHub Actions Workflow

Create `.github/workflows/deploy.yml`:

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [main]

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '22'

      - name: Install dependencies
        working-directory: ./frontend
        run: npm ci

      - name: Build
        working-directory: ./frontend
        run: npm run build

      - name: Export
        working-directory: ./frontend
        run: npx next export

      - name: Deploy
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./frontend/out
```

## Docker Deployment

### Dockerfile

Create `Dockerfile` in the frontend directory:

```dockerfile
# Build stage
FROM node:22-alpine AS builder

WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm ci

# Copy source code
COPY . .

# Build application
RUN npm run build

# Production stage
FROM node:22-alpine AS runner

WORKDIR /app

# Copy built files
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/public ./public
COPY --from=builder /app/package*.json ./
COPY --from=builder /app/next.config.js ./

# Install production dependencies only
RUN npm ci --production

EXPOSE 3000

CMD ["npm", "start"]
```

### Build and Run

```bash
# Build image
docker build -t movie-review-app ./frontend

# Run container
docker run -p 3000:3000 movie-review-app
```

### Docker Compose

Create `docker-compose.yml`:

```yaml
version: '3.8'

services:
  app:
    build:
      context: ./frontend
      dockerfile: Dockerfile
    ports:
      - "3000:3000"
    restart: unless-stopped
```

Run with:
```bash
docker-compose up -d
```

## Environment Configuration

### Node.js Version

The application requires **Node.js 22+**. This is enforced by:

1. **`.nvmrc`** - Specifies Node version for nvm users
   ```
   22
   ```

2. **`package.json` engines** - Enforces minimum version
   ```json
   {
     "engines": {
       "node": ">=22.0.0",
       "npm": ">=10.0.0"
     }
   }
   ```

### Environment Variables

The application currently has no environment variables. If adding:

1. Create `.env.local` in frontend directory:
   ```
   NEXT_PUBLIC_API_URL=https://api.example.com
   ```

2. Access in code:
   ```typescript
   const apiUrl = process.env.NEXT_PUBLIC_API_URL;
   ```

3. Add to `.gitignore`:
   ```
   .env.local
   .env*.local
   ```

## Performance Optimization

### Image Optimization

For static export, images are not optimized by Next.js. Consider:

1. **Optimize before deployment**:
   ```bash
   npm install -g sharp-cli
   sharp -i input.jpg -o output.jpg -q 80
   ```

2. **Use a CDN** with automatic optimization (Cloudflare, Cloudinary, etc.)

3. **Serve WebP format** where supported

### Code Splitting

Next.js automatically code-splits by route. To further optimize:

```tsx
// Dynamic imports for large components
import dynamic from 'next/dynamic';

const HeavyComponent = dynamic(() => import('@/components/HeavyComponent'), {
  loading: () => <p>Loading...</p>,
});
```

### Caching Headers

Set cache headers in your hosting platform:

**Vercel** (`vercel.json`):
```json
{
  "headers": [
    {
      "source": "/(.*)",
      "headers": [
        {
          "key": "Cache-Control",
          "value": "public, max-age=31536000, immutable"
        }
      ]
    }
  ]
}
```

**Netlify** (`netlify.toml`):
```toml
[[headers]]
  for = "/*"
  [headers.values]
    Cache-Control = "public, max-age=31536000, immutable"
```

### Bundle Size Reduction

1. **Analyze bundle**:
   ```bash
   ANALYZE=true npm run build
   ```

2. **Remove unused dependencies**:
   ```bash
   npm uninstall unused-package
   ```

3. **Use dynamic imports** for non-critical code

## Troubleshooting

### Build Fails

**Issue**: Build fails with TypeScript errors

**Solution**:
```bash
# Check TypeScript errors
npm run type-check

# Fix errors or temporarily skip
# (not recommended for production)
```

---

**Issue**: Build fails with memory error

**Solution**:
```bash
# Increase Node memory
NODE_OPTIONS='--max-old-space-size=4096' npm run build
```

### Static Export Issues

**Issue**: Page shows 404 after refresh

**Solution**: Configure redirects/rewrites in your hosting platform to always serve `index.html`.

---

**Issue**: Images not loading in static export

**Solution**: Ensure `images.unoptimized: true` in `next.config.js`.

### Deployment Errors

**Issue**: Vercel build fails with "Module not found"

**Solution**: Ensure all dependencies are in `package.json`, not just `devDependencies`.

---

**Issue**: GitHub Pages shows blank page

**Solution**:
1. Check basePath in `next.config.js`
2. Verify `.nojekyll` file exists
3. Check browser console for 404 errors

### Performance Issues

**Issue**: Large bundle size

**Solution**:
1. Run bundle analyzer
2. Identify large dependencies
3. Use dynamic imports
4. Remove unused code

---

**Issue**: Slow page loads

**Solution**:
1. Enable CDN caching
2. Optimize images
3. Minimize JavaScript
4. Use code splitting

## Production Checklist

Before deploying to production:

- [ ] Run `npm test` - All tests passing
- [ ] Run `npm run lint` - No linting errors
- [ ] Run `npm run build` - Build succeeds
- [ ] Test production build locally with `npm run start`
- [ ] Check bundle size with `ANALYZE=true npm run build`
- [ ] Verify all images load correctly
- [ ] Test on multiple browsers (Chrome, Firefox, Safari, Edge)
- [ ] Test on mobile devices
- [ ] Run Lighthouse audit (Performance, Accessibility, Best Practices, SEO)
- [ ] Verify meta tags and social sharing previews
- [ ] Set up error monitoring (Sentry, etc.)
- [ ] Configure analytics (Google Analytics, Plausible, etc.)
- [ ] Set up custom domain and SSL
- [ ] Configure caching headers
- [ ] Add security headers (already configured in `next.config.js`)
- [ ] Test accessibility with screen readers
- [ ] Verify 404 page works correctly
- [ ] Set up CI/CD pipeline

## Monitoring and Analytics

### Error Monitoring

Integrate error tracking:

```bash
# Sentry
npm install @sentry/nextjs

# Initialize
npx @sentry/wizard -i nextjs
```

### Analytics

Add analytics to `_app.tsx`:

```tsx
import { useEffect } from 'react';
import { useRouter } from 'next/router';

export default function App({ Component, pageProps }) {
  const router = useRouter();

  useEffect(() => {
    const handleRouteChange = (url) => {
      // Track page view
      window.gtag('config', 'GA_MEASUREMENT_ID', {
        page_path: url,
      });
    };

    router.events.on('routeChangeComplete', handleRouteChange);
    return () => {
      router.events.off('routeChangeComplete', handleRouteChange);
    };
  }, [router.events]);

  return <Component {...pageProps} />;
}
```

## CI/CD Pipeline

### GitHub Actions Example

Create `.github/workflows/ci.yml`:

```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '22'

      - name: Install dependencies
        working-directory: ./frontend
        run: npm ci

      - name: Run linter
        working-directory: ./frontend
        run: npm run lint

      - name: Run tests
        working-directory: ./frontend
        run: npm test

      - name: Build
        working-directory: ./frontend
        run: npm run build
```

---

For more information, see:
- [Next.js Deployment Documentation](https://nextjs.org/docs/deployment)
- [Vercel Documentation](https://vercel.com/docs)
- [Netlify Documentation](https://docs.netlify.com/)

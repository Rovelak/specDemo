# Movie Review Website

A modern, specification-driven Next.js movie review website built with TypeScript, Tailwind CSS, and mock data. This project demonstrates fixture-based architecture, comprehensive testing, and specification-driven development using SpecKit.

## Table of Contents

- [Quick Start](#quick-start)
- [Project Overview](#project-overview)
- [Technology Stack](#technology-stack)
- [Architecture](#architecture)
- [Development](#development)
- [Testing](#testing)
- [Project Structure](#project-structure)
- [Documentation](#documentation)
- [Contributing](#contributing)

## Quick Start

### Prerequisites

- Node.js 22+ (locked via `.nvmrc`)
- npm 10+

### Installation

```bash
# Clone the repository
git clone <repository-url>
cd specDemo

# Install dependencies
cd frontend
npm install

# Start development server
npm run dev
```

Visit [http://localhost:3000](http://localhost:3000) to see the application.

## Project Overview

This is a **frontend-only movie review website** that showcases:

- **Static mock data architecture** - No backend or API required
- **Specification-driven development** - Built using SpecKit workflow
- **Type-safe data validation** - Runtime validation with TypeScript
- **Comprehensive testing** - Unit tests (Jest) and E2E tests (Playwright)
- **Modern React patterns** - Functional components, hooks, and composition
- **Accessible design** - WCAG compliance with semantic HTML and ARIA labels

### Key Features

- Browse movies on an interactive landing page
- View detailed movie information with cast and reviews
- Search and filter movies by title and year
- Responsive design with Tailwind CSS
- Static export compatible for CDN deployment

## Technology Stack

### Core Framework

- **Next.js 14.0.0** - React framework with Pages Router
- **React 18.2.0** - UI library
- **TypeScript 5.9.3** - Type safety and developer experience
- **Node.js 22+** - Runtime environment

### Styling

- **Tailwind CSS 3.4.8** - Utility-first CSS framework
- **shadcn/ui** - High-quality component library
- **PostCSS** - CSS transformation and optimization
- **lucide-react** - Icon library

### Testing

- **Jest 29.0.0** - Unit testing framework
- **@testing-library/react 14.0.0** - Component testing utilities
- **Playwright 1.56.1** - End-to-end testing
- **ts-jest** - TypeScript support for Jest

### Development Tools

- **ESLint 8.0.0** - Code linting
- **TypeScript Compiler** - Type checking
- **Autoprefixer** - CSS vendor prefixes

## Architecture

### Data Flow

The application follows a **fixture-based data architecture** with no external API:

```
fixtures/movies.json (source of truth)
        ↓
lib/fixtures.ts (loader + validator)
        ↓
types/models.ts (TypeScript types)
        ↓
React Components (UI rendering)
        ↓
Pages Router (Next.js routing)
```

### Type Definitions

#### Movie Type

```typescript
type Movie = {
  id: string; // Unique identifier
  title: string; // Movie title
  releaseYear: number; // Year of release
  posterUrl?: string; // Poster image URL (optional)
  synopsis?: string; // Plot summary (optional)
  cast?: string[]; // Array of actor names (optional)
  reviews?: Review[]; // Array of reviews (optional)
};
```

#### Review Type

```typescript
type Review = {
  id: string; // Unique identifier
  author: string; // Review author name
  rating: number; // Rating (0-10)
  text?: string; // Review text (optional)
};
```

### Data Validation

The application includes **runtime validation** to ensure data integrity:

- **Location**: [frontend/src/lib/fixtures.ts](frontend/src/lib/fixtures.ts)
- **Function**: `validateMoviesFixture()`
- **Validates**:
  - Required fields (id, title, releaseYear)
  - Year plausibility (1900 - current year + 2)
  - Review data integrity (author, text, rating 0-10)
  - Returns detailed validation errors

Validation runs automatically on app start and logs issues to the console.

### Page Routes

| Route          | Component                                                       | Description                             |
| -------------- | --------------------------------------------------------------- | --------------------------------------- |
| `/`            | [pages/index.tsx](frontend/src/pages/index.tsx)                 | Landing page with movie list and search |
| `/movies/[id]` | [pages/movies/[id].tsx](frontend/src/pages/movies/%5Bid%5D.tsx) | Dynamic movie detail page               |
| `_app.tsx`     | [pages/\_app.tsx](frontend/src/pages/_app.tsx)                  | App wrapper with global styles          |

### Component Architecture

**Layout Components**:

- [Layout.tsx](frontend/src/components/Layout.tsx) - App wrapper with header and footer
- [Header.tsx](frontend/src/components/Header.tsx) - Navigation header

**Feature Components**:

- [MovieCard.tsx](frontend/src/components/MovieCard.tsx) - Movie thumbnail with title and year
- [MovieDetail.tsx](frontend/src/components/MovieDetail.tsx) - Full movie details display
- [ReviewList.tsx](frontend/src/components/ReviewList.tsx) - Review display component
- [SearchBar.tsx](frontend/src/components/SearchBar.tsx) - Search and filter interface
- [EmptyState.tsx](frontend/src/components/EmptyState.tsx) - Empty state messaging

**UI Components** ([src/components/ui/](frontend/src/components/ui/)):

- shadcn/ui components (Button, etc.)

### Security

The application implements strict security headers in [next.config.js](frontend/next.config.js):

- **HSTS** - HTTP Strict Transport Security
- **X-Frame-Options** - Clickjacking protection
- **X-Content-Type-Options** - MIME sniffing protection
- **Referrer-Policy** - Referrer information control
- **Permissions-Policy** - Feature access restrictions
- **Content-Security-Policy** - XSS and injection protection

> **Note**: Current CSP allows `unsafe-inline` and `unsafe-eval` for scripts (temporary during development).

## Development

All development commands run from the `frontend/` directory:

```bash
cd frontend

# Development server (localhost:3000)
npm run dev

# Production build
npm run build

# Start production server
npm run start

# Run ESLint
npm run lint

# Format code
npm run format

# Type checking
npm run type-check
```

### Adding Movies

To add new movies to the application:

1. Edit [frontend/fixtures/movies.json](frontend/fixtures/movies.json)
2. Ensure data matches the `Movie` type in [types/models.ts](frontend/src/types/models.ts)
3. Run `npm run dev` and check console for validation errors
4. If adding new fields, update:
   - Type definitions in [types/models.ts](frontend/src/types/models.ts)
   - Validation logic in [lib/fixtures.ts](frontend/src/lib/fixtures.ts)
   - Relevant components that display the data

### Configuration Files

| File                                              | Purpose                      |
| ------------------------------------------------- | ---------------------------- |
| [next.config.js](frontend/next.config.js)         | Next.js and security headers |
| [tailwind.config.js](frontend/tailwind.config.js) | Tailwind CSS customization   |
| [tsconfig.json](frontend/tsconfig.json)           | TypeScript configuration     |
| [components.json](frontend/components.json)       | shadcn/ui configuration      |
| [.eslintrc.json](frontend/.eslintrc.json)         | ESLint rules                 |
| [postcss.config.cjs](frontend/postcss.config.cjs) | PostCSS plugins              |
| [.nvmrc](frontend/.nvmrc)                         | Node version lock (22+)      |

## Testing

### Unit Tests (Jest)

**Framework**: Jest + @testing-library/react

**Location**: [frontend/src/tests/](frontend/src/tests/)

**Test Files**:

- [fixturesValidation.test.ts](frontend/src/tests/fixturesValidation.test.ts) - Data validation tests
- [MovieCard.test.tsx](frontend/src/tests/MovieCard.test.tsx) - MovieCard component tests
- [MovieDetail.test.tsx](frontend/src/tests/MovieDetail.test.tsx) - MovieDetail component tests
- [SearchBar.test.tsx](frontend/src/tests/SearchBar.test.tsx) - Search functionality tests

**Commands**:

```bash
# Run all tests
npm test

# Run specific test file
npm test -- fixturesValidation.test.ts

# Run tests in watch mode
npm test -- --watch

# Generate coverage report
npm test -- --coverage
```

### E2E Tests (Playwright)

**Framework**: Playwright

**Location**: [frontend/tests/e2e/](frontend/tests/e2e/)

**Test Files**:

- [landing.spec.ts](frontend/tests/e2e/landing.spec.ts) - Landing page tests
- [movie-detail.spec.ts](frontend/tests/e2e/movie-detail.spec.ts) - Movie detail page tests
- [inception-navigation.spec.ts](frontend/tests/e2e/inception-navigation.spec.ts) - Navigation flow tests

**Commands**:

```bash
# Run all E2E tests (auto-starts dev server)
npm run test:e2e

# Run specific test file
npx playwright test tests/e2e/landing.spec.ts

# Run tests in headed mode (see browser)
npx playwright test --headed

# Run tests by name pattern
npx playwright test -g "test name pattern"

# Generate test report
npx playwright show-report
```

**Configuration**: [playwright.config.ts](frontend/playwright.config.ts)

- Auto-starts dev server on port 3000
- Retries failed tests once
- Generates traces on first retry

## Project Structure

```
specDemo/
├── .claude/                    # Claude Code configuration
│   ├── agents/                # Specialized AI agents
│   ├── commands/              # Custom slash commands
│   ├── hooks/                 # Git hooks
│   └── skills/                # Development skills
├── .github/                   # GitHub configuration
│   ├── copilot-instructions.md
│   ├── workflows/             # CI/CD workflows
│   └── prompts/               # Development prompts
├── .specify/                  # SpecKit template system
├── frontend/                  # Next.js application
│   ├── fixtures/              # Mock data
│   │   └── movies.json       # Movie dataset
│   ├── src/
│   │   ├── components/       # React components
│   │   │   ├── ui/          # shadcn/ui components
│   │   │   ├── Layout.tsx
│   │   │   ├── Header.tsx
│   │   │   ├── MovieCard.tsx
│   │   │   ├── MovieDetail.tsx
│   │   │   ├── ReviewList.tsx
│   │   │   ├── SearchBar.tsx
│   │   │   └── EmptyState.tsx
│   │   ├── lib/              # Utilities
│   │   │   ├── fixtures.ts   # Data loader & validator
│   │   │   └── utils.ts      # Tailwind utilities
│   │   ├── pages/            # Next.js pages
│   │   │   ├── index.tsx     # Landing page
│   │   │   ├── _app.tsx      # App wrapper
│   │   │   └── movies/
│   │   │       └── [id].tsx  # Movie detail page
│   │   ├── styles/           # Global styles
│   │   │   └── globals.css
│   │   ├── tests/            # Unit tests
│   │   └── types/            # TypeScript types
│   │       └── models.ts
│   ├── tests/
│   │   └── e2e/             # E2E tests
│   ├── next.config.js       # Next.js config
│   ├── jest.config.js       # Jest config
│   ├── playwright.config.ts # Playwright config
│   ├── tailwind.config.js   # Tailwind config
│   └── package.json         # Dependencies
├── specs/                   # Feature specifications
│   └── 001-i-am-building/  # Active feature
│       ├── spec.md         # Core specification
│       ├── plan.md         # Implementation plan
│       ├── tasks.md        # Task breakdown
│       ├── test-plan.md    # Testing strategy
│       ├── security.md     # Security considerations
│       └── a11y-report.md  # Accessibility report
├── CLAUDE.md               # Claude Code guidance
└── README.md               # This file
```

## Documentation

### Core Documentation

- [README.md](README.md) - This file (project overview)
- [CLAUDE.md](CLAUDE.md) - Claude Code guidance and constraints
- [frontend/README.md](frontend/README.md) - Frontend quickstart

### Specification Documents

Located in [specs/001-i-am-building/](specs/001-i-am-building/):

| Document                                                 | Purpose                                         |
| -------------------------------------------------------- | ----------------------------------------------- |
| [spec.md](specs/001-i-am-building/spec.md)               | User stories, requirements, acceptance criteria |
| [plan.md](specs/001-i-am-building/plan.md)               | Implementation plan and phases                  |
| [tasks.md](specs/001-i-am-building/tasks.md)             | Task breakdown and checklist                    |
| [test-plan.md](specs/001-i-am-building/test-plan.md)     | Testing strategy and scenarios                  |
| [security.md](specs/001-i-am-building/security.md)       | Security considerations                         |
| [a11y-report.md](specs/001-i-am-building/a11y-report.md) | Accessibility assessment                        |
| [data-model.md](specs/001-i-am-building/data-model.md)   | Data structure details                          |
| [quickstart.md](specs/001-i-am-building/quickstart.md)   | Getting started guide                           |

### Additional Documentation

- [.github/copilot-instructions.md](.github/copilot-instructions.md) - AI-assisted development guidelines
- Component-level documentation in source files

## Contributing

This project uses **SpecKit** for specification-driven development:

### Development Workflow

1. **Review specifications** in `specs/001-i-am-building/spec.md`
2. **Check implementation plan** in `specs/001-i-am-building/plan.md`
3. **Follow task breakdown** in `specs/001-i-am-building/tasks.md`
4. **Write tests first** following `specs/001-i-am-building/test-plan.md`
5. **Implement features** following project conventions
6. **Run all tests** before committing
7. **Update documentation** as needed

### Code Standards

- **TypeScript**: Strict mode enabled
- **Linting**: ESLint with Next.js rules
- **Formatting**: Prettier (configure via `.prettierrc`)
- **Testing**: Minimum 80% code coverage (unit tests)
- **Accessibility**: WCAG 2.1 AA compliance
- **Security**: Follow OWASP top 10 guidelines

### Git Workflow

```bash
# Create feature branch
git checkout -b feature/your-feature-name

# Make changes and test
npm test
npm run test:e2e
npm run lint

# Commit with conventional commits
git commit -m "feat: add new feature"

# Push and create PR
git push origin feature/your-feature-name
```

### Important Constraints

1. **No backend** - All data comes from `fixtures/movies.json`
2. **Node.js 22+** - Locked via `.nvmrc` and `package.json`
3. **Static export compatibility** - No server-side runtime dependencies
4. **Fixture validation** - Update both types and validation when modifying data structure

## License

[Add your license here]

## Support

For issues and questions:

- Create an issue in the repository
- Check [CLAUDE.md](CLAUDE.md) for Claude Code guidance
- Review specification documents in `specs/`

---

Built with ❤️ using Next.js, TypeScript, and SpecKit

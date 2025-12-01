# Contributing to Movie Review Website

Thank you for your interest in contributing to the Movie Review Website! This document provides guidelines and instructions for contributing to the project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [SpecKit Workflow](#speckit-workflow)
- [Coding Standards](#coding-standards)
- [Testing Guidelines](#testing-guidelines)
- [Commit Guidelines](#commit-guidelines)
- [Pull Request Process](#pull-request-process)
- [Project Structure](#project-structure)
- [Documentation](#documentation)
- [Getting Help](#getting-help)

## Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inclusive experience for everyone. We expect all contributors to:

- Use welcoming and inclusive language
- Be respectful of differing viewpoints and experiences
- Gracefully accept constructive criticism
- Focus on what is best for the community
- Show empathy towards other community members

### Unacceptable Behavior

- Harassment, discrimination, or offensive comments
- Trolling, insulting/derogatory comments, and personal attacks
- Public or private harassment
- Publishing others' private information without permission
- Other conduct which could reasonably be considered inappropriate

## Getting Started

### Prerequisites

Before contributing, ensure you have:

- **Node.js 22+** installed ([nvm](https://github.com/nvm-sh/nvm) recommended)
- **npm 10+** package manager
- **Git** version control
- A code editor (VS Code recommended)

### Fork and Clone

1. **Fork the repository** on GitHub
2. **Clone your fork**:
   ```bash
   git clone https://github.com/YOUR-USERNAME/specDemo.git
   cd specDemo
   ```
3. **Add upstream remote**:
   ```bash
   git remote add upstream https://github.com/ORIGINAL-OWNER/specDemo.git
   ```

### Installation

```bash
cd frontend
npm install
```

### Run Development Server

```bash
npm run dev
```

Visit [http://localhost:3000](http://localhost:3000) to see the application.

## Development Workflow

### 1. Create a Feature Branch

Always create a new branch for your work:

```bash
# Sync with upstream
git checkout main
git pull upstream main

# Create feature branch
git checkout -b feature/your-feature-name
```

**Branch naming conventions**:
- `feature/` - New features (e.g., `feature/add-rating-filter`)
- `fix/` - Bug fixes (e.g., `fix/search-case-sensitivity`)
- `docs/` - Documentation updates (e.g., `docs/update-readme`)
- `refactor/` - Code refactoring (e.g., `refactor/extract-search-hook`)
- `test/` - Test additions/updates (e.g., `test/add-review-list-tests`)
- `chore/` - Maintenance tasks (e.g., `chore/update-dependencies`)

### 2. Make Your Changes

- **Write clean code** following project standards
- **Add tests** for new functionality
- **Update documentation** if needed
- **Follow TypeScript** best practices
- **Ensure accessibility** (WCAG 2.1 AA)

### 3. Test Your Changes

```bash
# Run all tests
npm test

# Run specific test
npm test -- MovieCard.test.tsx

# Run linter
npm run lint

# Type checking
npm run type-check

# E2E tests
npm run test:e2e
```

### 4. Commit Your Changes

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```bash
git add .
git commit -m "feat: add movie rating filter"
```

See [Commit Guidelines](#commit-guidelines) for details.

### 5. Push and Create Pull Request

```bash
# Push to your fork
git push origin feature/your-feature-name
```

Then create a Pull Request on GitHub. See [Pull Request Process](#pull-request-process).

## SpecKit Workflow

This project uses **SpecKit** for specification-driven development.

### Understanding SpecKit

SpecKit is a workflow that emphasizes:
1. **Specification first** - Define requirements before coding
2. **Plan-driven development** - Create implementation plans
3. **Task breakdown** - Break work into actionable tasks
4. **Test planning** - Define test scenarios upfront

### Specification Documents

All feature specifications are in [specs/](specs/):

```
specs/
└── 001-i-am-building/
    ├── spec.md          # Core feature specification
    ├── plan.md          # Implementation plan
    ├── tasks.md         # Task breakdown
    ├── test-plan.md     # Testing strategy
    ├── security.md      # Security considerations
    └── a11y-report.md   # Accessibility report
```

### SpecKit Development Process

When adding a new feature:

1. **Create specification** (`spec.md`):
   - User stories
   - Functional requirements
   - Success criteria
   - Edge cases

2. **Create implementation plan** (`plan.md`):
   - Technical approach
   - Component structure
   - Data flow
   - Dependencies

3. **Break down tasks** (`tasks.md`):
   - Actionable checklist
   - Dependencies between tasks
   - Priority order

4. **Define test plan** (`test-plan.md`):
   - Unit test scenarios
   - E2E test scenarios
   - Accessibility tests

5. **Implement** following the plan

6. **Test** according to test plan

7. **Review** against specification

### SpecKit Slash Commands

The project includes custom slash commands in [.claude/commands/](.claude/commands/):

- `/speckit.specify` - Create feature specification
- `/speckit.plan` - Create implementation plan
- `/speckit.tasks` - Generate task breakdown
- `/speckit.implement` - Execute implementation
- `/speckit.checklist` - Generate custom checklist

Use these commands with Claude Code or refer to them for guidance.

## Coding Standards

### TypeScript

- **Use strict mode** - Already enabled in `tsconfig.json`
- **Type everything** - No `any` types unless absolutely necessary
- **Prefer interfaces** for object shapes
- **Use type inference** where obvious

#### Good Examples

```typescript
// Good: Explicit interface
interface Movie {
  id: string;
  title: string;
  releaseYear: number;
}

// Good: Type inference
const movies = loadMovies(); // Type inferred as Movie[]

// Good: Type guard
function isMovie(obj: unknown): obj is Movie {
  return typeof obj === 'object' && obj !== null && 'id' in obj;
}
```

#### Bad Examples

```typescript
// Bad: Using 'any'
function processData(data: any) { }

// Bad: No type annotation when not obvious
function transform(input) { return input.map(x => x * 2); }

// Bad: Unnecessary explicit type
const title: string = movie.title; // Type is already known
```

### React

- **Functional components** only (no class components)
- **Use hooks** for state and effects
- **Destructure props** in function signature
- **Use TypeScript props** interface

#### Component Template

```typescript
import React from 'react';

type Props = {
  required: string;
  optional?: number;
};

export default function MyComponent({ required, optional = 0 }: Props) {
  // Component logic
  return (
    <div>
      {/* JSX */}
    </div>
  );
}
```

### Styling

- **Use Tailwind CSS** utility classes
- **Follow shadcn/ui** patterns for components
- **Mobile-first** responsive design
- **Use semantic class names** for custom CSS

```tsx
// Good: Tailwind utilities
<div className="flex items-center gap-4 p-4 rounded-lg bg-white shadow-md">

// Good: Responsive
<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3">

// Good: Semantic custom class
<article className="movie-card">
```

### Accessibility

All components must be accessible (WCAG 2.1 AA):

- ✅ Use semantic HTML (`<article>`, `<section>`, `<nav>`)
- ✅ Provide ARIA labels where needed
- ✅ Ensure keyboard navigation works
- ✅ Add alt text to images
- ✅ Maintain heading hierarchy
- ✅ Test with screen readers

```tsx
// Good: Semantic HTML + ARIA
<article className="movie-card">
  <Link
    href={`/movies/${movie.id}`}
    aria-label={`View details for ${movie.title}`}
  >
    <img src={posterUrl} alt={`${movie.title} poster`} />
  </Link>
</article>

// Good: Screen reader label
<label htmlFor="search" className="visually-hidden">
  Search movies
</label>
<input id="search" type="text" />
```

### File Organization

- **One component per file** - `ComponentName.tsx`
- **Colocate tests** - `ComponentName.test.tsx` in `src/tests/`
- **Group related files** - Keep related components together
- **Use index files** - For cleaner imports

```
components/
├── Layout.tsx
├── Header.tsx
├── MovieCard.tsx
└── ui/
    ├── Button.tsx
    └── index.ts
```

### Naming Conventions

| Type | Convention | Example |
|------|------------|---------|
| Components | PascalCase | `MovieCard.tsx` |
| Functions | camelCase | `loadMovies()` |
| Hooks | camelCase with `use` prefix | `useMovieSearch()` |
| Constants | UPPER_SNAKE_CASE | `MAX_RESULTS` |
| Types/Interfaces | PascalCase | `Movie`, `MovieProps` |
| Files | kebab-case or PascalCase | `movie-card.tsx` or `MovieCard.tsx` |

## Testing Guidelines

### Unit Tests

Write unit tests for:
- Components (rendering, props, events)
- Utility functions
- Data validation
- Hooks

#### Test Structure

```typescript
import { render, screen, fireEvent } from '@testing-library/react';
import MyComponent from '@/components/MyComponent';

describe('MyComponent', () => {
  it('renders correctly', () => {
    render(<MyComponent title="Test" />);
    expect(screen.getByText('Test')).toBeInTheDocument();
  });

  it('handles click events', () => {
    const handleClick = jest.fn();
    render(<MyComponent onClick={handleClick} />);

    fireEvent.click(screen.getByRole('button'));
    expect(handleClick).toHaveBeenCalledTimes(1);
  });

  it('handles missing optional props', () => {
    render(<MyComponent />);
    // Component should render without errors
  });
});
```

#### Testing Best Practices

- ✅ Test user behavior, not implementation
- ✅ Use `screen` queries from Testing Library
- ✅ Test edge cases (empty data, missing props, errors)
- ✅ Use descriptive test names
- ✅ Keep tests focused (one assertion per test when possible)
- ❌ Don't test implementation details
- ❌ Don't test third-party libraries

### E2E Tests

Write E2E tests for:
- Critical user flows
- Navigation between pages
- Search and filter functionality
- Error states

#### E2E Test Structure

```typescript
import { test, expect } from '@playwright/test';

test.describe('Movie browsing', () => {
  test('should display movie list on homepage', async ({ page }) => {
    await page.goto('/');

    // Check for movie cards
    const movieCards = page.locator('.movie-card');
    await expect(movieCards).toHaveCount(2);
  });

  test('should navigate to movie detail page', async ({ page }) => {
    await page.goto('/');

    // Click first movie
    await page.click('text=Inception');

    // Verify navigation
    await expect(page).toHaveURL(/.*movies\/inception/);
    await expect(page.locator('h1')).toContainText('Inception');
  });
});
```

### Test Coverage

Aim for:
- **80%+ overall coverage**
- **90%+ for critical paths**
- **100% for utility functions**

Check coverage:
```bash
npm test -- --coverage
```

## Commit Guidelines

### Conventional Commits

Follow [Conventional Commits](https://www.conventionalcommits.org/) specification:

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

### Commit Types

| Type | Description | Example |
|------|-------------|---------|
| `feat` | New feature | `feat: add movie rating filter` |
| `fix` | Bug fix | `fix: resolve search case sensitivity` |
| `docs` | Documentation | `docs: update API documentation` |
| `style` | Formatting, missing semi-colons | `style: format with prettier` |
| `refactor` | Code refactoring | `refactor: extract search hook` |
| `test` | Add/update tests | `test: add MovieCard tests` |
| `chore` | Maintenance | `chore: update dependencies` |
| `perf` | Performance improvement | `perf: optimize image loading` |

### Commit Message Examples

**Good commits**:
```bash
feat: add search functionality to movie list
fix: correct poster image loading on detail page
docs: add component documentation for MovieCard
refactor: extract movie filtering logic to custom hook
test: add unit tests for ReviewList component
```

**Bad commits**:
```bash
update stuff
fix bug
WIP
changes
more changes
```

### Commit Message Rules

- ✅ Use imperative mood ("add", not "added" or "adds")
- ✅ Start with lowercase
- ✅ No period at the end
- ✅ Keep first line under 72 characters
- ✅ Provide context in body if needed
- ❌ Don't use vague messages like "fix bug"
- ❌ Don't commit commented-out code
- ❌ Don't mix unrelated changes

## Pull Request Process

### Before Creating a PR

1. ✅ All tests pass (`npm test` and `npm run test:e2e`)
2. ✅ Linter passes (`npm run lint`)
3. ✅ Types check (`npm run type-check`)
4. ✅ Code follows project standards
5. ✅ Documentation updated if needed
6. ✅ Commits follow conventional format
7. ✅ Branch is up-to-date with main

### Creating a Pull Request

1. **Push your branch**:
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Create PR on GitHub**:
   - Click "Compare & pull request"
   - Fill out the PR template
   - Add descriptive title
   - Link related issues

3. **PR Title Format**:
   ```
   feat: Add movie rating filter (#123)
   fix: Resolve search case sensitivity (#124)
   ```

### Pull Request Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Related Issues
Closes #123

## Changes Made
- Added search functionality
- Updated MovieCard component
- Added unit tests

## Testing
- [ ] Unit tests added/updated
- [ ] E2E tests added/updated
- [ ] Manual testing completed

## Screenshots (if applicable)
[Add screenshots for UI changes]

## Checklist
- [ ] Code follows project standards
- [ ] Tests pass locally
- [ ] Documentation updated
- [ ] No console errors/warnings
- [ ] Accessibility verified
```

### PR Review Process

1. **Automated checks** run (tests, linting, type checking)
2. **Reviewer assigned** by maintainers
3. **Review feedback** addressed
4. **Approval** from at least one maintainer
5. **Merge** to main branch

### Addressing Review Feedback

```bash
# Make requested changes
git add .
git commit -m "refactor: address PR feedback"

# Push updates
git push origin feature/your-feature-name
```

Don't force push unless absolutely necessary (preserves review history).

## Project Structure

### Directory Overview

```
specDemo/
├── .claude/           # Claude Code configuration
├── .github/           # GitHub workflows and templates
├── docs/              # Documentation
├── frontend/          # Next.js application
│   ├── fixtures/      # Mock data
│   ├── src/
│   │   ├── components/  # React components
│   │   ├── lib/         # Utilities
│   │   ├── pages/       # Next.js pages
│   │   ├── styles/      # Global styles
│   │   ├── tests/       # Unit tests
│   │   └── types/       # TypeScript types
│   ├── tests/e2e/     # E2E tests
│   └── [config files] # Various configs
└── specs/             # SpecKit specifications
```

### Adding New Files

**Component**:
```
src/components/NewComponent.tsx
src/tests/NewComponent.test.tsx
```

**Page**:
```
src/pages/new-page.tsx
tests/e2e/new-page.spec.ts
```

**Utility**:
```
src/lib/new-util.ts
src/tests/new-util.test.ts
```

## Documentation

### When to Update Docs

Update documentation when:
- Adding new features
- Changing existing behavior
- Adding new dependencies
- Modifying configuration
- Changing API contracts
- Adding new components

### Documentation Files

| File | Purpose |
|------|---------|
| [README.md](README.md) | Project overview |
| [CONTRIBUTING.md](CONTRIBUTING.md) | This file |
| [docs/API.md](docs/API.md) | Data models and fixtures |
| [docs/COMPONENTS.md](docs/COMPONENTS.md) | Component documentation |
| [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md) | Deployment guide |
| [CLAUDE.md](CLAUDE.md) | Claude Code guidance |

### Writing Documentation

- ✅ Use clear, concise language
- ✅ Provide code examples
- ✅ Include both what and why
- ✅ Keep up-to-date with code
- ✅ Use proper Markdown formatting
- ❌ Don't assume prior knowledge
- ❌ Don't leave placeholders like "TODO"

## Getting Help

### Resources

- **README** - [README.md](README.md)
- **Claude Code Docs** - [CLAUDE.md](CLAUDE.md)
- **Specifications** - [specs/](specs/)
- **GitHub Issues** - Report bugs or request features

### Asking Questions

When asking for help:

1. **Search existing issues** first
2. **Provide context**:
   - What you're trying to do
   - What you've tried
   - Error messages (full stack trace)
   - Environment (OS, Node version)
3. **Include code snippets** (formatted)
4. **Be specific** and concise

### Reporting Bugs

Create a GitHub issue with:

- **Clear title** - Describe the bug
- **Steps to reproduce** - How to trigger the bug
- **Expected behavior** - What should happen
- **Actual behavior** - What actually happens
- **Environment** - OS, Node version, browser
- **Screenshots** - If applicable
- **Additional context** - Anything else relevant

### Feature Requests

Create a GitHub issue with:

- **Clear title** - Describe the feature
- **Problem statement** - What problem does it solve?
- **Proposed solution** - How should it work?
- **Alternatives considered** - Other approaches
- **Additional context** - Use cases, examples

## License

By contributing, you agree that your contributions will be licensed under the same license as the project.

---

Thank you for contributing to the Movie Review Website! 🎬

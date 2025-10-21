import { test, expect } from "@playwright/test";

test.describe("Movie detail navigation", () => {
  test("navigates from landing to Inception detail and verifies content", async ({
    page,
  }) => {
    await page.goto("/");

    // Landing assertions
    await expect(
      page.getByRole("heading", { name: /movie reviews/i })
    ).toBeVisible();
    const inceptionLink = page.getByRole("link", {
      name: /view details for inception/i,
    });
    await expect(inceptionLink).toBeVisible();

    // Navigate to detail
    await inceptionLink.click();
    await expect(page).toHaveURL(/\/movies\/inception$/);

    // Detail assertions
    await expect(
      page.getByRole("heading", { name: /inception/i })
    ).toBeVisible();
    await expect(
      page.getByRole("heading", { name: /synopsis/i })
    ).toBeVisible();
    await expect(page.getByRole("heading", { name: /cast/i })).toBeVisible();
    // Disambiguate 'Reviews' heading (avoid matching site title 'Movie Reviews')
    const reviewsHeading = page.locator("h2", { hasText: /^Reviews$/ });
    await expect(reviewsHeading).toBeVisible();

    // Check at least one review
    const reviewAuthor = page.getByText(/Alice/i);
    await expect(reviewAuthor).toBeVisible();
  });
});

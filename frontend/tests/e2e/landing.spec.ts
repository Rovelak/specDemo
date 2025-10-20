import { test, expect } from "@playwright/test";

test.describe("Landing and Movie Detail", () => {
  test("landing lists movies and navigates to detail", async ({ page }) => {
    await page.goto("/");
    await expect(
      page.getByRole("heading", { name: /movie reviews/i })
    ).toBeVisible();
    const card = page.locator(".movie-card").first();
    await expect(card).toBeVisible();
    // Click first card link
    await card.click();
    // Detail page should show h1 movie title
    const title = page.locator("h1");
    await expect(title).toBeVisible();
  });
});

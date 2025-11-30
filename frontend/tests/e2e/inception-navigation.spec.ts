import { test, expect } from "@playwright/test";

test.describe("Inception Movie Navigation", () => {
  test("should navigate to Inception detail page and verify all content", async ({
    page,
  }) => {
    // Navigate to the main page
    await page.goto("/");

    // Verify we're on the landing page
    await expect(page).toHaveURL("http://localhost:3000/");
    await expect(page).toHaveTitle("Movie Reviews");

    // Verify the main heading is visible
    await expect(
      page.getByRole("heading", { name: "Movie Reviews" })
    ).toBeVisible();

    // Verify the search functionality is present
    await expect(
      page.getByRole("textbox", { name: "Search movies" })
    ).toBeVisible();
    await expect(page.getByRole("button", { name: "Search" })).toBeVisible();

    // Verify the "Add movie" button is present
    await expect(page.getByRole("button", { name: "Add movie" })).toBeVisible();

    // Find and verify the Inception movie card
    const inceptionLink = page.getByRole("link", {
      name: "View details for Inception",
    });
    await expect(inceptionLink).toBeVisible();

    // Verify the Inception movie card shows the year
    await expect(page.getByText("Inception")).toBeVisible();
    await expect(page.getByText("2010")).toBeVisible();

    // Click on the Inception movie
    await inceptionLink.click();

    // Verify navigation to the detail page
    await expect(page).toHaveURL("http://localhost:3000/movies/inception");
    await expect(page).toHaveTitle("Inception");

    // Verify the movie poster is displayed
    await expect(page.getByAltText("Inception poster")).toBeVisible();

    // Verify the main movie heading
    await expect(
      page.getByRole("heading", { name: "Inception", level: 1 })
    ).toBeVisible();

    // Verify the release year
    await expect(page.getByText("2010")).toBeVisible();

    // Verify the Synopsis section
    await expect(
      page.getByRole("heading", { name: "Synopsis", level: 2 })
    ).toBeVisible();
    await expect(
      page.getByText(
        /A thief who steals corporate secrets through the use of dream-sharing technology/
      )
    ).toBeVisible();

    // Verify the Cast section
    await expect(
      page.getByRole("heading", { name: "Cast", level: 3 })
    ).toBeVisible();
    await expect(page.getByText("Leonardo DiCaprio")).toBeVisible();
    await expect(page.getByText("Joseph Gordon-Levitt")).toBeVisible();

    // Verify the Reviews section
    await expect(
      page.getByRole("heading", { name: "Reviews", level: 2 })
    ).toBeVisible();

    // Verify Alice's review
    await expect(page.getByText("Alice")).toBeVisible();
    await expect(page.getByText("Rating: 5")).toBeVisible();
    await expect(page.getByText("Brilliant.")).toBeVisible();

    // Verify the footer is still present
    await expect(page.getByText("© 2025 Movie Reviews")).toBeVisible();
  });

  test("should verify page structure and accessibility", async ({ page }) => {
    // Navigate directly to Inception detail page
    await page.goto("/movies/inception");

    // Verify page structure for accessibility
    const mainContent = page.getByRole("main");
    await expect(mainContent).toBeVisible();

    // Verify proper heading hierarchy
    const h1 = page.getByRole("heading", { level: 1 });
    await expect(h1).toBeVisible();
    await expect(h1).toHaveText("Inception");

    const h2Headings = page.getByRole("heading", { level: 2 });
    await expect(h2Headings).toHaveCount(2); // Synopsis and Reviews

    const h3Headings = page.getByRole("heading", { level: 3 });
    await expect(h3Headings).toHaveCount(1); // Cast

    // Verify image has alt text
    const poster = page.getByRole("img", { name: "Inception poster" });
    await expect(poster).toBeVisible();

    // Verify list structure for cast and reviews
    const lists = page.getByRole("list");
    await expect(lists).toHaveCount(2); // Cast list and Reviews list
  });
});

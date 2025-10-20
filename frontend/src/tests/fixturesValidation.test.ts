import { validateMoviesFixture, movies } from "../lib/fixtures";

describe("fixtures validation", () => {
  it("should validate movies fixture with no issues", () => {
    const result = validateMoviesFixture(movies);
    expect(result.valid).toBe(true);
    expect(result.issues).toHaveLength(0);
  });
});

import React from "react";
import "@testing-library/jest-dom";
import { render, screen } from "@testing-library/react";
import MovieDetail from "../components/MovieDetail";

const movie = {
  id: "x",
  title: "Test Movie",
  releaseYear: 2021,
  synopsis: "A short synopsis.",
  cast: ["A", "B"],
  reviews: [{ id: "r1", author: "Alice", rating: 4, text: "Nice" }],
};

test("renders movie detail fields", () => {
  render(<MovieDetail movie={movie as any} />);
  expect(
    screen.getByRole("heading", { name: "Test Movie" })
  ).toBeInTheDocument();
  expect(screen.getByText("2021")).toBeInTheDocument();
  expect(screen.getByText("A")).toBeInTheDocument();
  expect(screen.getByText("Nice")).toBeInTheDocument();
});

import React from "react";
import { render, screen } from "@testing-library/react";
import MovieCard from "../components/MovieCard.jsx";

const movie = { id: "x", title: "Test", releaseYear: 2020 };

test("renders movie title and year", () => {
  render(<MovieCard movie={movie as any} />);
  expect(screen.getByText("Test")).toBeInTheDocument();
  expect(screen.getByText("2020")).toBeInTheDocument();
});

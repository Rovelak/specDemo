import React from "react";
import "@testing-library/jest-dom";
import { render, screen, fireEvent } from "@testing-library/react";
import SearchBar from "../components/SearchBar";

test("calls onSearch as user types", () => {
  const queries: string[] = [];
  render(<SearchBar onSearch={(q) => queries.push(q)} />);
  const input = screen.getByRole("textbox", { name: /search movies/i });
  fireEvent.change(input, { target: { value: "Inception" } });
  expect(queries[queries.length - 1]).toBe("Inception");
});

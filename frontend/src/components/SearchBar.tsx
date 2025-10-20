import React, { useState } from "react";

type Props = {
  onSearch: (query: string) => void;
  placeholder?: string;
};

export default function SearchBar({
  onSearch,
  placeholder = "Search movies...",
}: Props) {
  const [value, setValue] = useState("");

  return (
    <form
      role="search"
      aria-label="Movie search"
      onSubmit={(e) => {
        e.preventDefault();
        onSearch(value.trim());
      }}
      className="search-bar"
    >
      <label htmlFor="movie-search" className="visually-hidden">
        Search movies
      </label>
      <input
        id="movie-search"
        name="q"
        type="text"
        value={value}
        placeholder={placeholder}
        onChange={(e) => {
          const v = e.target.value;
          setValue(v);
          onSearch(v.trim());
        }}
      />
      <button type="submit">Search</button>
    </form>
  );
}

import React, { useState } from "react";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { Search } from "lucide-react";

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
      className="flex gap-2 w-full max-w-md"
    >
      <label htmlFor="movie-search" className="sr-only">
        Search movies
      </label>
      <div className="relative flex-1">
        <Search className="absolute left-3 top-1/2 -translate-y-1/2 h-4 w-4 text-muted-foreground" aria-hidden="true" />
        <Input
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
          className="pl-9"
        />
      </div>
      <Button type="submit">
        <Search className="h-4 w-4 mr-2" aria-hidden="true" />
        Search
      </Button>
    </form>
  );
}

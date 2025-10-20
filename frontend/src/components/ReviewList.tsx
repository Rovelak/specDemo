import React from "react";
import type { Review } from "../types/models";

type Props = {
  reviews?: Review[];
};

export default function ReviewList({ reviews }: Props) {
  if (!reviews || reviews.length === 0) {
    return <div>No reviews yet.</div>;
  }

  return (
    <ul className="review-list">
      {reviews.map((r) => (
        <li key={r.id} className="review-item">
          <strong>{r.author}</strong> — <span>Rating: {r.rating}</span>
          {r.text && <p>{r.text}</p>}
        </li>
      ))}
    </ul>
  );
}

import React from "react";

export default function EmptyState({
  message = "No movies available.",
}: {
  message?: string;
}) {
  return <div className="empty-state">{message}</div>;
}

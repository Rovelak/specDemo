import React from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Star } from "lucide-react";
import type { Review } from "../types/models";

type Props = {
  reviews?: Review[];
};

export default function ReviewList({ reviews }: Props) {
  if (!reviews || reviews.length === 0) {
    return (
      <p className="text-muted-foreground italic">
        No reviews yet.
      </p>
    );
  }

  return (
    <div className="space-y-4">
      {reviews.map((r) => (
        <Card key={r.id}>
          <CardContent className="pt-6">
            <div className="flex items-start justify-between gap-4 mb-2">
              <p className="font-semibold">{r.author}</p>
              <Badge variant="secondary" className="flex items-center gap-1" aria-label={`Rating: ${r.rating} out of 10`}>
                <Star className="h-3 w-3 fill-current" aria-hidden="true" />
                {r.rating}
              </Badge>
            </div>
            {r.text && <p className="text-muted-foreground">{r.text}</p>}
          </CardContent>
        </Card>
      ))}
    </div>
  );
}

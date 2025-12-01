import React from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Film } from "lucide-react";

export default function EmptyState({
  message = "No movies available.",
}: {
  message?: string;
}) {
  return (
    <Card className="border-dashed">
      <CardContent className="flex flex-col items-center justify-center py-12">
        <Film className="h-12 w-12 text-muted-foreground mb-4" aria-hidden="true" />
        <p className="text-muted-foreground text-center">{message}</p>
      </CardContent>
    </Card>
  );
}

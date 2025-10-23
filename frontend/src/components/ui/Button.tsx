import * as React from "react";

interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: "default" | "ghost";
}

export default function Button({
  className = "",
  variant = "default",
  ...props
}: ButtonProps) {
  const base =
    "inline-flex items-center px-4 py-2 rounded-md text-sm font-medium";
  const variants: Record<string, string> = {
    default: "bg-neutral-900 text-white hover:bg-neutral-800",
    ghost: "bg-transparent text-neutral-900 hover:bg-neutral-100",
  };
  return (
    <button
      className={`${base} ${variants[variant]} ${className}`}
      {...props}
    />
  );
}

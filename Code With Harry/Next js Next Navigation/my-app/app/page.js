"use client"

import { useSearchParams } from "next/navigation";

export default function Home() {
const SearchParams = useSearchParams();

  return (
    <div>
      Main Content
      <p>the Blog is {SearchParams.get("blog")} and utm source is {SearchParams.get("utm-source")} </p>
    </div>
  );
}

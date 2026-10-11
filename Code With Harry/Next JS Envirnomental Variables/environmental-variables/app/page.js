"use client"
export default function Home() {
  console.log("The ID is:", process.env.ID)
  console.log("The ID is:", process.env.SECRET)

  return (
    <div>
      Hey this is home {process.env.NEXT_PUBLIC_ID} and the Secret password is {process.env.SECRET}
    </div>
  );
}

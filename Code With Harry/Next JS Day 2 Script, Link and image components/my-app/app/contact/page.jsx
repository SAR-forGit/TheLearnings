import React from 'react'
import Script from 'next/script'

const contact = () => {
    return (
        <div>
            <Script>
                alert("Welcome to Facebook Contact Page,there's still time to get lost");
            </Script>
            contact us on:
        </div>
    )
}

export default contact


export const metadata = {
    title: "Facebook - Contact",
    description: "Niggah why do u wanna know contact me? Call yo mama instead homie",
};

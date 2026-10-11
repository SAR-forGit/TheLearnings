"use client"

import React from 'react'
import { usePathname } from 'next/navigation'
import Link from 'next/link'

const NavBar = () => {
    const pathName = usePathname();

    return (
        <div>
            <div>{pathName}</div>
            <ul className='flex justify-end-safe gap-2'>
                <Link href="/">Home</Link>
                <Link href="/">Contact</Link>
                <Link href="/">Profile</Link>
            </ul>
        </div>
    )
}

export default NavBar

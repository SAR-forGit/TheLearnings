import React from 'react'
import Link from 'next/link'

const Navbar = () => {
    return (
        <nav className='flex justify-between bg-slate-800 text-white p-5 py-2'>
            <Link href="/">
                <div className="logo font-bold">Facebook</div>
            </Link>
            <ul className="flex gap-6">
                <Link href="/">Home</Link>
                <Link href="/about">About</Link>
                <Link href="/contact">Contact us</Link>
            </ul>
        </nav>
    )
}

export default Navbar

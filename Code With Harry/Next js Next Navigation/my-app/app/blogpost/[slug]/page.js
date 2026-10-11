"use client"
import React, { useEffect } from 'react'
import { useParams } from 'next/navigation'
import { useRouter } from 'next/router'

const page = () => {
    const params = useParams(), router = useRouter();

    useEffect(() => {
        setTimeout(() => {
            router.push('/page')
        }, 2333);
    }, []);

    return (
        <div>
            Hey there {params.slug}

            <button type='button' onClick={() => router.push('/dashboard')}></button>
        </div>
    )
}

export default page

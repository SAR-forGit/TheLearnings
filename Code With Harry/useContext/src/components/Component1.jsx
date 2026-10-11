import React, { useContext } from 'react'
import { counterContext } from '../context/context'

const component1 = () => {
    const value = useContext(counterContext)
    return (
        <div>
            <span>
                {value.count + " "}
                hey there I'm component
            </span>
        </div>
    )
}

export default component1

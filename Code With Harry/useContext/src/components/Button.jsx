import React, { useContext } from 'react'
import Component1 from './Component1.jsx'
import { counterContext } from '../context/context.js'

const Button = () => {
  const value = useContext(counterContext)
  return (
    <button onClick={() => value.setCount((count) => count + 1)}>
      <Component1/>
      Increase Value by Clicking 
    </button>
  )
}

export default Button

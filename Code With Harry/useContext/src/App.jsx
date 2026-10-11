import { useState } from 'react'
import './App.css'
import Navbar from './components/Navbar'
import { counterContext } from './context/context'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    <counterContext.Provider value={{count, setCount}}>
      <Navbar count={count}/>
    </counterContext.Provider>
    </>
  )
}

export default App

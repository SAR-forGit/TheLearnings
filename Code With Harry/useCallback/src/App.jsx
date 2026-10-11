import { useState, useCallback } from 'react'
import './App.css'
import Navbar from './components/Navbar'

function App() {
  const [count, setCount] = useState(0)
  const [adjective, setAdjective] = useState("Good")

  const getAdjective = useCallback(() => { return "another " + count }, [count]);

  // const getAdjective = () => {
  //   return "another " + count;
  // }

  return (
    <>
      <Navbar adjective={"good"} getAdjective={getAdjective} />
      <button onClick={() => { setCount((count) => count + 1) }}>{count}</button>
    </>
  )
}

export default App

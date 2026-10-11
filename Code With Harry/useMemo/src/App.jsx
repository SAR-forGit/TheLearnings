import { useState, useMemo } from 'react'
import './App.css'

const nums = new Array(30_000_000).fill(0).map((_, i) => {
  return {
    index: i,
    isMagical: i === 20_000_000
  }
})

function App() {
  const [count, setCount] = useState(0);

  const [numbers, setNumbers] = useState(nums);

  const magical = useMemo(() => numbers.find(item => item.isMagical === true), [numbers]) //Expensive Computation

  return (
    <>
      <div>
        Magical number is {magical.index}
      </div>
      <button onClick={
        () => {
          setCount((count) => count + 1);
          if (count == 10) {
            setNumbers(new Array(10_000_000).fill(0).map((_, i) => {
              return {
                index: i,
                isMgical: i === 9_000_000
              }
            }))
          }
        }
      }
      >{count}</button >
    </>
  )
}

export default App

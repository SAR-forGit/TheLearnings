import './App.css'
import Navbar from './components/Navbar';
import { useSelector, useDispatch } from 'react-redux'
import { decrement, increment, incrementByAmount } from './redux/counter/counterSlice';

function App() {
  const count = useSelector((state) => state.counter.value),
    dispatch = useDispatch();

  return (
    <>
      <div>
        <Navbar />
        <button onClick={() => dispatch(decrement())}>-</button>
        Currently count is {count}
        <button onClick={() => dispatch(increment())}>+</button>
        <br />
        <button onClick={() => dispatch(incrementByAmount(2))}>Increment By 2</button>
      </div>
    </>
  )
}

export default App

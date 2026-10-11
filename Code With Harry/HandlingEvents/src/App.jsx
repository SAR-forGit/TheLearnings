import { useState } from 'react'
import './App.css'

function App() {
  const [count, setCount] = useState(0)
  // const [name, setName] = useState("Niggesh")
  const [form, setForm] = useState({})


  const handleClick = () => {
    alert("Hey I'm clicked");
  }

  const handleMouseOver = () => {
    alert("I said you don't hover still you did it");
  }
  
  // const handleChange = (e) => {
  //   setName(e.target.value)
  // }

  const handleChange = (e) => {
    setForm({...form, [e.target.name]:e.target.value});
    console.log(form)
  }

  return (
    <>

    <div className="redBlock">
    <button onMouseOver={handleMouseOver}>Do not hover on me</button>
    </div>

    {/* <input type="text" value={name} onChange={handleChange}/>
    <div className="button">
      <button onClick={handleClick}>Click me</button>
    </div> */}

    <input type="text" name='email' value={form?.email} onChange={handleChange}/>
    <input type="text" name='phone' value={form.phone?form.phone:""} onChange={handleChange}/>
    </>
  )
}

export default App

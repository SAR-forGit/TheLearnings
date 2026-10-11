import { useEffect, useState } from 'react'
import './App.css'

function App() {
  const [cards, setCards] = useState([]);

  const fetchData = async () => {
    let a = await fetch("https://jsonplaceholder.typicode.com/posts");
    let data = await a.json();
    setCards(data);
    console.log(data[0])
  }

  useEffect(() => {
    fetchData()
  }, [])

  return (
    <>
      <div className='CardsPlace'>

        {cards.map((card) => (
          <div className="aCard" key={card.id}>
            <h2>{card.title}</h2>
            <p>{card.body}</p>
            <span>UserID {card.id}</span>
          </div>
        ))}
      </div>
    </>
  )
}

export default App

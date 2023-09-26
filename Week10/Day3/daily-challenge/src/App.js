import './App.css';
import { useState } from 'react';

function App() {
  const [languages, setLanguages] = useState([
    {name: "Php", votes: 0},
    {name: "Python", votes: 0},
    {name: "JavaSript", votes: 0},
    {name: "Java", votes: 0}
  ])  

  const addVote = (index) => {
    let plusVote = [...languages]
    plusVote[index].votes += 1;
    setLanguages(plusVote);
  }

  return (
    <div className="App">
      {languages.map((element, id) => {
        return (
          <div style={{ backgroundColor: "beige", margin: "10px auto", border: "2px black solid", padding: "5px", alignItems: "center", justifyContent: "space-around",  width: "300px"}}>
          <h3 key={id}>{element.name} </h3>
          <span>{element.votes} </span>
          <button onClick={() => addVote(id)} style={{background: 'none', color: "green", fontSize: "1rem ", fontWeight: "bold", border: "none"}}>Vote here</button>
          </div>
        )
      })}
    </div> 
  );
}

export default App;

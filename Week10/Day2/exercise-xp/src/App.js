import logo from './logo.svg';
import './App.css';
import UserFavoriteAnimal from './components/UserFavoriteAnimals';
import Exercise from './components/Exercise3';

const user = {
  firstName: 'Bob',
  lastName: 'Dylan',
  favAnimals : ['Horse','Turtle','Elephant','Monkey']
};

function App() {
  const myelement = <h1>I Love JSX!</h1>;
  const sum = 5 + 5;
  return (
    <div className="App">
      <h3>{user.firstName}</h3>
      <h3>{user.lastName}</h3>
      <p>Hello World!</p>
      {myelement}
      <p>React is {sum} times better with JSX</p>
      <UserFavoriteAnimal info={user.favAnimals}></UserFavoriteAnimal>
      <Exercise></Exercise>
    </div>
  );
}

export default App;

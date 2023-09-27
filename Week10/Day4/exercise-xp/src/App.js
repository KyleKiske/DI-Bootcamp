import './App.css';
import React from 'react';
import ErrorBoundary from './Components/ErrorBoundary';
import Color from './Components/Color';

function App() {
  return (
    <div className="App">
      {/* <ErrorBoundary>
        <BuggyCounter/>
        <BuggyCounter/>
      </ErrorBoundary> */}
      <ErrorBoundary>
        <BuggyCounter/>
      </ErrorBoundary>
      <ErrorBoundary>
        <BuggyCounter/>
      </ErrorBoundary>
      <BuggyCounter/>
      <Color></Color>

    </div>
  );
}

class BuggyCounter extends React.Component {
  constructor() {
    super();
    this.state = { counter: 0 };
  }

  handleClick = () => {
    this.setState({counter: this.state.counter +1});
  }

  render() {
    return (
      <div>
        <div onClick={this.handleClick}>
          {this.state.counter > 5 ? (function () {throw new Error('I crashed!')}()) : this.state.counter} 
          
        </div>
      </div>
    )
  }
}

export default App;

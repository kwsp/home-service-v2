import React from 'react';
//import './App.css';
import Button from 'react-bootstrap/Button';

import TopNavBar from './TopNavBar';
import CardRow from './CardRow';


function App() {
  return (
    <div className="App">
      <div className="d-flex flex-column">
        <TopNavBar />
        <CardRow />
      
        <Button>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
        </Button>
      </div>
    </div>
  );
}

export default App;

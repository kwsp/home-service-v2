import React from 'react';
//import './App.css';
import Button from 'react-bootstrap/Button';
import Container from 'react-bootstrap/Container';

import TopNavBar from './TopNavBar';
import CardRow from './CardRow';


function App() {
  return (
    <div className="App">
      <div className="d-flex flex-column">

        <TopNavBar />

        <Container fluid>

            <CardRow />

        </Container>
      
        <Button>
          Learn React
        </Button>
      </div>
    </div>
  );
}

export default App;

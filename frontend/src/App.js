import React from 'react';
//import './App.css';
import Button from 'react-bootstrap/Button';
import Container from 'react-bootstrap/Container';

import TopNavBar from './TopNavBar';
import CardRow from './CardRow';
import LinePlot from './LinePlot';


const width = 500, height = 350, margin = 20;
const data = [
    {a: 1, b: 3},
    {a: 2, b: 6},
    {a: 3, b: 2},
    {a: 4, b: 12},
    {a: 5, b: 8}
];


class App extends React.Component {

  render() {

      return (
        <div className="App">
          <div className="d-flex flex-column">

            <TopNavBar />

            <Container fluid>

                <CardRow />

                <LinePlot data={data} height={height} width={width} margin={margin}/>

            </Container>
          
            <Button>
              "I am a fookin' button"
            </Button>
          </div>
        </div>
      );
  }
}

export default App;

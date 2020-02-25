import React from 'react';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';

import CustomCard from './card';



class TimeCard extends React.Component {
    constructor(props) {
        super(props);
        this.state = {time: new Date().toLocaleTimeString()};
    }

    componentDidMount() {
        this.timerID = setInterval(
            () => this.tick(), 
            1000
        );
    }

    componentWillUnmount() {
        clearInterval(this.timerID);
    }

    tick() {
        this.setState({
            time: new Date().toLocaleTimeString()
        })
    }

    render() {
      return (
          <CustomCard title="Time" text={this.state.time} />
      );
    }
}




class CardRow extends React.Component {

    render() {
        return (
            <Row>
                <Col xl="3" md="6"><TimeCard /></Col>
                <Col xl="3" md="6"><CustomCard title="Temperature" text="bla bla"/></Col>
                <Col xl="3" md="6"><CustomCard title="Humidity" text="bla bla"/></Col>
                <Col xl="3" md="6"><CustomCard title="Andromeda Collision" text="bla bla"/></Col>
            </Row>
            
        )
    }
}

export default CardRow;

import React from 'react';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';

import CustomCard from './card';

class TimeCard extends React.Component {

    componentDidMount() {
      this.interval = setInterval(() => this.setState({ time: Date.now() }), 1000);
    }
    componentWillUnmount() {
      clearInterval(this.interval);
    }

    render() {
        return (
            <CustomCard title="Time" text="bla bla"/>
        )
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

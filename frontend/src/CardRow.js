import React from 'react';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Container from 'react-bootstrap/Container';

import CustomCard from './card';


class CardRow extends React.Component {

    render() {
        return (
            <Container fluid>
                <Row>
                    <Col xl="3" md="6"><CustomCard title="Card 1" text="bla bla"/></Col>
                    <Col xl="3" md="6"><CustomCard title="Card 2" text="bla bla"/></Col>
                    <Col xl="3" md="6"><CustomCard title="Card 3" text="bla bla"/></Col>
                    <Col xl="3" md="6"><CustomCard title="Card 4" text="bla bla"/></Col>
                </Row>
            </Container>
            
        )
    }
}

export default CardRow;

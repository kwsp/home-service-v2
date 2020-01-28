import React from 'react';
import Card from 'react-bootstrap/Card';


class CustomCard extends React.Component {

    //constructor(props) {
        //super(props);
        //this.state = { title: "title", content: "content" }
    //}

    render() { 
        return (
            <Card >
                <Card.Body className="no-gutter align-items-center">
                    <Card.Title as="h5"> {this.props.title}</Card.Title>
                    <Card.Text>
                        {this.props.text}
                    </Card.Text>

                </Card.Body>
            </Card>
        )
    }
}

export default CustomCard;

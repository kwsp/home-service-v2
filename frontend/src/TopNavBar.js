import React from 'react';
import Navbar from 'react-bootstrap/Navbar';
import Nav from 'react-bootstrap/Nav';
import Form from 'react-bootstrap/Form';
import FormControl from 'react-bootstrap/FormControl';


function TopNavBar() {
    return (
        <Navbar bg="dark" variant="dark" expand="lg" mb={3}>
            <Navbar.Brand href="https://tigernie.com">Tiger IoT Dashboard</Navbar.Brand>
            <Nav className="mr-auto">
                <Nav.Link href="#">Home</Nav.Link>

            </Nav>
            <Form inline>
                <FormControl type="text" placeholder="Search" className="mr-sm-2" />
            </Form>
        </Navbar>
    )
}

export default TopNavBar;

import React from 'react';
import { Card, Nav, Row } from 'react-bootstrap';
import { Link } from 'react-router-dom';
import './AboutUs.css'; // Import the CSS file
import Navbar from './Navbar';

const creatorsData = [
    {
      id: 1,
      name: 'Kruttika Abhyankar',
      description: "Introducing Kruttika Abhyankar, a driven and ambitious individual with an unwavering passion for her work in the dynamic field of data science. Join Kruttika on her journey to harness the power of data and turn it into actionable insights. Together, we can explore the endless possibilities of data-driven innovation.",
      image: 'kru_img.jpeg',
    },
    {
      id: 2,
      name: 'Jay Ajmera',
      description: "Meet Jay Ajmera, our passionate data science student and machine learning enthusiast. Leading the team at Analytika NMIMS, Jay spearheads data science projects aimed at solving real-world challenges. Join us on this data-driven journey, and let's collaborate to make a difference.",
      image: 'jay_img.jpeg',
    },
    {
      id: 3,
      name: 'Chirag Chaudhary',
      description: "Meet Chirag Chaudhary, a dedicated individual driven by his pursuit of excellence. With a diverse range of skills and a commitment to continuous growth, Chirag is poised to make a meaningful impact. Join us in celebrating Chirag's journey as he strives for excellence and embraces new challenges.",
      image: 'chirag_img.jpeg',
    },
    {
      id: 4,
      name: 'Ninad Khasale',
      description: "Meet Ninad Khasale, a dedicated and enthusiastic individual. With a thirst for knowledge and a commitment to excellence, Ninad is poised to make a lasting impact in his chosen field. Join us in following Ninad's journey as he pursues his aspirations and contributes to meaningful progress.",
      image: 'ninad_img.jpeg',
    },
  ];

const CreatorsPage = () => {
  return (
    <div className="container mt-5">
      <Navbar />
      <h1>Meet the Creators</h1>
      <Row className="mt-4">
      {creatorsData.map(creator => (
  <div key={creator.id} className="col-md-3 mb-4">
    <Card>
      <Card.Img variant="top" src={creator.image} alt={`Image of ${creator.name}`} className="card-img" />
      <Card.Body>
        <Card.Title>{creator.name}</Card.Title>
        <Card.Text>{creator.description}</Card.Text>
      </Card.Body>
    </Card>
  </div>
))}

      </Row>
    </div>
  );
};

export default CreatorsPage;

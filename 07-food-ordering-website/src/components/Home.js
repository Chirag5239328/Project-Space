import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom'; // Import Link from react-router-dom
import Navbar from './Navbar.js';
import myVideo from './/FOOD.mp4';
import axios from 'axios';


const Home = () => {

  const [restaurants, setRestaurants] = useState([]);

  useEffect(() => {
    // Make an HTTP GET request to fetch restaurant data
    axios.get('http://127.0.0.1:8000/api/restaurants/')
      .then(response => {
        // Set the retrieved data to the state
        setRestaurants(response.data);
        console.log(response.data);
        console.log(restaurants);
      })
      .catch(error => {
        console.error('Error fetching restaurant data:', error);
  });
},[]);

  return (
    <div className="home">

      <Navbar />
      <section className="hero">
        {/* Hero Header Section */}
        <div className="hero-header">
          <h1>Find the Best Restaurants Near You</h1>
          {/* Filter options for veg/non-veg, cuisine, ratings, and price */}
          {/* ... (your filter options here) */}
          <div className="filters">

            {/* Cuisine filter */}
            <select style={{ padding: '5px', borderRadius: '5px', border: '1px solid #ccc',marginRight: '10px' }}>
            <option value="">Select Cuisine</option>
            {/* Add cuisine options */}
            </select>
            {/* Ratings filter */}
            <select style={{ padding: '5px', borderRadius: '5px', border: '1px solid #ccc',marginRight: '10px' }}>
              <option value="">Select Ratings</option>
              {/* Add ratings options */}
            </select>
            {/* Price filter */}
            <select style={{ padding: '5px', borderRadius: '5px', border: '1px solid #ccc',marginRight: '10px' }}>
              <option value="">Select Price Range</option>
              {/* Add price range options */}
            </select>
          </div>
        </div>
        <video autoPlay loop muted>
        <source src={myVideo} type="video/mp4" />
      </video>
      </section>

      {/* Feature Section */}
      <section className="features">
        
        <div className="featured-restaurants">
          {/* Dynamically generate restaurant cards with Link */}
          {restaurants.map(restaurant => (
  <Link to={`/restaurant-menu/${restaurant.id}`} key={restaurant.id}>
    <div className="restaurant-card">
      <img src={restaurant.imageUrl} alt="Restaurant" />
      <h3>{restaurant.name}</h3>
      <p>Cuisine: {restaurant.cuisine}</p>
      <p>Rating: {restaurant.rating}</p>
    </div>
  </Link>
))}
        </div>
      </section>
    </div>
  );
};

export default Home;

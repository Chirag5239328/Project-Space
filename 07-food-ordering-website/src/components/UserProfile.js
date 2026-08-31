import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import Navbar from './Navbar.js';
import './UserProfile.css';
import axios from 'axios';

const UserProfile = () => {
  const [user, setUser] = useState(null);
  const userId = 2; // Replace with the actual user ID

  useEffect(() => {
    // Make an HTTP GET request to fetch user data by user ID
    axios.get('http://127.0.0.1:8000/api/users/')
      .then(response => {
        setUser(response.data[userId]);
      })
      .catch(error => {
        console.error('Error fetching user data:', error);
      });
  }, [userId]);

  if (!user) {
    return <div>Loading...</div>;
  }

  return (
    <div className="user-profile">
      <Navbar />
      <section className="user-details">
        <h1>Welcome, {user.username}!</h1>
        <h2>User Information</h2>
        <p><strong>Username:</strong> {user.username}</p>
        <p><strong>Email:</strong> {user.email}</p>
        <p><strong>Address:</strong> {user.address}</p>
        <p><strong>Phone:</strong> {user.phone_number}</p> {/* Make sure it matches your Django model field name */}
        
        <Link to="/past-orders">
          <button>View Past Orders</button>
        </Link>
        <Link to="/addresses">
          <button>Addresses</button>
        </Link>
      </section>
    </div>
  );
};

export default UserProfile;
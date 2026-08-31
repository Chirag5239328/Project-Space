import React, { useState, useEffect } from 'react';
import Navbar from './Navbar.js';
import './Addresses.css';
import axios from 'axios';

const Addresses = () => {
  const [userAddresses, setUserAddresses] = useState([]);
  const userId = 2; 

  useEffect(() => {
    // Make an HTTP GET request to fetch user addresses data by user ID
    axios.get(`http://127.0.0.1:8000/api/addresses/?user=${userId}`)  // Filter by user ID
      .then(response => {
        setUserAddresses([response.data[0]]);
      })
      .catch(error => {
        console.error('Error fetching user addresses data:', error);
      });
  }, [userId]);

  return (
    <div className="addresses">
      <Navbar />
      <h1>Addresses</h1>
      <ul>
        {userAddresses.map(address => (
          <li key={address.name}>
            <strong>Address Line 1:</strong> {address.address_line1} <br />
            <strong>Address Line 2:</strong> {address.address_line2} <br />
            <strong>City:</strong> {address.city} <br />
            <strong>State:</strong> {address.state} <br />
            <strong>Postal Code:</strong> {address.postal_code}<br />
            <strong>Country:</strong> {address.country}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Addresses;

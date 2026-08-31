import React, { useState, useEffect } from 'react';
import Navbar from './Navbar.js';
import axios from 'axios'; // Import Axios
// get the user id from the local storage
const userId = 2;
const PastOrders = () => {
  const [pastOrders, setPastOrders] = useState([]);

  useEffect(() => {
    // Make an HTTP GET request to fetch past orders data
    axios.get('http://127.0.0.1:8000/api/orders/') // Replace with your Django API URL
      .then(response => {
        setPastOrders([response.data[userId]]);
      })
      .catch(error => {
        console.error('Error fetching past orders data:', error);
      });
  }, []);

  return (
    <div className="past-orders">
      <Navbar />
      <h1>Past Orders</h1>
      <ul>
        {pastOrders.map(order => (
          <li key={order.id}>
            <strong>Restaurant:</strong> {order.restaurant_name} <br />
            <strong>Order Date:</strong> {order.order_date} <br />
            <strong>Status:</strong> {order.status} <br />
            <strong>Total Price:</strong> ${order.total_price}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default PastOrders;

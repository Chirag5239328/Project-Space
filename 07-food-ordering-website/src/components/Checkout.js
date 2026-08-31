import React, { useState } from 'react';
import { useCart } from './CartContext';
import Navbar from './Navbar';
import { Link } from 'react-router-dom';
import './Checkout.css'; // Import the CSS file


const Checkout = () => {
  const { cart } = useCart();
  const [formData, setFormData] = useState({
    address: '',
    paymentType: 'Credit Card',
  });

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Handle form submission logic here (e.g., send order details to the server)
    // Reset the form data after submission if needed
    console.log('Order placed:', { ...formData, cartItems: cart });
  };

  return (
    <div className="checkout">
      <Navbar />
      <h1>Checkout</h1>
      <div className="checkout-form">
        <form onSubmit={handleSubmit}>
          <label>
            Address :
            <input
              type="text"
              name="address"
              value={formData.address}
              onChange={handleInputChange}
              required
            />
          </label>
          <label>
            Payment Type:
            <select name="paymentType" value={formData.paymentType} onChange={handleInputChange} required>
              <option value="Credit Card">Credit Card</option>
              <option value="Debit Card">Debit Card</option>
              <option value="PayPal">PayPal</option>
              {/* Add more payment types as needed */}
            </select>
          </label>
          <button type="submit">Place Order</button>
        </form>
        <div className="order-summary">
          <h2>Order Summary</h2>
          <ul>
            {cart.map((item) => (
              <li key={item.id}>
                {item.name} - Quantity: {item.quantity} - Price: Rs{(item.price * item.quantity).toFixed(2)}
              </li>
            ))}
          </ul>
          <h3>Total: Rs{cart.reduce((total, item) => total + item.price * item.quantity, 0).toFixed(2)}</h3>
        </div>
      </div>
      <Link to="/cart">
        <button>Back to Cart</button>
      </Link>
    </div>
  );
};

export default Checkout;

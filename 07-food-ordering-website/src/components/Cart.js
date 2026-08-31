import React from 'react';
import { useCart } from './CartContext';
import Navbar from './Navbar';
import { Link } from 'react-router-dom';
import './Cart.css'; 

const Cart = () => {
  const { cart, dispatch } = useCart();

  const removeFromCart = (itemId) => {
    dispatch({ type: 'REMOVE_FROM_CART', payload: { id: itemId } });
  };

  const increaseQuantity = (itemId) => {
    dispatch({ type: 'INCREASE_QUANTITY', payload: { id: itemId } });
  };

  const decreaseQuantity = (itemId) => {
    dispatch({ type: 'DECREASE_QUANTITY', payload: { id: itemId } });
  };

  const calculateSubtotal = () => {
    return cart.reduce((total, item) => total + item.price * item.quantity, 0).toFixed(2);
  };

  return (
    <div className="cart">
      <Navbar />
      <h1 className='heading'>Shopping Cart</h1>
      {cart.length === 0 ? (
        <p>Your cart is empty.</p>
      ) : (
        <div className="cart-items">
          {cart.map((item) => (
            <div className="cart-item" key={item.id}>
              <div className="item-details">
                <h3>{item.name}</h3>
                <div className="quantity-controls">
                <p>Quantity: {item.quantity}</p>
                  <button className="button1" onClick={() => decreaseQuantity(item.id)}>-</button>
                  <button className="button1" onClick={() => increaseQuantity(item.id)}>+</button>
                </div>
                <p>Price: Rs {item.price.toFixed(2)}</p>
                <button className="button1" onClick={() => removeFromCart(item.id)}>Remove</button>
              </div>
            </div>
          ))}
          <div className="subtotal">
            <h2>Total: Rs {calculateSubtotal()}</h2>
            <Link to="/checkout">
              <button>Place Order</button>
            </Link>
          </div>
        </div>
      )}
    </div>
  );
};

export default Cart;

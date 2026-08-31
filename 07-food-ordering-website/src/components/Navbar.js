import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <nav className="navbar">
      <div className="logo">
       <h1>Kwick Kravings<img src="/taco.png" alt="Profile" className='small-image'/></h1>
      </div>
      <ul className="nav-links">
        <li><Link to="/">Home</Link></li>
        <li><Link to="/cart">Cart</Link> </li>
        <li><Link to="/user-profile">Profile</Link></li>
        <li><Link to="/about-us">About Us</Link></li>
        {/* Add more navigation links as needed */}
      </ul>
    </nav>
  );
};

export default Navbar;

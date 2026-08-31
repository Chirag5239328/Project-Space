import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import Navbar from './Navbar';
import { useCart } from './CartContext';
import './RestaurantMenu.css';

const restaurantData = [
  {
    id: 1,
    name: 'Bella Italia',
    rating: 4.5,
    menu: [
      { id: 1, name: 'Pesto', description: 'Delicious Pesto pasta with a burst of basil flavor.', price: 350, imageUrl: '/ita1.jpg', rating: 4.2 },
      { id: 2, name: 'Red Sauce Pasta', description: 'Classic Italian pasta with rich and tangy red sauce.', price: 375, imageUrl: '/ita4.jpg', rating: 3.5 },
      { id: 3, name: 'White Sauce Pasta', description: 'Creamy white sauce pasta to satisfy your cravings.', price: 359, imageUrl: '/pasta.jpg', rating: 4.0 }
    ]
  },
  {
    id: 2,
    name: 'Tortilla Street',
    rating: 4.5,
    menu: [
      { id: 4, name: 'Macaroni', description: 'Savor the cheesy delight of Macaroni for a comforting meal.', price: 249.99, imageUrl: '/mex4.jpg', rating: 4.5 },
      { id: 5, name: 'Canopies', description: 'Enjoy a delightful assortment of Canopies, perfect for sharing.', price: 199.50, imageUrl: '/mex1.jpg', rating: 4.6 },
      { id: 6, name: 'Nachos', description: 'Crunch on the zesty Nachos loaded with flavorful toppings.', price: 179.99, imageUrl: '/mex2.jpg', rating: 4.4 }
    ]
  },
  {
    id: 3,
    name: 'Indian Masala House',
    rating: 4.8,
    menu: [
      { id: 7, name: 'Biryani', description: 'Indulge in aromatic Biryani, a flavorful delight from India.', price: 399.00, imageUrl: '/ind1.jpg', rating: 4.7 },
      { id: 8, name: 'Idli', description: 'Experience the soft and fluffy Idli, a South Indian classic.', price: 159.99, imageUrl: '/ind2.jpg', rating: 4.5 },
      { id: 9, name: 'Chole-Puri', description: 'Delight in the spicy and tangy Chole-Puri combo.', price: 179.50, imageUrl: '/ind3.jpg', rating: 4.6 }
    ]
  }
  // Add more restaurants as needed
];

  
  
  
  const RestaurantMenu = () => {
    const { id } = useParams();
    const [restaurant, setRestaurant] = useState(null);
    const { cart, dispatch } = useCart();
  
    useEffect(() => {
      const selectedRestaurant = restaurantData.find(rest => rest.id === parseInt(id, 10));
      setRestaurant(selectedRestaurant);
    }, [id]);
  
    const addToCart = (item) => {
      const newItem = { ...item, quantity: 1 };
      dispatch({ type: 'ADD_TO_CART', payload: newItem });
      alert('${item.name} added to cart!');
    };
  
    if (!restaurant) {
      return <div>Loading...</div>;
    }
  
    return (
      <div className="restaurant-menu">
        <Navbar />
        <section className="blog-post-header">
          <h1>{restaurant.name}</h1>
          <p>Restaurant Rating: {restaurant.rating}</p>
        </section>
  
        <section className="blog-post-body">
          <h2>Menu</h2>
          <div className="menu-items">
            {restaurant.menu.map(item => (
              <div className="menu-item" key={item.id}>
                <img src={item.imageUrl} alt={item.name} />
                <h4>{item.name}</h4>
                <p>{item.description}</p>
                <p>Rating: {item.rating}</p>
                <p>Price: Rs{item.price.toFixed(2)}</p>
                <button onClick={() => addToCart(item)}>Add to Cart</button>
              </div>
            ))}
          </div>
        </section>
      </div>
    );
  };
  
  export default RestaurantMenu;
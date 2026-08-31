import React from 'react';
import './App.css';
import AppRouter from './AppRouter';
import { CartProvider } from './components/CartContext'; // Import CartProvider from CartContext


function App() {
  return (
    <div className="App">
      <CartProvider> {/* Wrap AppRouter with CartProvider */}
        <AppRouter />
      </CartProvider>
      
    </div>
  );
}

export default App;

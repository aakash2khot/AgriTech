import React from 'react';
import '../styles/Header.css';  // Import header styles
import logo from '../assets/images/logo.png';

function Header() {
  return (
    <header className="Header">
      <img src={logo} alt="AGRITECH Logo" className="Header-logo" />
      <h1>AGRITECH</h1>
      <p>Your Agricultural Crop Recommendation System</p>
    </header>
  );
}

export default Header;

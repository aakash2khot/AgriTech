import React from 'react';
import { Link } from 'react-router-dom';
import '../../styles/MainMenu.css';

function MainMenu() {
  return (
    <div className="main-menu">
      <h2>Welcome to AgriTech</h2>
      <p>Select a service to get started:</p>
      <Link to="/crop-recommendation" className="main-menu-link">Crop Recommendation</Link>
      <Link to="/plant-disease-detection" className="main-menu-link">Plant Disease Detection</Link>
    </div>
  );
}

export default MainMenu;

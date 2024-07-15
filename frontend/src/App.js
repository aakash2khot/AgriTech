import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import CropRecommendationForm from './components/CropRecommendation/Form';
import PlantDiseaseDetectionForm from './components/PlantDiseaseDetection/Form';
import CropRecommendationResult from './components/CropRecommendation/Result';  // Import CropRecommendationResult component
import PlantDiseaseDetectionResult from './components/PlantDiseaseDetection/Result';  // Import PlantDiseaseDetectionResult component
import './styles/App.css';

function App() {
  const [recommendation, setRecommendation] = useState('');  // State for crop recommendation
  const [disease, setDisease] = useState('');  // State for plant disease detection

  return (
    <Router>
      <div className="app">
        <main>
          <Routes>
            <Route path="/crop-recommendation" element={
              <div>
                <CropRecommendationForm setRecommendation={setRecommendation} />
                {recommendation && <CropRecommendationResult recommendedCrop={recommendation} />}  {/* Display recommendation result */}
              </div>
            } />
            <Route path="/plant-disease-detection" element={
              <div>
                <PlantDiseaseDetectionForm setDisease={setDisease} />
                {disease && <PlantDiseaseDetectionResult disease={disease} />}  {/* Display disease detection result */}
              </div>
            } />
            <Route path="/" element={
              <div className="main-menu">
                <h2>Welcome to AgriTech</h2>
                <p>Select a service to get started:</p>
                <Link to="/crop-recommendation" className="main-menu-link">Crop Recommendation</Link>
                <Link to="/plant-disease-detection" className="main-menu-link">Plant Disease Detection</Link>
              </div>
            } />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;

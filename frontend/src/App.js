import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import CropRecommendationForm from './components/CropRecommendation/Form';
import PlantDiseaseDetectionForm from './components/PlantDiseaseDetection/Form';
import FertilizerRecommendationForm from './components/FertilizerRecommendation/Form';
import PestInfestationForm from './components/PestInfestation/Form';
import CropRecommendationResult from './components/CropRecommendation/Result';
import PlantDiseaseDetectionResult from './components/PlantDiseaseDetection/Result';
import FertilizerRecommendationResult from './components/FertilizerRecommendation/Result';
import PestInfestationResult from './components/PestInfestation/Result';
import './styles/App.css';

function App() {
  const [recommendation, setRecommendation] = useState('');
  const [disease, setDisease] = useState('');
  const [pest, setPest] = useState('');

  return (
    <Router>
      <div className="app">
        <main>
          <Routes>
            <Route path="/crop-recommendation" element={
              <div>
                <CropRecommendationForm setRecommendation={setRecommendation} />
                {recommendation && <CropRecommendationResult recommendedCrop={recommendation} />}
              </div>
            } />
            <Route path="/plant-disease-detection" element={
              <div>
                <PlantDiseaseDetectionForm setDisease={setDisease} />
                {disease && <PlantDiseaseDetectionResult disease={disease} />}
              </div>
            } />
            <Route path="/fertilizer-recommendation" element={
              <FertilizerRecommendationForm setRecommendation={setRecommendation} />
            } />
            <Route path="/fertilizer-result" element={<FertilizerRecommendationResult recommendation={recommendation} />} />
            <Route path="/pest-infestation" element={
              <div>
                <PestInfestationForm setPest={setPest} />
                {pest && <PestInfestationResult pest={pest} />}
              </div>
            } />
            <Route path="/" element={
              <div className="main-menu">
                <h2>Welcome to AgriTech</h2>
                <p>Hi There, Welcome Back!</p>
                <Link to="/crop-recommendation" className="main-menu-link">Crop Recommendation</Link>
                <Link to="/plant-disease-detection" className="main-menu-link">Plant Disease Detection</Link>
                <Link to="/fertilizer-recommendation" className="main-menu-link">Fertilizer Recommendation</Link>
                <Link to="/pest-infestation" className="main-menu-link">Pest Infestation</Link>
              </div>
            } />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;

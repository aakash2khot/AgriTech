import React from 'react';
import { Link } from 'react-router-dom';
import '../../styles/FertilizerRecommendation.css';

function FertilizerRecommendationResult({ recommendation }) {
  return (
    <div className="fertilizer-result-container">
      <h2>Fertilizer Recommendation</h2>
      <div className="fertilizer-recommendation-box">
        <p dangerouslySetInnerHTML={{ __html: recommendation }}></p>
      </div>
      <Link to="/fertilizer-recommendation" className="fertilizer-back-link">Back to Fertilizer Recommendation</Link>
    </div>
  );
}

export default FertilizerRecommendationResult;

import React from 'react';
import '../../styles/Result.css';

function CropRecommendationResult({ recommendedCrop }) {
  return (
    <div className="result">
      <h2>Recommended Crop:</h2>
      <p>{recommendedCrop}</p>
    </div>
  );
}

export default CropRecommendationResult;

import React from 'react';
import '../../styles/Result.css';

function PlantDiseaseDetectionResult({ disease }) {
  return (
    <div className="result">
      <h2>Predicted Disease:</h2>
      <p>{disease}</p>
    </div>
  );
}

export default PlantDiseaseDetectionResult;

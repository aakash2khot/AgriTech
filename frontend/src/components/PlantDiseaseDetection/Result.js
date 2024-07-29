// Result.js
import React from 'react';
import '../../styles/Result.css';

function PlantDiseaseDetectionResult({ disease, diseaseInfo }) {
  return (
    <div className="result">
      <h2>Predicted Disease:</h2>
      <p>{disease}</p>
      <h3>Disease Information:</h3>
      <div dangerouslySetInnerHTML={{ __html: diseaseInfo }}></div>
    </div>
  );
}

export default PlantDiseaseDetectionResult;

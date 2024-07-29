import React from 'react';
import '../../styles/PestInfestation.css';

const PestInfestationResult = ({ pest, managementStrategies }) => {
  return (
    <div className="pest-result-container">
      <h2>Pest Infestation Result</h2>
      <p>Predicted Pest: {pest}</p>
      {managementStrategies && (
        <div className="pest-management-box">
          <h3>Management Strategies for {managementStrategies.name}</h3>
          <p>{managementStrategies.description}</p>
          <ul>
            {managementStrategies.management.map((strategy, index) => (
              <li key={index}>{strategy}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default PestInfestationResult;

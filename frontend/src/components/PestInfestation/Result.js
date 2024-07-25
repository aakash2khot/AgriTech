import React from 'react';

const PestInfestationResult = ({ pest }) => {
  return (
    <div>
      <h2>Pest Infestation Result</h2>
      <p>Predicted Pest: {pest}</p>
    </div>
  );
};

export default PestInfestationResult;

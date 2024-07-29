import React, { useState } from 'react';
import axios from 'axios';
import '../../styles/PestInfestation.css';

const PestInfestationForm = ({ setPest, setManagementStrategies }) => {
  const [file, setFile] = useState(null);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post('/pest-detection/predict-pest', formData, {
        headers: { 'Content-Type': 'multipart/form-data' }
      });
      setPest(response.data.predicted_pest);
      setManagementStrategies(response.data.management_strategies);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div className="pest-form-container">
      <h2>Pest Infestation Detection</h2>
      <form onSubmit={handleSubmit}>
        <input type="file" onChange={handleFileChange} required />
        <button type="submit">Predict Pest</button>
      </form>
    </div>
  );
};

export default PestInfestationForm;

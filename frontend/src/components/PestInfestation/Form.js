import React, { useState } from 'react';
import axios from 'axios';

const PestInfestationForm = ({ setPest }) => {
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
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div>
      <h2>Pest Infestation Detection</h2>
      <form onSubmit={handleSubmit}>
        <input type="file" onChange={handleFileChange} />
        <button type="submit">Predict Pest</button>
      </form>
    </div>
  );
};

export default PestInfestationForm;

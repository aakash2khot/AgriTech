// Form.js
import React, { useState } from 'react';
import axios from 'axios';
import '../../styles/Form.css';

function PlantDiseaseDetectionForm({ setDisease, setDiseaseInfo }) {
  const [selectedFile, setSelectedFile] = useState(null);

  const handleFileChange = (e) => {
    setSelectedFile(e.target.files[0]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!selectedFile) {
      console.error('No file selected');
      return;
    }

    const formData = new FormData();
    formData.append('file', selectedFile);

    try {
      const response = await axios.post('/plant-disease-detection/predict-disease', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      console.log('Response from backend:', response.data);

      // Pass the result to the setDisease and setDiseaseInfo prop functions
      setDisease(response.data.predicted_disease);
      setDiseaseInfo(response.data.disease_info);
    } catch (error) {
      console.error('There was an error making the request:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="form">
      <label>
        Upload Image:
        <input type="file" onChange={handleFileChange} />
      </label>
      <button type="submit">Predict Disease</button>
    </form>
  );
}

export default PlantDiseaseDetectionForm;

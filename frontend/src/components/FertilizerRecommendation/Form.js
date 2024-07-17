import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import '../../styles/FertilizerRecommendation.css';

function FertilizerRecommendationForm({ setRecommendation }) {
  const [cropname, setCropname] = useState('');
  const [nitrogen, setNitrogen] = useState('');
  const [phosphorous, setPhosphorous] = useState('');
  const [pottasium, setPottasium] = useState('');
  const navigate = useNavigate();

  useEffect(() => {
    // Clear the recommendation when this form is mounted
    setRecommendation('');
  }, [setRecommendation]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('/fertilizer-recommendation/fertilizer-predict', {
        cropname,
        nitrogen,
        phosphorous,
        pottasium,
      }, {
        headers: {
          'Content-Type': 'application/json',
        },
      });
      setRecommendation(response.data.recommendation);
      navigate('/fertilizer-result');
    } catch (error) {
      console.error('Error recommending fertilizer:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="fertilizer-form-container">
      <div>
        <label>Crop Name:</label>
        <input type="text" value={cropname} onChange={(e) => setCropname(e.target.value)} required />
      </div>
      <div>
        <label>Nitrogen Value:</label>
        <input type="number" value={nitrogen} onChange={(e) => setNitrogen(e.target.value)} required />
      </div>
      <div>
        <label>Phosphorous Value:</label>
        <input type="number" value={phosphorous} onChange={(e) => setPhosphorous(e.target.value)} required />
      </div>
      <div>
        <label>Potassium Value:</label>
        <input type="number" value={pottasium} onChange={(e) => setPottasium(e.target.value)} required />
      </div>
      <button type="submit">Get Fertilizer Recommendation</button>
    </form>
  );
}

export default FertilizerRecommendationForm;

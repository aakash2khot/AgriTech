import React, { useState } from 'react';
import axios from 'axios';
import '../../styles/Form.css';  // Adjust path to your CSS if needed

function CropRecommendationForm({ setRecommendation }) {
  const [formData, setFormData] = useState({
    N: '',
    P: '',
    K: '',
    city: '',
    rainfall: '',
    ph: ''
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    console.log("Sending data:", formData);  // Debugging statement

    try {
      const response = await axios.post('/crop-recommendation/recommend', new URLSearchParams(formData), {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
      });
      console.log('Response from backend:', response.data);  // Debugging statement

      // Pass the result to the setRecommendation prop function
      setRecommendation(response.data.recommended_crop);
    } catch (error) {
      console.error('There was an error making the request:', error);
    }
  };

  return  (
    <form onSubmit={handleSubmit} className="form">
    <h2>Crop Recommendation Form</h2>
      <label>
        N:
        <input type="text" name="N" value={formData.N} onChange={handleChange} />
      </label>
      <label>
        P:
        <input type="text" name="P" value={formData.P} onChange={handleChange} />
      </label>
      <label>
        K:
        <input type="text" name="K" value={formData.K} onChange={handleChange} />
      </label>
      <label>
        City:
        <input type="text" name="city" value={formData.city} onChange={handleChange} />
      </label>
      <label>
        Rainfall:
        <input type="text" name="rainfall" value={formData.rainfall} onChange={handleChange} />
      </label>
      <label>
        pH:
        <input type="text" name="ph" value={formData.ph} onChange={handleChange} />
      </label>
      <button type="submit">Get Recommendation</button>
    </form>

  );
}

export default CropRecommendationForm;

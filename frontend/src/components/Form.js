// import React, { useState } from 'react';
// import axios from 'axios';
// import '../styles/Form.css';  // Import form styles

// function Form({ onSubmit }) {
//   const [formData, setFormData] = useState({
//     N: '',
//     P: '',
//     K: '',
//     city: '',
//     rainfall: '',
//     ph: ''
//   });

//   const handleChange = (e) => {
//     setFormData({
//       ...formData,
//       [e.target.name]: e.target.value
//     });
//   };

//   const handleSubmit = async (e) => {
//     e.preventDefault();
//     console.log("Sending data:", formData);  // Debugging statement

//     try {
//       const response = await axios.post('/recommend', new URLSearchParams(formData), {
//         headers: {
//           'Content-Type': 'application/x-www-form-urlencoded',
//         },
//       });
//       console.log('Response from backend:', response.data);  // Debugging statement
//       onSubmit(response.data.recommended_crop);
//     } catch (error) {
//       console.error('There was an error making the request:', error);
//     }
//   };

//   return (
//     <form onSubmit={handleSubmit} className="Form">
//       <label htmlFor="N">Nitrogen (N):</label>
//       <input
//         type="number"
//         name="N"
//         id="N"
//         value={formData.N}
//         onChange={handleChange}
//         placeholder="Enter Nitrogen value"
//         style={{ color: 'black' }}
//       />

//       <label htmlFor="P">Phosphorous (P):</label>
//       <input
//         type="number"
//         name="P"
//         id="P"
//         value={formData.P}
//         onChange={handleChange}
//         placeholder="Enter Phosphorous value"
//         style={{ color: 'black' }}
//       />

//       <label htmlFor="K">Potassium (K):</label>
//       <input
//         type="number"
//         name="K"
//         id="K"
//         value={formData.K}
//         onChange={handleChange}
//         placeholder="Enter Potassium value"
//         style={{ color: 'black' }}
//       />

//       <label htmlFor="city">City:</label>
//       <input
//         type="text"
//         name="city"
//         id="city"
//         value={formData.city}
//         onChange={handleChange}
//         placeholder="Enter City"
//         style={{ color: 'black' }}
//       />

//       <label htmlFor="rainfall">Rainfall (mm):</label>
//       <input
//         type="number"
//         name="rainfall"
//         id="rainfall"
//         value={formData.rainfall}
//         onChange={handleChange}
//         placeholder="Enter Rainfall in mm"
//         style={{ color: 'black' }}
//       />

//       <label htmlFor="ph">pH:</label>
//       <input
//         type="number"
//         name="ph"
//         id="ph"
//         value={formData.ph}
//         onChange={handleChange}
//         placeholder="Enter pH value"
//         style={{ color: 'black' }}
//       />

//       <button type="submit">Get Recommendation</button>
//     </form>
//   );
// }

// export default Form;

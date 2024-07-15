from flask import Blueprint, request, jsonify
import pickle
import numpy as np
import requests  # Make sure you have requests library

crop_recommendation_bp = Blueprint('crop_recommendation_bp', __name__)

# Load the pre-trained model
model_path = 'models/RandomForest.pkl'
with open(model_path, 'rb') as f:
    crop_recommendation_model = pickle.load(f)

def weather_fetch(city_name):
    """
    Fetch and returns the temperature and humidity of a city
    :params: city_name
    :return: temperature, humidity
    """
    api_key = 'bdbd1fd2ecab8758770a6522def4e64e'
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()

    if x["cod"] != "404":
        y = x["main"]

        temperature = round((y["temp"] - 273.15), 2)
        humidity = y["humidity"]
        return temperature, humidity
    else:
        return None

@crop_recommendation_bp.route('/recommend', methods=['POST'])
def recommend_crop():
    try:
        # Extract form data
        data = request.form
        print(f"Received data: {data}")  # Debugging statement
        
        # Extract features
        N = int(data.get('N', 0))
        P = int(data.get('P', 0))
        K = int(data.get('K', 0))
        city = data.get('city', '')  # Get city from form data
        rainfall = float(data.get('rainfall', 0))
        ph = float(data.get('ph', 0))

        # Fetch weather data
        weather_data = weather_fetch(city)
        if weather_data:
            temperature, humidity = weather_data
        else:
            temperature, humidity = 0, 0  # Set default values if city is not found

        # Create input array for the model
        input_features = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
        print(f"Input features: {input_features}")  # Debugging statement
        
        # Make prediction
        my_prediction = crop_recommendation_model.predict(input_features)
        final_prediction = my_prediction[0]
        print(f"Prediction: {final_prediction}")  # Debugging statement
        
        return jsonify({'recommended_crop': final_prediction})
    except Exception as e:
        print(f"Error: {e}")  # Debugging statement
        return jsonify({'error': str(e)}), 500

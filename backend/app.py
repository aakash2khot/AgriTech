from flask import Flask
from flask_cors import CORS
from routes.crop_recommendation import crop_recommendation_bp
from routes.plant_disease_detection import plant_disease_detection_bp
from routes.fertilizer_recommendation import fertilizer_recommendation_bp
from routes.pest_detection import pest_detection_bp  # Import the pest detection blueprint

app = Flask(__name__)
CORS(app)

# Register blueprints with new URL prefixes
app.register_blueprint(crop_recommendation_bp, url_prefix='/crop-recommendation')
app.register_blueprint(plant_disease_detection_bp, url_prefix='/plant-disease-detection')
app.register_blueprint(fertilizer_recommendation_bp, url_prefix='/fertilizer-recommendation')
app.register_blueprint(pest_detection_bp, url_prefix='/pest-detection')  # Register the pest detection blueprint

if __name__ == '__main__':
    print("Starting server...")
    app.run(debug=True)

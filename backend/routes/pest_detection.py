import os
import torch
from flask import Blueprint, request, jsonify
from torchvision import transforms, models
from PIL import Image
import io
import numpy as np

# Define the Blueprint for pest detection
pest_detection_bp = Blueprint('pest_detection_bp', __name__)

# Define classes (update with your actual class names)
pest_classes = ["aphids", "armyworm", "beetle", "bollworm", "grasshopper", "mites", "mosquito", "sawfly", "stem borer"]

# Load the pre-trained ResNet model for feature extraction
resnet50_model = models.resnet50(weights='DEFAULT')
resnet50_model.eval()

# Load the logistic regression model
logreg_model_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'logreg_model.pth')
logreg_model = torch.nn.Linear(1000, len(pest_classes))  # Assuming 2048 is the feature size from ResNet50
logreg_model.load_state_dict(torch.load(logreg_model_path, map_location=torch.device('cpu')))
logreg_model.eval()

# Define the image transformation
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# Function to extract features using ResNet-50
def extract_features(image, model):
    img_t = transform(image)
    img_u = torch.unsqueeze(img_t, 0)
    
    with torch.no_grad():
        features = model(img_u)
        features = features.view(features.size(0), -1)
    
    return features

# Function to make predictions using the logistic regression model
def predict_pest(image):
    features = extract_features(image, resnet50_model)
    with torch.no_grad():
        outputs = logreg_model(features)
        _, preds = torch.max(outputs, dim=1)
        prediction = pest_classes[preds[0].item()]
    return prediction

@pest_detection_bp.route('/predict-pest', methods=['POST'])
def predict_pest_route():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'}), 400
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400

        img = file.read()
        image = Image.open(io.BytesIO(img))
        prediction = predict_pest(image)

        return jsonify({'predicted_pest': prediction})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': str(e)}), 500

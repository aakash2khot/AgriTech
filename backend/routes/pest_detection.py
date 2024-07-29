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

# Define pest management strategies
pest_management_dic = {
    "aphids": {
        "name": "Aphids",
        "description": "Aphids are small sap-sucking insects.",
        "management": [
            "Introduce natural predators such as ladybugs.",
            "Use insecticidal soaps or neem oil.",
            "Remove aphids manually by spraying water."
        ]
    },
    "armyworm": {
        "name": "Armyworm",
        "description": "Armyworms are the caterpillar life stage of a moth.",
        "management": [
            "Use pheromone traps to monitor and control the population.",
            "Apply Bacillus thuringiensis (Bt) or other biological insecticides.",
            "Remove weeds and plant debris to reduce habitat."
        ]
    },
    "beetle": {
        "name": "Beetle",
        "description": "Beetles are a group of insects that can cause significant damage to crops.",
        "management": [
            "Use row covers to protect plants from beetles.",
            "Apply neem oil or other insecticides.",
            "Introduce beneficial nematodes to control beetle larvae."
        ]
    },
    "bollworm": {
        "name": "Bollworm",
        "description": "Bollworms are a common pest of cotton and other crops.",
        "management": [
            "Use Bacillus thuringiensis (Bt) sprays.",
            "Introduce natural enemies such as trichogramma wasps.",
            "Implement crop rotation to break the life cycle of the pest."
        ]
    },
    "grasshopper": {
        "name": "Grasshopper",
        "description": "Grasshoppers are herbivorous insects that can consume large amounts of plant material.",
        "management": [
            "Use biological control agents like protozoa or nematodes.",
            "Apply insecticidal baits in affected areas.",
            "Create barriers or use row covers to protect plants."
        ]
    },
    "mites": {
        "name": "Mites",
        "description": "Mites are small arthropods that can cause damage by feeding on plant sap.",
        "management": [
            "Introduce predatory mites to control the pest population.",
            "Apply horticultural oils or insecticidal soaps.",
            "Maintain proper plant hygiene and remove infested plant parts."
        ]
    },
    "mosquito": {
        "name": "Mosquito",
        "description": "Mosquitoes are a common pest that can spread diseases.",
        "management": [
            "Eliminate standing water where mosquitoes breed.",
            "Use mosquito nets or screens to protect plants.",
            "Apply larvicides to water sources to kill mosquito larvae."
        ]
    },
    "sawfly": {
        "name": "Sawfly",
        "description": "Sawflies are insects that can cause defoliation in plants.",
        "management": [
            "Handpick larvae from plants and destroy them.",
            "Introduce natural predators like birds or parasitic wasps.",
            "Use insecticidal sprays specifically for sawflies."
        ]
    },
    "stem borer": {
        "name": "Stem Borer",
        "description": "Stem borers are larvae that bore into the stems of plants, causing damage.",
        "management": [
            "Apply Bacillus thuringiensis (Bt) or other biological insecticides.",
            "Use pheromone traps to monitor and reduce the pest population.",
            "Remove and destroy infested plant parts."
        ]
    },
    "leafhopper": {
        "name": "Leafhopper",
        "description": "Leafhoppers are insects that suck sap from plants, causing damage.",
        "management": [
            "Introduce natural predators such as lacewings and ladybugs.",
            "Apply insecticidal soaps or neem oil.",
            "Use reflective mulches to repel leafhoppers."
        ]
    },
    "mealybug": {
        "name": "Mealybug",
        "description": "Mealybugs are soft-bodied insects that suck plant sap, causing damage.",
        "management": [
            "Introduce natural enemies like ladybugs and parasitic wasps.",
            "Apply horticultural oils or insecticidal soaps.",
            "Remove and destroy heavily infested plant parts."
        ]
    },
    "whitefly": {
        "name": "Whitefly",
        "description": "Whiteflies are small insects that feed on plant sap and can transmit diseases.",
        "management": [
            "Use yellow sticky traps to monitor and reduce whitefly populations.",
            "Introduce natural enemies such as ladybugs and lacewings.",
            "Apply insecticidal soaps or neem oil."
        ]
    },
    "thrips": {
        "name": "Thrips",
        "description": "Thrips are tiny insects that feed on plants, causing damage to leaves and flowers.",
        "management": [
            "Introduce natural predators like predatory mites and minute pirate bugs.",
            "Use blue sticky traps to monitor and control thrips.",
            "Apply insecticidal soaps or neem oil."
        ]
    }
}


# Load the pre-trained ResNet model for feature extraction
resnet50_model = models.resnet50(weights='DEFAULT')
resnet50_model.eval()

# Load the logistic regression model
logreg_model_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'logreg_model.pth')
logreg_model = torch.nn.Linear(1000, len(pest_classes))
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
        management_strategies = pest_management_dic.get(prediction, {})

        return jsonify({'predicted_pest': prediction, 'management_strategies': management_strategies})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': str(e)}), 500

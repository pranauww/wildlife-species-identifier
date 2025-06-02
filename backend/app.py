from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
from PIL import Image
import io
import joblib
import logging
import tensorflow as tf
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the saved model, scaler, and label encoder
try:
    model = joblib.load('svm_model.pkl')
    scaler = joblib.load('scaler.pkl')
    label_encoder = joblib.load('label_encoder.pkl')
    logger.info("Successfully loaded model, scaler, and label encoder")
except Exception as e:
    logger.error(f"Error loading model files: {str(e)}")
    raise

# Load ResNet50 for feature extraction
try:
    resnet = ResNet50(weights='imagenet', include_top=False, pooling='avg')
    logger.info("Successfully loaded ResNet50 model")
except Exception as e:
    logger.error(f"Error loading ResNet50: {str(e)}")
    raise

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    try:
        # Read and preprocess the image
        image = Image.open(io.BytesIO(file.read()))
        image = image.convert('RGB')  # Convert to RGB if image is in different format
        image = image.resize((224, 224))  # Resize to match ResNet50's expected input
        
        # Convert image to array and preprocess for ResNet50
        image_array = img_to_array(image)
        image_array = np.expand_dims(image_array, axis=0)
        image_array = preprocess_input(image_array)
        
        # Extract features using ResNet50
        features = resnet.predict(image_array, verbose=0)
        logger.debug(f"ResNet50 feature shape: {features.shape}")
        
        # Scale the features
        scaled_features = scaler.transform(features)
        logger.debug(f"Feature shape after scaling: {scaled_features.shape}")
        
        # Make prediction
        prediction = model.predict(scaled_features)
        
        # Convert numeric prediction back to common name
        species_name = label_encoder.inverse_transform(prediction)[0]
        
        logger.info(f"Successfully predicted species: {species_name}")
        return jsonify({'prediction': species_name})
    
    except Exception as e:
        logger.error(f"Error during prediction: {str(e)}", exc_info=True)
        return jsonify({'error': f'Error processing image: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True) 
from flask import Flask, request, jsonify, send_from_directory
import joblib
import os

app = Flask(__name__)

# Load pricing model from .pkl
model = joblib.load('rolex_pricing_model.pkl')

# Prediction route
@app.route('/predict', methods = ['POST'])
def predict():
    data = request.get_json()
    year = int(data.get('year', 0))
    condition = data.get('condition', '')
    prediction = model.predict([[year], [condition]])[0]

    # Fetch Rolex model image
    rolex_model_name = data.get('model', '').replace(' ', '_').lower()
    image_path = f'images/{rolex_model_name}.jpg'
    image_url = image_path if os.path.exists(image_path) else 'images/default.jpg'

    return jsonify({'predicted_price': round(prediction, 2), 'image_url': image_url})

# Serve images to API
@app.route('/images/<filename>')
def get_images(filename):
    return send_from_directory('images', filename)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000, debug = True)
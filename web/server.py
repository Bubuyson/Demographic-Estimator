from flask import Flask, render_template, request, jsonify
import matplotlib.pyplot as plt
from crop_test import process_image
from pipeline_main import load_models, predict_labels
from mtcnn.mtcnn import MTCNN
import os

app = Flask(__name__)
emotion_model, race_model, gender_model, age_model = load_models()
detector = MTCNN()

# Route to render the upload form

@app.route('/')
def index():
    return render_template('index.html', processed_file="")

# Route to handle the file upload
@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']
    
    if file.filename == '':
        return "No selected file"

    if file:
        # Save the uploaded file
        uploaded_file_path = os.path.join('static\\uploads', file.filename)
        file.save(uploaded_file_path)

        # Process the uploaded image
        #process_image(file.filename)
        predict_labels(emotion_model=emotion_model, race_model=race_model, gender_model=gender_model, age_model=age_model, input_image_name=file.filename, detector=detector)

        return jsonify({'image_name': file.filename})

if __name__ == '__main__':
    app.run(debug=True)
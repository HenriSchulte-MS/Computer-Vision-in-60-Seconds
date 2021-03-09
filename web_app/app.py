from recognize_image import recognize_image
import os
from flask import Flask, render_template, request, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recognize', methods=['GET', 'POST'])
def recognize():
    # Get image
    if request.method == 'POST':
        image = request.files['image']

        description_result = recognize_image(image)
        
        # Save image
        image_path = os.path.join('static', 'img', image.filename)
        image.seek(0)
        image.save(image_path)

        return render_template('recognize.html', captions=description_result.captions, image=url_for('static', filename='img/' + image.filename))
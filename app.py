from flask import Flask, render_template,request
from PIL import Image
import numpy as np
import tensorflow as tf
import os

app = Flask(__name__ ,static_folder='static')
app.debug = True


# predict function start 
def predictClass(imagePath):   
    model = tf.keras.models.load_model(r'C:\Users\Admin\OneDrive\Desktop\6th Sem\AiMl\Lab\Project\cancerDetection\cancerDetectionAiMl.h5')
    input_shape = (28, 28)
    image = Image.open(imagePath)
    image = image.resize((input_shape)) 
    image = np.array(image)  
    image = np.expand_dims(image, axis=0)
    predictions = model.predict(image)
    predicted_class = np.argmax(predictions)
    print('Predicted disease class:', predicted_class)
    return predicted_class

classes = {
    2:'bkl - benign keratosis-like lesions',
    4:'nv - melanocytic nevi',
    3:'df - dermatofibroma',
    6:'mel - melanoma ',
    5:'vasc - vascular lesions',
    1:'bcc - basal cell carcinoma',
    0:'akiec - Actinic keratoses'
    }


def diseaseName(classNumber):
    return classes[classNumber]


@app.route('/home', methods=['GET', 'POST'])
def detect_disease():
    if request.method == 'POST':
        image = request.files['image']
        filename = image.filename
        file_path = os.path.join('static/uploads', filename)
        image.save(file_path)
        classNumber = predictClass(file_path)
        pred = diseaseName(classNumber)
        return render_template('home.html', disease=pred)
    else:
        return render_template('home.html')

# form for taking image
# <form class="bg-grey" action="{{ url_for('detect_disease') }}" method="post" enctype="multipart/form-data">
#             <br>
#             <br>
#             <div class="centre">
            
#             <div class="imageUpload">
#                 <div class="centre blog-right centre">
#                     <h3>Upload A Photo To Detect</h3>
#                 </div>
#             <label for="formFileLg" class="form-label"></label>
#             <input id="formFileLg" class="form-control form-control-lg" type="file" name="image">
#             </div>

#             <div class="centre">
#             <input class="hero-btn red-btn bd-rd" style="margin-top:20px" type="submit" name="s1" value="Detect Disease">
#             </div>
# </form>

# predict function end 

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/submit_cancer_form', methods=['POST'])
def submit_cancer_form():
    # Retrieve form data from the request
    name = request.form.get('name')
    email = request.form.get('email')
    age = request.form.get('age')
    gender = request.form.get('gender')
    skin_image = request.files['skin-image']
    message = request.form.get('message')

    # Process the form data as needed
    # ...
    print(name,email,age,gender,message)

    # Return a response, such as a success message
    return 'Form submitted successfully!'

if __name__ == '__main__':
    app.run()

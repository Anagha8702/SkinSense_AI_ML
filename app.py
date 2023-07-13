from flask import Flask, render_template,request

app = Flask(__name__ ,static_folder='static')
app.debug = True

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

from flask import Flask, render_template, request
import os
from Main import CHECK

app = Flask(__name__)

# Define the upload folder
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None

    if request.method == 'POST':
        # Check if the file is present in the request
        if 'image_path' in request.files:
            # Get the file data
            image_file = request.files['image_path']
            # Save the file to a temporary location or process it directly
            image_path = save_file(image_file)
        else:
            return "No file provided"

        # Get the document type from the form
        document_type = request.form.get('document_type')

        result = CHECK(document_type, image_path)  # Capture the result

    return render_template('index.html', result=result)

def save_file(file):
    # Save the file to the upload folder and return the file path
    if file:
        filename = file.filename
        # Create the upload folder if it doesn't exist
        upload_folder = app.config['UPLOAD_FOLDER']
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)
        file_path = os.path.join(upload_folder, filename)
        file.save(file_path)
        return file_path
    else:
        return None

if __name__ == '__main__':
    app.run(debug=True)

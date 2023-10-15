import os
from PIL import Image
from flask import Flask, request, render_template

app = Flask(__name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/convert', methods=['POST'])
def convert():
    output_in = './pdf'

    # Check if the 'file' key is in the request.files dictionary
    if 'file' not in request.files:
        return "No file part"

    files = request.files.getlist('file')

    # Iterate through the list of uploaded files
    for file in files:
        # If the file is valid, convert it to PDF and save with the source file name
        if file and allowed_file(file.filename):
            image = Image.open(file)
            image_converted = image.convert('RGB')
            # Save the output PDF with the source file name
            output_filename = os.path.join(output_in, '{}.pdf'.format(os.path.splitext(file.filename)[0]))
            image_converted.save(output_filename)
        else:
            return "Invalid file format"

    return "Conversion successful!"


if __name__ == '__main__':
    app.run(debug=True)

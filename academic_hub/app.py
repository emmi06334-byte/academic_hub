# from flask import Flask, render_template, request, redirect, send_from_directory
# import os

# app = Flask(__name__)
# UPLOAD_FOLDER = 'uploads'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# if not os.path.exists(UPLOAD_FOLDER):
#     os.makedirs(UPLOAD_FOLDER)

# @app.route('/')
# def index():
#     files = []
#     for filename in os.listdir(UPLOAD_FOLDER):
#         category = filename.split('_')[0]  # e.g., notes_filename.pdf
#         files.append({'filename': filename, 'category': category})
#     return render_template('index.html', files=files)

# @app.route('/upload', methods=['POST'])
# def upload():
#     title = request.form['title']
#     category = request.form['category']
#     file = request.files['file']
#     filename = f"{category}_{title}_{file.filename}"
#     file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#     return redirect('/')

# @app.route('/download/<filename>')
# def download_file(filename):
#     return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

# @app.route('/delete/<filename>')
# def delete_file(filename):
#     os.remove(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#     return redirect('/')

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, render_template, request, redirect, send_from_directory
import os

app = Flask(__name__)

# Folder to store uploaded files
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create the uploads folder if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Home route: show all files
@app.route('/')
def index():
    files = []
    for filename in os.listdir(UPLOAD_FOLDER):
        category = filename.split('_')[0]  # e.g., notes_filename.pdf
        files.append({'filename': filename, 'category': category})
    return render_template('index.html', files=files)

# Upload route
@app.route('/upload', methods=['POST'])
def upload():
    title = request.form['title']
    category = request.form['category']
    file = request.files['file']
    if file:
        filename = f"{category}_{title}_{file.filename}"
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return redirect('/')

# Download route
@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

# Delete route
@app.route('/delete/<filename>')
def delete_file(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(file_path):
        os.remove(file_path)
    return redirect('/')

# Filter by category route
@app.route('/category/<category>')
def filter_category(category):
    files = []
    for filename in os.listdir(UPLOAD_FOLDER):
        file_category = filename.split('_')[0]
        if file_category == category:
            files.append({'filename': filename, 'category': file_category})
    return render_template('index.html', files=files)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
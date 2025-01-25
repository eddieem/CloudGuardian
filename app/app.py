import os
from flask import Flask, request, render_template, redirect, url_for
from .security_analyzer import analyze_configuration  # Use relative import

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

# Ensure the uploads directory exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    
    if file and file.filename.endswith('.json'):
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        
        report = analyze_configuration(filepath)
        
        # Optionally delete the file after processing
        os.remove(filepath)
        
        return render_template('report.html', report=report)
    else:
        return redirect(request.url)

if __name__ == '__main__':
    app.run(debug=True)


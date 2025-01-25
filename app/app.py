import os
from flask import Blueprint, Flask, request, render_template, redirect, url_for
from .security_analyzer import analyze_configuration

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    
    if file and file.filename.endswith('.json'):
        filepath = os.path.join(Flask.current_app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        
        report = analyze_configuration(filepath)
        
        # Optionally delete the file after processing
        os.remove(filepath)
        
        return render_template('report.html', report=report)
    else:
        return redirect(request.url)

if __name__ == '__main__':
    app.run(debug=True)

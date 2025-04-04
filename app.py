from flask import Flask, render_template, request, jsonify, send_from_directory
import os
from werkzeug.utils import secure_filename

app = Flask(__name__, 
    static_url_path='/static',
    static_folder='static',
    template_folder='templates'
)

# Configure upload folder
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024  # 10MB max file size

# Ensure upload directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    try:
        return render_template('index.html')
    except Exception as e:
        print(f"Error rendering template: {e}")
        return "Error loading page", 500

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/verify_document', methods=['POST'])
def verify_document():
    if 'document' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['document']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Here you would add your blockchain verification logic
        # For now, we'll just return a success message
        return jsonify({
            'success': True,
            'message': 'Document verified successfully',
            'filename': filename
        })
    
    return jsonify({'error': 'Invalid file type'}), 400

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 
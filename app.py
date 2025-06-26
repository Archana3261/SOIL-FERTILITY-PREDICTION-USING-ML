from flask import Flask, request, render_template
from naivebayes import analyze
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    
    if file:
        stream = io.TextIOWrapper(file.stream)
        result = analyze(stream)
        return render_template('index.html', result=result)
    
    return "Error processing the file"

if __name__ == '__main__':
    app.run(debug=True)


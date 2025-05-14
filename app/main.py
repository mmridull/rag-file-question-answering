
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
from rag import process_file, answer_query

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'app/uploads'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Home route
@app.route('/', methods=['GET', 'POST'])
def index():
    answer = ""
    if request.method == 'POST':
        if 'file' in request.files:
            uploaded_file = request.files['file']
            filename = secure_filename(uploaded_file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            uploaded_file.save(filepath)
            process_file(filepath)
        elif 'question' in request.form:
            question = request.form['question']
            answer = answer_query(question)
    return render_template('index.html', answer=answer)

if __name__ == '__main__':
    app.run(debug=True)

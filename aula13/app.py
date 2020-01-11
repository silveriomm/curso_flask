import os
from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'upload')

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
	file = request.files['imagen']
	savePath = os.path.join(UPLOAD_FOLDER, secure_filename(file.filename))
	file.save(savePath)
	foto = savePath
	print(foto)
	return render_template('upload.html', foto=foto)

if __name__=='__main__':
	app.run(debug=True)
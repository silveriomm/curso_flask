from flask import Flask, render_template, request, abort, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('login.html')	
	
@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		if request.form['username'] == 'admin' and request.form['password'] == 'admin':
			return redirect(url_for('sucesso'))
		else:
			abort(401)			
	else:
		abort(403)	

@app.route('/sucesso')
def sucesso():
	return '<h2>Sucesso!</h2>'

if __name__=='__main__':
	app.run(debug=True)
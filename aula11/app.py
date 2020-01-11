from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')
	
@app.route('/setcockie', methods=['GET', 'POST'])
def setcockie():
	resp = make_response(render_template('setcockie.html'))	
	if request.method == 'POST':
		dados = request.form['c']
		resp.set_cookie("testCockie", dados)
	
	return resp
	
@app.route('/getcockie')
def getcockie():
	cockieName = request.cookies.get('testCockie')
	return '<h1>O valor do cockie é: {}</h1>'.format(cockieName)

if __name__=='__main__':
	app.run(debug=True)
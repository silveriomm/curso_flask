from flask import Flask, render_template, request

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
	nome = request.form['nome']
	senha = request.form['senha']
	if request.method == 'POST':
		return 'Nome: %s<br> Senha: %s' % (nome,senha)
	return 'Ok POST'

if __name__=='__main__':
	app.run(debug=True)
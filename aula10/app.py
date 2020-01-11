from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/nota')
def nota():
	return render_template('nota.html')

@app.route('/calculo', methods=['POST'])
def calculo():
	total = sum([int(v) for v in request.form.to_dict().values()])
	return render_template('calculo.html', total=total)

if __name__=='__main__':
	app.run(debug=True)
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Index</h1>'

def teste():
    return '<h2>Teste</h2>'

def teste2():
    return '<h2>Teste2</h2>'

app.add_url_rule('/teste', 'teste', teste)
app.add_url_rule('/teste2', 'teste2', teste2)

if __name__=='__main__':
    app.run(debug=True)
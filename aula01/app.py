from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Index</h1>'
    
@app.route('/teste')
def teste():
    return '<h1>Teste</h1>'
    
if __name__=='__main__':
    app.run()
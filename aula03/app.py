from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/hello')
@app.route('/hello/<nome>')
def hello(nome=''):
    return '<h1>Hello {}</h1>'.format(nome)

@app.route('/blog')
@app.route('/blog/<int:post_id>')
def blog(post_id=-1):
    if post_id >= 0:
       return '<h2>Blog info: {}</h2>'.format(post_id)
    else:
       return '<h2>Blog Todo</h2>'

if __name__=='__main__':
    app.run()
from flask import Flask
from flask import request
app=Flask(__name__)
@app.route('/hi')
def hello():
    return 'hi'
@app.route('/')
def index():
    return 'hello world'
@app.route('/test')
def test():
    a=5+6
    return 'this value is {}'.format(a)
@app.route('/name')
def name():
    data=request.args.get('x')
    return 'this is my input from my url {}'.format(data)
if __name__ =='__main__':
    app.run(debug=True)
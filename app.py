from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world! This is just a demo.'

@app.route('/test2')
def test2():
    return 'This is a test!'

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')
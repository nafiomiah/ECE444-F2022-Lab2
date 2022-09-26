from flask import Flask
app = Flask(__name__)

@app.route('/')
def simple_hello_world():
    page_title = '<h1>Hello World!</h1>'
    return page_title

@app.route('/helloname/<name>')
def hello_name(name):
    page_title = '<h1> Hello, {}! </h1>'.format(name.capitalize())
    return page_title


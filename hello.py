from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def simple_hello_world():
    # page_title = '<h1>Hello World!</h1>'
    # return page_title
    return render_template('index.html')

@app.route('/helloname/<input_name>')
def hello_name(input_name):
    # page_title = '<h1> Hello, {}! </h1>'.format(name.capitalize())
    # return page_title
    return render_template('user.html',name = input_name)




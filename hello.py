from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/')
def simple_hello_world():
    # page_title = '<h1>Hello World!</h1>'
    # return page_title
    return render_template('index.html', current_time = datetime.utcnow())

@app.route('/helloname/<input_name>')
def hello_name(input_name):
    # page_title = '<h1> Hello, {}! </h1>'.format(name.capitalize())
    # return page_title
    return render_template('user.html',name = input_name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def unhandled_exception(e):
    return render_template('500.html'), 500




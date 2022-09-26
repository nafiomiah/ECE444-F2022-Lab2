from flask import Flask
app = Flask(__name__)

@app.route('/')
def simple_hello_world():
    page_title = '<h1>Hello World!</h1>'
    return page_title


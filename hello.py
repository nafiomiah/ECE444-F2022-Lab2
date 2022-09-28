from flask import Flask, render_template, redirect, session, flash
from flask_bootstrap import Bootstrap
# from flask_moment import Moment
# from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
bootstrap = Bootstrap(app)
# moment = Moment(app)
app.config['SECRET_KEY'] = 'qikgu'

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators = [DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index_page(): 
    nf = NameForm()
    if nf.validate_on_submit():
        prev_name = session.get('name')
        if prev_name is not None and prev_name != nf.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = nf.name.data
        return redirect("/")
    return render_template('index.html', form = nf, name = session.get('name'))

# @app.route('/helloname/<input_name>')
# def hello_name(input_name):
#     # page_title = '<h1> Hello, {}! </h1>'.format(name.capitalize())
#     # return page_title
#     return render_template('user.html',name = input_name)

# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html'), 404

# @app.errorhandler(500)
# def unhandled_exception(e):
#     return render_template('500.html'), 500




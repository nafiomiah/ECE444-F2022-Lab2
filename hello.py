from flask import Flask, render_template, redirect, session, flash
from flask_bootstrap import Bootstrap
# from flask_moment import Moment
# from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email


app = Flask(__name__)
bootstrap = Bootstrap(app)
# moment = Moment(app)
app.config['SECRET_KEY'] = 'abcdef'


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators = [DataRequired()])
    email = EmailField('What is your UofT Email address?', validators = [DataRequired(), Email()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index_page(): 
    nf = NameForm()
    if nf.validate_on_submit():
        prev_name = session.get('name')
        if prev_name is not None and prev_name != nf.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = nf.name.data

        prev_email = session.get('email')
        if prev_email is not None and prev_email != nf.email.data:
            flash('Looks like you have changed your email!')
        session['email'] = nf.email.data

        if 'utoronto' in nf.email.data:
            session['isUofTEmail'] = True
        elif 'utoronto' not in nf.email.data:
            session['isUofTEmail'] = False

        return redirect("/")
    return render_template('index.html', form = nf, name = session.get('name'), email = session.get('email'), isUofTEmail = session.get('isUofTEmail'))


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




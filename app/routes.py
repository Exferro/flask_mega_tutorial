from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


@app.route('/')
def root():
    return 'Hello, root!'


@app.route('/index')
def index():
    user = {'username': 'Aleksei'}

    posts = [
        {
            'author': {'username': 'Sanya'},
            'body': 'Beautiful day in Dolgoprudny!'
        },
        {
            'author': {'username': 'Liolik'},
            'body': 'The Avengers movie was not cool at all!'
        }
    ]
    return render_template('index.html', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data}, remember_me={form.remember_me.data}')
        return redirect(url_for('index'))

    return render_template('login.html', title='Sign in', form=form)

from wsgiref import validate
from flask import render_template, redirect,url_for
from shop.forms import LoginForm
from shop.models import User , Tweet

def index():
    name = {'username':'root'}
    posts = [
        {
            'author':{'username':'root'},
            'body':"Hi I'm root!"
        },
        {
            'author':{'username':'test'},
            'body':"Hi I'm test!"
        },
    ]
    return render_template('index.html',name = name , posts = posts)

def login():
    form = LoginForm(meta={'csrf': False})
    if form.validate_on_submit():
        msg = "username={}, password={}, remember_me={}".format(
            form.username.data,
            form.password.data,
            form.remember_me.data
        )
        print(msg)
        return redirect(url_for('index'))
    return render_template('login.html',form = form)
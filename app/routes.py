from flask import render_template 
from app import app 

@app.route('/')
@app.route('/index')

def index():
    user = {'username':'Piyush'}
    posts = [
        {
            'author': {'username' : 'John'},
            'body' : 'Beautiful day in Portland!'
        },
        {
            'author':{'username' : 'Wick'},
            'body' : 'You made a big mistake!'
        }
    ]
    return render_template('index.html', title = 'Home', user=user, posts = posts)
from flask import Flask, request, render_template,redirect,session
from flask_session import Session
import hashlib
import string
import sqlite3

app = Flask(__name__)


#This section of code is used to call the index page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')



if __name__ == "__main__":
    app.run(debug=True)
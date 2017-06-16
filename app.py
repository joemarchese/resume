from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dev/')
def dev():
    return render_template('dev.html')

@app.route('/about/')
def about():
    return ''

if __name__ == '__main__':
    app.run()

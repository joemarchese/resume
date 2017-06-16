from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def resume():
    return render_template('resume.html')

@app.route('/dev/')
def dev():
    return render_template('dev.html')

@app.route('/about/')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run()

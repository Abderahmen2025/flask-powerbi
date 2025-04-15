
from app import app
from flask import render_template

@app.route('/')
def home():
    return render_template('page-profile.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/table')
def table():
    return render_template('table-basic.html')

@app.route('/descriptive')
def descriptive():
    return render_template('descriptive.html')

@app.route('/predictive')
def predictive():
    return render_template('page-blank.html')

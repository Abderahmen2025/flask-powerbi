from flask import render_template, request
from app import app
import numpy as np
import pandas as pd
import pickle
import os

model_path = os.path.join(os.path.dirname(__file__), 'model.pkl')
model = pickle.load(open(model_path, 'rb'))

@app.route('/')
def home():
    return render_template('dashboard.html')

@app.route('/table')
def table():
    return render_template('table.html')

@app.route('/descriptive')
def descriptive():
    return render_template('descriptive.html')

@app.route('/predictive', methods=["GET", "POST"])
def predictive():
    prediction = None
    if request.method == "POST":
        data = [float(request.form[f"feature{i}"]) for i in range(1, 5)]
        prediction = model.predict([data])[0]
    return render_template('predictive.html', prediction=prediction)
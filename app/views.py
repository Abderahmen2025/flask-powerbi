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


from flask import render_template, request
import pickle
import numpy as np

# Charger le modèle une seule fois
model = pickle.load(open("app/model.pkl", "rb"))

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    prediction = None
    if request.method == 'POST':
        try:
            age = int(request.form['age'])
            km = int(request.form['km'])
            vehicule = request.form['vehicule']

            # Encodage du type de véhicule (exemple simplifié)
            vehicule_code = {'citadine': 0, 'SUV': 1, 'utilitaire': 2}.get(vehicule, 0)

            # Création du vecteur de caractéristiques
            input_data = np.array([[age, km, vehicule_code]])
            prediction = model.predict(input_data)[0]
            # Interprétation de la sortie du modèle
            if prediction == 0:
                prediction = "✅ Risque faible"
            elif prediction == 1:
                prediction = "⚠️ Risque modéré"
            else:
                prediction = "❌ Risque élevé"

        except Exception as e:
            prediction = f"Erreur lors de la prédiction : {e}"

    return render_template("page-blank.html", prediction=prediction)

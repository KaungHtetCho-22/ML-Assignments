from flask import Flask, render_template, request, flash
import pickle
import numpy as np
import os
from model import Normal

app = Flask(__name__)

with open(os.path.join('models/', 'car_price_old.model'), 'rb') as file:
    old_loaded_model = pickle.load(file)


with open(os.path.join('models/', 'car_price_new.model'), 'rb') as file:
    new_loaded_model = pickle.load(file)

old_model = old_loaded_model['model']
old_scaler = old_loaded_model['scaler']
old_max_power_default = old_loaded_model.get('max_power')  
old_mileage_default = old_loaded_model.get('mileage')  
old_year_default = old_loaded_model.get('year')  

new_model = new_loaded_model['model']
new_scaler = new_loaded_model['scaler']
new_max_power_default = new_loaded_model.get('max_power')
new_mileage_default = new_loaded_model.get('mileage')
new_year_default = new_loaded_model.get('year')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict_new')
def predict_new():
    return render_template(
        'predict_new.html',
        max_power_default=new_max_power_default,
        mileage_default=new_mileage_default,
        year_default=new_year_default
    )

@app.route('/predict_old')
def predict_old():
    return render_template(
        'predict_old.html',
        max_power_default=old_max_power_default,
        mileage_default=old_mileage_default,
        year_default=old_year_default
    )


@app.route('/process-data-old', methods=['POST'])
def process_data_old():
    if request.method == 'POST':
        max_power = request.form.get('max_power', old_max_power_default)
        mileage = request.form.get('mileage', old_mileage_default)
        year = request.form.get('year', old_year_default)

        max_power = float(max_power) if max_power else old_max_power_default
        mileage = float(mileage) if mileage else old_mileage_default
        year = int(year) if year else old_year_default

        result = str(int(prediction_old(max_power, mileage, year)[0]))
        return result

# Prediction function for old model
def prediction_old(max_power, mileage, year):
    sample = np.array([[max_power, mileage, year]])
    sample_scaled = old_scaler.transform(sample)
    result = np.exp(old_model.predict(sample_scaled))
    return result

@app.route('/process-data-new', methods=['POST'])
def process_data_new():
    if request.method == 'POST':
        max_power = request.form.get('max_power', new_max_power_default)
        mileage = request.form.get('mileage', new_mileage_default)
        year = request.form.get('year', new_year_default)

        max_power = float(max_power) if max_power else new_max_power_default
        mileage = float(mileage) if mileage else new_mileage_default
        year = int(year) if year else new_year_default

        result = str(int(prediction_new(max_power, mileage, year)[0]))
        return result

# Prediction function for new model
def prediction_new(max_power, mileage, year):
    sample = np.array([[max_power, mileage, year]])
    sample_scaled = new_scaler.transform(sample)
    intercept = np.ones((sample_scaled.shape[0], 1))
    sample_scaled = np.concatenate((intercept, sample_scaled), axis=1)
    result = np.exp(new_model.predict(sample_scaled))
    return result

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=7000)

from flask import Flask, render_template, request
import pickle
import numpy as np
import os
from model import RidgeLogisticRegression, RidgePenalty

app = Flask(__name__)

# Load best WITH Ridge model
with open(os.path.join('models/', 'car_price_with_ridge.model'), 'rb') as file:
    ridge_loaded_model = pickle.load(file)

# Load best WITHOUT Ridge model
with open(os.path.join('models/', 'car_price_without_ridge.model'), 'rb') as file:
    noridge_loaded_model = pickle.load(file)

# Extract model components
ridge_model             = ridge_loaded_model['model']
ridge_scaler            = ridge_loaded_model['scaler']
ridge_max_power_default = ridge_loaded_model.get('max_power')
ridge_mileage_default   = ridge_loaded_model.get('mileage')
ridge_year_default      = ridge_loaded_model.get('year')
ridge_engine_default    = ridge_loaded_model.get('engine')
ridge_class_bins        = ridge_loaded_model.get('classes')

noridge_model             = noridge_loaded_model['model']
noridge_scaler            = noridge_loaded_model['scaler']
noridge_max_power_default = noridge_loaded_model.get('max_power')
noridge_mileage_default   = noridge_loaded_model.get('mileage')
noridge_year_default      = noridge_loaded_model.get('year')
noridge_engine_default    = noridge_loaded_model.get('engine')
noridge_class_bins        = noridge_loaded_model.get('classes')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict_with_ridge')
def predict_with_ridge():
    return render_template(
        'predict_with_ridge.html',
        max_power_default=ridge_max_power_default,
        mileage_default=ridge_mileage_default,
        year_default=ridge_year_default,
        engine_default=ridge_engine_default
    )

@app.route('/predict_without_ridge')
def predict_without_ridge():
    return render_template(
        'predict_without_ridge.html',
        max_power_default=noridge_max_power_default,
        mileage_default=noridge_mileage_default,
        year_default=noridge_year_default,
        engine_default=noridge_engine_default
    )


@app.route('/process-data-with-ridge', methods=['POST'])
def process_data_with_ridge():
    max_power = float(request.form.get('max_power', ridge_max_power_default))
    mileage   = float(request.form.get('mileage', ridge_mileage_default))
    year      = int(request.form.get('year', ridge_year_default))
    engine    = int(request.form.get('engine', ridge_engine_default))
    result = predict_with_ridge_result(max_power, mileage, year, engine)
    return result

@app.route('/process-data-without-ridge', methods=['POST'])
def process_data_without_ridge():
    max_power = float(request.form.get('max_power', noridge_max_power_default))
    mileage   = float(request.form.get('mileage', noridge_mileage_default))
    year      = int(request.form.get('year', noridge_year_default))
    engine    = int(request.form.get('engine', noridge_engine_default))
    result = predict_without_ridge_result(max_power, mileage, year, engine)
    return result

def predict_with_ridge_result(max_power, mileage, year, engine):
    sample        = np.array([[max_power, mileage, year, engine]])
    sample_scaled = ridge_scaler.transform(sample)
    intercept     = np.ones((sample_scaled.shape[0], 1))
    sample_scaled = np.concatenate((intercept, sample_scaled), axis=1)
    predicted_class = int(ridge_model.predict(sample_scaled)[0])
    lower = ridge_class_bins[predicted_class]
    upper = ridge_class_bins[predicted_class + 1]
    if np.isinf(upper):
        return f"${int(lower):,}+"
    else:
        return f"${int(lower):,} - ${int(upper):,}"

def predict_without_ridge_result(max_power, mileage, year, engine):
    sample        = np.array([[max_power, mileage, year, engine]])
    sample_scaled = noridge_scaler.transform(sample)
    intercept     = np.ones((sample_scaled.shape[0], 1))
    sample_scaled = np.concatenate((intercept, sample_scaled), axis=1)
    predicted_class = int(noridge_model.predict(sample_scaled)[0])
    lower = noridge_class_bins[predicted_class]
    upper = noridge_class_bins[predicted_class + 1]
    if np.isinf(upper):
        return f"${int(lower):,}+"
    else:
        return f"${int(lower):,} - ${int(upper):,}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=7000)
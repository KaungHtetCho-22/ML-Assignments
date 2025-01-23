# app.py
from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the dictionary from the file
with open('A1_KaungHtetCho/models/car_price.model', 'rb') as file:
    loaded_model = pickle.load(file)

# Access individual components
model = loaded_model['model']
scaler = loaded_model['scaler']
max_power__default = loaded_model['max_power']
mileage_default = loaded_model['mileage']
year_default = loaded_model['year']

print("Model and associated values have been loaded!")

@app.route('/')
def index():
    return render_template(
        'index.html',
        max_power_default=max_power__default,
        mileage_default=mileage_default,
        year_default=year_default
    )

@app.route('/predict', methods=['POST'])
def predict():
    max_power = request.form.get('max_power', max_power__default)
    mileage = request.form.get('mileage', mileage_default)
    year = request.form.get('year', year_default)

    # Convert input values to floats
    try:
        max_power = float(max_power)
    except ValueError:
        max_power = max_power__default

    try:
        mileage = float(mileage)
    except ValueError:
        mileage = mileage_default

    try:
        year = float(year)
    except ValueError:
        year = year_default

    # Predict car price
    predicted_price = int(prediction(max_power, mileage, year)[0])

    return render_template('predict.html', predicted_price=predicted_price)

# Prediction function to predict car price
def prediction(max_power, mileage, year):
    sample = np.array([[max_power, mileage, year]])
    sample_scaled = scaler.transform(sample)
    result = np.exp(model.predict(sample_scaled))
    return result

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

filename = 'model/car_price.model'
loaded_data = pickle.load(open(filename, 'rb'))

# Separating the values in the model file into variables for easy access
model = loaded_data['model']
scaler = loaded_data['scaler']
name_map = loaded_data['name_map']
engine_default = loaded_data['engine_default']
mileage_default = loaded_data['mileage_default']

# The home page containing a link to the prediction page
@app.route('/')
def index():
    return render_template('index.html')

# The prediction page
@app.route('/predict')
def predict():
    return render_template('predict.html')

# The route to calculate the prediction result but not accessed by users
@app.route('/process-data', methods = ['POST'])
def process_data():
    if request.method == 'POST':
        # Getting the values required for prediction
        brand_name = request.form.get('name')
        name = name_map.get(brand_name,'32')
        engine = request.form.get('engine', engine_default)
        mileage = request.form.get('mileage', mileage_default)

        # Convert engine and mileage to float only if they are not empty strings
        if engine:
            engine = float(engine)
        else:
            engine = engine_default  # Set a default value if engine is empty

        if mileage:
            mileage = float(mileage)
        else:
            mileage = mileage_default # Set a default value if mileage is empty

        # Calling the prediction function, coverting the result to int for user experience and then to string
        # to display on the website
        result = str(int(prediction(name,engine,mileage)[0]))

        return result

# Prediction function to predit car price
def prediction(name,engine,mileage):
    # Put the user input into an array
    sample = np.array([[name,engine,mileage]])

    # Scale the input data using the trained scaler
    sample_scaled = scaler.transform(sample)

    # Predict the car price using the trained model
    result = np.exp(model.predict(sample_scaled))

    return result

port_number = 8000

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port_number)
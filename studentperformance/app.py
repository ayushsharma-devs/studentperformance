from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('model.pkl')

@app.route('/')
def home():
    # Set default selections
    return render_template('index.html', result=None, gender='0', prep='0')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form values
    gender = request.form['gender']
    prep = request.form['prep']

    # Make prediction
    data = np.array([[int(gender), int(prep)]])
    prediction = model.predict(data)[0]
    result = "Pass ✅" if prediction == 1 else "Fail ❌"

    # Pass form values back to retain selection
    return render_template('index.html', result=result, gender=gender, prep=prep)

if __name__ == '__main__':
    app.run(debug=True)

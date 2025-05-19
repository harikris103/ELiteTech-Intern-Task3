from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

model = joblib.load("student_model.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    df = pd.DataFrame([data])
    pred = model.predict(df)[0]
    result = "✅ PASS" if pred == 1 else "❌ FAIL"
    return jsonify({"prediction": result})

if __name__ == '__main__':
    app.run(debug=True)

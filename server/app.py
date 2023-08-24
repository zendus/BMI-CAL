from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/api/endpoint', methods=['POST'])
def handle_post_request():
    try:
        data = request.json  # Assuming the request data is in JSON format
        # You can process the data here and return a response
        # BMI (BODY MASS INDEX) = WEIGHT(KG) / HEIGHT SQUARED
        user_height = float(data["height"])
        user_weight = float(data["weight"])
        bmi = round(user_weight / user_height ** 2, 2)
        status = ""

        if bmi < 18.5:
            status = "UNDERWEIGHT"
        elif bmi >= 18.5 and bmi <= 24.9:
            status = "NORMAL"
        elif bmi >= 25 and bmi <= 29.9:
            status = "OVERWEIGHT"
        else:
            status = "OBESE"

        response = {"bmi": bmi, "status": status}
        print(bmi, status)
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)

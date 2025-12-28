from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    return jsonify({
        "approval_probability": 0.72,
        "risk_score": 35
    })

if __name__ == '__main__':
    app.run(port=8000, debug=True)

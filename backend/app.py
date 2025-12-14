from flask import Flask, request, jsonify
from src.models.predict import predict_species

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    features = [
        data["sepal_length"],
        data["sepal_width"],
        data["petal_length"],
        data["petal_width"],
    ]

    prediction = predict_species(features)

    return jsonify({"prediction": prediction})


if __name__ == "__main__":
    app.run(debug=True)

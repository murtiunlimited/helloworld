import pickle
import numpy as np

def load_model(path: str):
    with open(path, "rb") as f:
        return pickle.load(f)

def predict_species(features: list):
    model = load_model("models/iris_nb.pkl")
    features = np.array(features).reshape(1, -1)
    return model.predict(features)[0]

import pickle

def save_model(model, path: str):
    with open(path, "wb") as f:
        pickle.dump(model, f)

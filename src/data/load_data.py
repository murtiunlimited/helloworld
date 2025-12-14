import pandas as pd

def load_iris_data(path: str):
    """
    Loads iris dataset from CSV.
    """
    return pd.read_csv(path)

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

from src.data.load_data import load_iris_data
from src.utils.save_model import save_model

def train_model():
    # Load data
    iris = load_iris_data("data/iris.csv")

    # Features and target
    X = iris[['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width']]
    y = iris['Species']

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42
    )

    # Train model
    model = GaussianNB()
    model.fit(X_train, y_train)

    # Evaluate
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    print("Accuracy Score:", accuracy)

    # Save model
    save_model(model, "models/iris_nb.pkl")

    return model


if __name__ == "__main__":
    train_model()

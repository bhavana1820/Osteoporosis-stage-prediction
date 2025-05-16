import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sklearn.metrics import classification_report
from src.data_preprocessing import load_and_preprocess_data
import joblib


for gender in ["men", "women"]:
    print(f"\n--- Evaluating Model for {gender.capitalize()} ---")

    # Load data
    X_train, X_test, y_train, y_test, _ = load_and_preprocess_data(gender)

    # Load model
    model = joblib.load(f"model_{gender}.pkl")

    # Predictions
    y_pred = model.predict(X_test)

    # Report
    print(classification_report(y_test, y_pred, target_names=["Normal", "Osteopenia", "Osteoporosis", "Severe Osteoporosis"]))

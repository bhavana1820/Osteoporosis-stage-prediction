import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sklearn.ensemble import RandomForestClassifier
import joblib
from src.data_preprocessing import load_and_preprocess_data

for gender in ["men", "women"]:
    X_train, X_test, y_train, y_test, _ = load_and_preprocess_data(gender)

    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    joblib.dump(model, f"model_{gender}.pkl")
    print(f"{gender.capitalize()} model trained and saved.")

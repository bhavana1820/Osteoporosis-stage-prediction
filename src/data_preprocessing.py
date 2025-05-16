import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

def load_and_preprocess_data(gender):
    df = pd.read_csv(f"dataset/osteoporosis_data_{gender}.csv")

    X = df.drop("Stage", axis=1)
    y = df["Stage"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42
    )

    return X_train, X_test, y_train, y_test, scaler

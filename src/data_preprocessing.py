

# src/data_preprocessing.py
# import pandas as pd
# from sklearn.preprocessing import StandardScaler
# from sklearn.model_selection import train_test_split

# scaler = StandardScaler()

# def load_and_preprocess_data(gender="men"):
#     file_path = f"dataset/osteoporosis_data_{gender}.csv"
#     df = pd.read_csv(file_path)

#     X = df.drop("Stage", axis=1)
#     y = df["Stage"]

#     X_scaled = scaler.fit_transform(X)

#     X_train, X_test, y_train, y_test = train_test_split(
#         X_scaled, y, test_size=0.2, random_state=42
#     )

#     return X_train, X_test, y_train, y_test, scaler

# def get_scaler():
#     return scaler



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

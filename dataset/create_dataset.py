
# dataset/generate_datasets.py
# import pandas as pd
# import numpy as np

# def generate_dataset(gender="men"):
#     np.random.seed(42)
#     n_samples = 500

#     age = np.random.randint(40, 90, size=n_samples)
#     bmi = np.random.normal(25, 5, size=n_samples)

#     if gender == "men":
#         testosterone = np.random.normal(500, 100, size=n_samples)
#     else:  # women
#         testosterone = np.random.normal(50, 20, size=n_samples)  # lower values

#     vitamin_d = np.random.normal(25, 10, size=n_samples)
#     calcium = np.random.normal(800, 200, size=n_samples)
#     alcohol = np.random.randint(0, 10, size=n_samples)
#     smoking = np.random.choice([0, 1], size=n_samples)
#     physical_activity = np.random.randint(1, 6, size=n_samples)

#     labels = []
#     for a, v, t in zip(age, vitamin_d, testosterone):
#         if a > 70 or v < 15 or t < (300 if gender == "men" else 30):
#             labels.append(2)
#         elif a > 60 or v < 20 or t < (400 if gender == "men" else 40):
#             labels.append(1)
#         else:
#             labels.append(0)

#     df = pd.DataFrame({
#         "Age": age,
#         "BMI": bmi,
#         "Testosterone": testosterone,
#         "VitaminD": vitamin_d,
#         "CalciumIntake": calcium,
#         "AlcoholIntake": alcohol,
#         "Smoking": smoking,
#         "PhysicalActivity": physical_activity,
#         "Stage": labels
#     })

#     df.to_csv(f"dataset/osteoporosis_data_{gender}.csv", index=False)
#     print(f"{gender.capitalize()} dataset created successfully.")

# generate_dataset("men")
# generate_dataset("women")



import pandas as pd
import numpy as np
from collections import Counter
import os

def generate_data(gender="men", n_samples=500):
    np.random.seed(42)

    age = np.random.randint(40, 90, size=n_samples)
    bmi = np.random.normal(25, 5, size=n_samples)
    
    # Testosterone range differs by gender
    testosterone = np.random.normal(500, 100, size=n_samples) if gender == "men" else np.random.normal(40, 10, size=n_samples)

    vitamin_d = np.random.normal(25, 10, size=n_samples)
    calcium = np.random.normal(800, 200, size=n_samples)
    alcohol = np.random.randint(0, 10, size=n_samples)
    smoking = np.random.choice([0, 1], size=n_samples)
    physical_activity = np.random.randint(1, 6, size=n_samples)

    labels = []
    for a, v, t in zip(age, vitamin_d, testosterone):
        if gender == "men":
            if a > 80 or (v < 8 and t < 250):
                labels.append(3)
            elif a > 70 or v < 15 or t < 300:
                labels.append(2)
            elif a > 60 or v < 20 or t < 400:
                labels.append(1)
            else:
                labels.append(0)
        else:  # women
            if a > 80 or (v < 8 and t < 20):
                labels.append(3)
            elif a > 70 or v < 15 or t < 30:
                labels.append(2)
            elif a > 60 or v < 20 or t < 40:
                labels.append(1)
            else:
                labels.append(0)

    print(f"Stage distribution ({gender}):", Counter(labels))

    df = pd.DataFrame({
        "Age": age,
        "BMI": bmi,
        "Testosterone": testosterone,
        "VitaminD": vitamin_d,
        "CalciumIntake": calcium,
        "AlcoholIntake": alcohol,
        "Smoking": smoking,
        "PhysicalActivity": physical_activity,
        "Stage": labels
    })

    # Create dataset directory if not exists
    os.makedirs("dataset", exist_ok=True)

    filename = f"dataset/osteoporosis_data_{gender}.csv"
    df.to_csv(filename, index=False)
    print(f"{gender.capitalize()} dataset saved as {filename}.")

# Generate both datasets
generate_data("men")
generate_data("women")

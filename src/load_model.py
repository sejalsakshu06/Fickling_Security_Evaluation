import fickling

fickling.hook.activate_safe_ml_environment(
    also_allow=[
        "sklearn.linear_model._base"
    ]
)

import pickle
import pandas as pd

# Load the saved model
with open("house_model.pkl", "rb") as file:
    model = pickle.load(file)

print("Model loaded successfully!")

# Create new house data with the same feature names used during training
houses = pd.DataFrame([
    [1500, 3, 2, 7],
    [1000, 2, 2, 12],
    [2000, 4, 3, 5]
], columns=["area_sqft", "bedrooms", "bathrooms", "age_years"])

# Make predictions
predictions = model.predict(houses)

# Display predictions
for i, prediction in enumerate(predictions):
    print(f"House {i + 1} predicted price: {prediction:.2f} lakh")
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import pickle

# 1. Load house data
data = pd.read_csv("house_data.csv")

# 2. Separate inputs and target
X = data[["area_sqft", "bedrooms", "bathrooms", "age_years"]]
y = data["price_lakh"]

# 3. Train the model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

# 4. Check predictions on the training data
predictions = model.predict(X)
error = mean_absolute_error(y, predictions)

print("Model trained successfully.")
print(f"Mean Absolute Error: {error:.2f} lakh")

# 5. Test a few normal predictions
test_houses = pd.DataFrame([
    [1500, 3, 2, 7],
    [2000, 4, 3, 5],
    [1000, 2, 2, 12]
], columns=["area_sqft", "bedrooms", "bathrooms", "age_years"])

test_predictions = model.predict(test_houses)

print("\nNormal predictions:")
for house, prediction in zip(test_houses.values, test_predictions):
    print(
        f"{house[0]} sqft, {house[1]} bedrooms, "
        f"{house[2]} bathrooms, {house[3]} years old"
        f" -> {prediction:.2f} lakh"
    )

# 6. Save the model as a Pickle file
with open("house_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("\nSaved model: house_model.pkl")
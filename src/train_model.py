import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# 1. Load our house dataset
data = pd.read_csv("house_data.csv")

# 2. Separate inputs and output
X = data[["area_sqft", "bedrooms", "bathrooms", "age_years"]]
y = data["price_lakh"]

# 3. Split data into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Create the ML model
model = LinearRegression()

# 5. Train the model
model.fit(X_train, y_train)

# 6. Test the model
predictions = model.predict(X_test)

# 7. Measure performance
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("Model trained successfully!")
print("Mean Absolute Error:", mae)
print("R2 Score:", r2)

# 8. Save the trained model
with open("house_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model saved as house_model.pkl")
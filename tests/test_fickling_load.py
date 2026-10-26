
import fickling

fickling.hook.activate_safe_ml_environment()

with open("house_model.pkl", "rb") as file:
    model = fickling.load(file)

print("Fickling load successful!")
print(type(model))

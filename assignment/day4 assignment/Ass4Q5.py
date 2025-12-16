# List of lambda functions for conversions
converters = [
    lambda t: t * 1000,            
    lambda kg: kg * 1000,        
    lambda g: g * 1000,             
    lambda mg: mg * 0.00000220462   
]

# Input from user in tonnes
tonnes = float(input("Enter weight in tonnes: "))

# Perform conversions
kg = converters[0](tonnes)
grams = converters[1](kg)
milligrams = converters[2](grams)
pounds = converters[3](milligrams)

# Display results
print(f"{tonnes} tonnes = {kg} kg")
print(f"{kg} kg = {grams} grams")
print(f"{grams} grams = {milligrams} milligrams")
print(f"{milligrams} milligrams = {pounds} lbs")

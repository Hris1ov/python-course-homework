# This program calculates the Body Mass Index (BMI) based on weight and height
# Input: Weight in kilograms and Height in meters
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = weight / (height * height)

# Round the result to 2 decimal places using round() function
bmi_rounded = round(bmi, 2)

# Output the result
print(f"Your BMI is: {bmi_rounded}")


def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def classify_bmi(bmi, age):
    if age < 18:
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal weight"
        elif 25 <= bmi < 29.9:
            return "Overweight"
        elif 30 <= bmi < 34.9:
            return "Obesity class 1"
        elif 35 <= bmi < 39.9:
            return "Obesity class 2"
        else:
            return "Obesity class 3"
    else:
        if bmi < 22:
            return "Underweight"
        elif 22 <= bmi < 27:
            return "Normal weight"
        elif 27 <= bmi < 32:
            return "Overweight"
        elif 32 <= bmi < 37:
            return "Obesity class 1"
        elif 37 <= bmi < 42:
            return "Obesity class 2"
        else:
            return "Obesity class 3"

weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))
age = int(input("Enter your age: "))

bmi = calculate_bmi(weight, height)

classification = classify_bmi(bmi, age)

print(f"\nYour BMI is: {bmi:.2f}")
print(f"Classification: {classification}")
print(f"Age: {age} years")

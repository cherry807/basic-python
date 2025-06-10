def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)

weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))
print("BMI:", calculate_bmi(weight, height))

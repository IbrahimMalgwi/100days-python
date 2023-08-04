height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = round(weight / height ** 2)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, have a normal weight.")
elif bmi < 35:
    print("Your BMI is {bmi}, have a overweight.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese")
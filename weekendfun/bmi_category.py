weight = float(input("Enter weight in KG: "))

height = float(input("Enter height in Meters: "))

bmi = weight / (height * height)

if (bmi < 18.5):
    print("BMI is ", bmi, "(UNDERWEIGHT)")

elif (bmi > 18.4 and bmi < 25):
    print("BMI is ", bmi, "(NORMAL)")

elif (bmi > 24.9 and bmi < 30):
    print("BMI is ", bmi, "(OVERWEIGHT)")

else:
    print("(OBESE)")

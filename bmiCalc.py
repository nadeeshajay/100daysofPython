weight = float(input('Input your weight(kg) : '))
height_cm = float(input('Input your height(cm) : '))
height = height_cm/100
bmi = round(weight / (height**2),2)
print(f"Your BMI value is : {bmi}")

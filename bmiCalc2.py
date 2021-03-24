weight = float(input('Input your weight(kg) : '))
height_cm = float(input('Input your height(cm) : '))
height = height_cm/100
bmi = round(weight / (height**2),2)
print(f"Your BMI value is : {bmi}")
print('That means..')
if bmi <= 18 :
    print('You are underweight !')
elif bmi <= 25 :
    print('You have a normal weight.')
elif bmi <= 30 :
    print('You are overweight !')
elif bmi <= 35 :
    print('You are obese.')
else:
    print('You are clinically OBESE !')
print('Welcome to the rollercoaster !')
height = float(input('Enter your height(cm): '))
if height >= 120 :
    age = int(input('Enter your age : '))
else :
    print('Sorry you\'re not height enough !')
bill = 0
if age <=12 :
    bill = 5.00
    print(f'The cost is $ {bill}')
elif age <=18 : 
    bill = 7.00
    print(f'The cost is $ {bill}')
else :
    bill = 10.00
    print(f'The cost is $ {bill}')

photo = input('Do you want to take photographs? This will cost additional $ 3.00 (Type y or n) ')
if photo == 'y' :
    print(f'The cost is $ {bill + 3 }')
else :
    print('Thank you for coming !')

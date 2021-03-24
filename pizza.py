cost = 0
print('Welcome to Python Pizza ! \nSmall pizza : $15 \nMedium pizza : $20 \nLarge pizza : $25 \n')
print('Pepperoni for small pizza + $2 \nPepperoni for medium or large pizza + $3\n')
print('Extra cheese for any size pizza + $1\n')
size = input('What size of pizza you want? Type s or m or l : ')
if size == 's':
    cost = 15
    pepperoni = input('Do you want pepperoni ? Type y or n : ')
    if pepperoni == 'y' :
        cost += 2
    cheese = input('Do you want extra cheese ? Type y or n : ')
    if cheese == 'y' :
        cost += 1
    print(f'Your total bill is $ {cost}')
elif size == 'm' :
    cost = 20 
    pepperoni = input('Do you want pepperoni ? Type y or n : ')
    if pepperoni == 'y' :
        cost += 3
    cheese = input('Do you want extra cheese ? Type y or n : ')
    if cheese == 'y' :
        cost += 1
    print(f'Your total bill is $ {cost}')
elif size == 'l' :
    cost = 25
    pepperoni = input('Do you want pepperoni ? Type y or n : ')
    if pepperoni == 'y' :
        cost += 3
    cheese = input('Do you want extra cheese ? Type y or n : ')
    if cheese == 'y' :
        cost += 1
    print(f'Your total bill is $ {cost}')
else :
    print('Please type s or m or l to select a size !')
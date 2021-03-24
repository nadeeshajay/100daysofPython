print('Welcome to love calculator !')
yourName = input('Type your name here : ')
your_name = yourName.lower()
herName = input('Type his / her name here : ')
her_name = herName.lower()
t = your_name.count('t') + her_name.count('t')
r = your_name.count('r') + her_name.count('r')
u = your_name.count('u') + her_name.count('u')
e = your_name.count('e') + her_name.count('e')

l = your_name.count('l') + her_name.count('l')
o = your_name.count('o') + her_name.count('o')
v = your_name.count('v') + her_name.count('v')
e = your_name.count('e') + her_name.count('e')

true = t + r + u + e
love = l + o + v + e
result = 'Your love precentage is ' + str(true) + str(love) +'%'
print(result)
rock = "ROCK"
paper = "PAPER"
scissor = "SCISSOR"
tools = [rock, paper, scissor]
select1 = int(input('Rock, paper and scissor !!!\nType 0 for Rock\n1 for Paper\n2 for Scissor: '))
player = tools[select1]
print (f'You choose {player}')
import random
select2 = random.randint(0,2)
computer = tools[select2]
print(f'Computer choose {computer}')
if select1 == 0 and select2 == 2:
    print('You won !!')
elif select1 == 2 and select2 == 1 :
    print('You won !!')
elif select1 == 1 and select2 == 0 :
    print('You won !!')
elif select1 == select2:
    print('Match tied !!')
else :
    print('You lost !!!')
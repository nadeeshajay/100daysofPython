import random
test_seed = int(input('Input a seed number : '))
random.seed(test_seed)

names = input('Enter your names here \n')
name_list = names.split(', ')

index = random.randint(0, len(name_list)-1)
buyer = name_list[index]
print(f"{buyer} is going to buy the meal today!!")
while True :
    num = str(input('Enter two digit number here : '))
    if len(num)==2 :
        result = int(num[0]) + int(num[1])
        print(result)
        break
    else :
        print('Please enter two digit number !')
boole = True 

while boole:
    try:
        a = int(input('What first number would you like to add: '))
        b = int(input('What second number would you liked to add: '))
    except ValueError:
        print('Please input a number')
    else:
        print(a + b)
        boole = False


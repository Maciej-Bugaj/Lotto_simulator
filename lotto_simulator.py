import random

try:
    number1 = int(input('Enter the first number: '))
    number2 = int(input('Enter the second number: '))
    number3 = int(input('Enter the third number: '))
    number4 = int(input('Enter the fourth number: '))
    number5 = int(input('Enter the fifth number: '))
    number6 = int(input('Enter the sixth number: '))

    numbers = [number1, number2, number3, number4, number5, number6]

    print("\nYour selected numbers are: ", numbers)

    myNumbers = []

    while len(myNumbers) < 7:
        
        generatedNumbers = random.randint(1,49)

        if generatedNumbers in myNumbers:
            print('The numbers that were repeated during the draw: ', myNumbers)
            continue
        
        myNumbers.append(generatedNumbers)
    print('The lock has been released...')
    print('Here are the winning numbers: ', myNumbers)



    for i in myNumbers:
        if i in numbers:
            print('Congratulations, you hit the number: ',[i])
            
except ValueError:
    print('Error! One or more of the values ​​you provided is not a number!')

input('Press ENTER to finish')
 





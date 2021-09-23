def Datacoupling():
    number1 = 10
    number2 = 20
    number3 = 30
    number4 = 40
    number5 = 50
    printer(number1,number2,number3,number4,number5)

def printer(number1,number2,number3,number4,number5):
    print('Number 1:',number1)
    print('Number 2:',number2)
    print('Number 3:',number3)
    print('Number 4:',number4)
    print('Number 5:',number5)

Datacoupling()

""" To avoid this we can either create objects of the parameters and
if possible pass the object which contains the data itself but this
    results in stamp coupling.So to avoid this from our example we can 
    create multiple methods for printing the numbers.."""

def printer1(number1,number2,number3):
    print('Number 1:',number1)
    print('Number 2:',number2)
    print('Number 3:',number3)

def printer2(number4,number5):
    print('Number 4:',number4)
    print('Number 5:',number5)



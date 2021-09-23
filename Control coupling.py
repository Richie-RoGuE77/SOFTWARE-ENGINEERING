class Base(object):
    def __init__(self,number):
        self.number= number

    def fact(self):
        if (self.number == 0):
            print("The factorial of the number is 1")
        else:
            for i in range(1, self.number + 1):
                i = i * (i + 1)
            print(f"The factorial of the number is {format(i)}")

x  = Base(0)
x.fact()

"""Here the variable number in class Base decides which lines of code is to be executed
in the function fact()..To avoid this type of coupling we need to factory design methods
i.e using different functions for solving each case.."""

#In our example we can use one function for number == 0  and another for number > 0

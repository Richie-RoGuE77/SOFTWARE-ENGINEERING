gvar = -20
def fun1(a):
    if(a>0):
        global gvar
        gvar = 40
        print(gvar)
        a = 0

def fun2():
    global gvar
    if(gvar > 0):
        print("The global variable variable value has been changed")

fun1(1)
fun2()

"""In this example both the functions fun1 and fun2 use the same global variable .
This creates a lot of confusion and errors in our code if its value is changed ,
 to avoid this we can use a static variable inside the functions.."""

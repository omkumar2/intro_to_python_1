def myFunction1():
    global x
    x=x*2
    print('Value of x inside function 1',x)

def myFunction2():
    global x
    x=x*3
    print('Value of x inside function 2',x)
    
x=5
print("Value of x before function call",x)
myFunction1()
myFunction2()
print("Value of x after function call",x)

def myFunction1(x):
    x = x * 2
    print('Value of x inside function 1', x)
    return x

def myFunction2(x):
    x = x * 3
    print('Value of x inside function 2', x)
    return x
    
x = 5
print("Value of x before function call", x)
x = myFunction1(x)
x = myFunction2(x)
print("Value of x after function call", x)
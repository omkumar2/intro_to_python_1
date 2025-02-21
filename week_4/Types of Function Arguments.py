
def add(a, b, c):
    return (a + b - c)

print(add( a = 20,b = 30,c =  40)) #10
print(add(20, 30, 40)) #10

#next
def add(c, a = 20, b = 30):
    return (a + b - c)
print(add(40))  #10
print(add(40, 10)) #0
print(add(40, 10, 50)) #20

# Types of Functions

'''
#inbuilt functions
print(), input() ,len()

#library functions
math.log(), math.sqrt(), random.random() ,randrange(), round(), str(), sum(), type(), reversed(), range(), max(), min(), map(), filter(), zip(),

#string methods (functions)
''.upper(), "".lower(), title(), capitalize(), swapcase(), isupper(), islower(), isdigit(), isalpha(), index(), replase(), split()
'''
#user defined functions
def square(x):
 sqr = x ** 2
 return sqr  

print(square(5))
def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y

add = lambda x,y:x+y
sub = lambda x,y:x-y
mul = lambda x,y:x*y
div = lambda x,y:x/y

print(add(10,20))
print(sub(10,20))
print(mul(10,20))
print(div(10,20))

print(type(add))

# enmerate

fruits = ['mango', 'apple', 'banana', 'orange', 'pineapple', 'watermelon', 'guava', 'kiwi']

size = [5,5,6,6,9,10,5,4]

print(list(zip(fruits,size)))
print(dict(zip(fruits,size)))

for fruit in enumerate(fruits):
    print(fruit)
    
for i in range(len(fruits)):
    print(i, fruits[i]) 
    
#map

a=[10,20,30,40,50,60]
b=[5,10,15,20,25,30]
#c = a + 1
def sub(x,y):
    return x-y

def incr(x):
    return x+1

c = map(sub,a,b)
c = map(incr, a)
print(list(c))

#

import math

a = [25, -16, 9, 81, -100]

def square_root(n):
    return math.sqrt(n)

def is_positive(n):
    return n > 0

c = map(square_root, filter(is_positive, a))  
print(list(c))
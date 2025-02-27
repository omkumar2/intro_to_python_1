#Write a python code using functions which calculates the number of upper case letters in a sentence,
#lower case letters ,total number of caharaters and total number of words in a sentence.

def upper(s):
    upper=0
    for c in s:
        if(c.isupper()):
            upper+=1
    return upper

def lower(s):
    lower=0
    for c in s:
        if(c.islower()):
            lower+=1
    return lower

def characters(s):
    chars=0
    for c in s:
        chars+=1
    return chars

def words(s):
    words=1
    for c in s:
        if(c==" "):
            words+=1
    return words

sentence=input("Enter a sentence: ")
uLetters=upper(sentence)
print(f'\nTotal number of upper case charcters: {uLetters}')
lLeters=lower(sentence)
print(f'Total number of lower case charcters: {lLeters}')
Chars=characters(sentence)
print(f'Total number of charcters: {Chars}')
Words=words(sentence)
print(f'Total number of words: {Words}')


#Write a python code using functions to calculate area and perimeter of a rectangle and circle.

pi = 22/7

def area_Rectangle(l,b):
    return l*b

def areaCricle(r):
    return pi*r*r

def perimeterRectangle(l,b):
    return 2*(l+b)

def perimeterCricle(r):
    return 2*pi*r

l=float(input("Enter length of rectangle: "))
b=float(input("Enter breadth of rectangle: "))
print(f'Area of rectangle: {area_Rectangle(l,b)}')
print(f'Perimeter of rectangle: {perimeterRectangle(l,b)}')

r=float(input("Enter radius of circle: "))
print(f'Area of circle: {areaCricle(r)}')
print(f'Perimeter of circle: {perimeterCricle(r)}') 

#Write a python code using functions which checks whether the input coordinats from a triangle or not

def distance(x1,y1,x2,y2):
    return ((((x2-x1)**2)+((y2-y1)**2))**0.5)

def isTriangle(max, a, b):
    if((a+b)>max):
        print('\nnTringale')
    else:
        print('\nNot a Triangle')
        
x1=float(input("Enter x1: "))
y1=float(input("Enter y1: "))
x2=float(input("Enter x2: "))
y2=float(input("Enter y2: "))
x3=float(input("Enter x3: "))
y3=float(input("Enter y3: "))

d1=distance(x1,y1,x2,y2)
print(f'\nDistance between point ({x1},{y1}) and ({x2},{y2}) = {d1}')
d2=distance(x2,y2,x3,y3)
print(f'Distance between point ({x2},{y2}) and ({x3},{y3}) = {d2}')
d3=distance(x3,y3,x1,y1)
print(f'Distance between point ({x3},{y3}) and ({x1},{y1}) = {d3}')

if(d1>d2):
    if (d1>d3):
        isTriangle(d1,d2,d3)
    else:
        isTriangle(d3,d1,d2)
elif(d2>d3):
    isTriangle(d2,d1,d3)
else:
    isTriangle(d3,d1,d2)
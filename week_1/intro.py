print("Hello, type your name :")
n=str(input())
print("Which place are you in?")
p=str(input())
print("Hello",n,"How is the weather in",p,"?")
print("what is your age?")
age=int(input())
print("good know you are ",age,"years old")

#this both are same

n=str(input("Hello, type your name :"))
p=str(input("Which place are you in?"))
print("Hello",n,"How is the weather in",p,"?")
age=int(input("what is your age?"))                                      
print("good know you are ",age,"years old")

#area of circle
r = int(input("Enter the radius of the circle: "))
area = 3.14*r*r
print("Area of the circle with radius",r,"is",area)

#list

l=[10,20,30]
print(l[0])
print(l[1])
print(l[2])

print(type(l[2]))#<class 'int'>
print(type(l)) #this show console -- <class 'list'>

# data type 1
l=[10,20,30]
n=10
r=6.3
o="om kumar"

print(type(l)) #<class 'list'>
print(type(n)) #<class 'int'>
print(type(r)) #<class 'float'>
print(type(o)) #<class 'str'>

#other data type

b1 = True
b2 = False
print(type(b1)) #<class 'bool'>
print(type(b2)) #<class 'bool'>
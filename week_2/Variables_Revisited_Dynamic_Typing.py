#next
# and =4
# print(and) #key word are not use as a syntax 

# #next
# 1a=3
# print(1a) #you can not used no. at stating

#next
roll=3
ROLL=112
Roll=15
print(roll,ROLL,Roll) #3 112 15       #python is case 

#next
x,y=1,2
print(x,y) #1,2       
x,y=y,x
print(x,y) #2,1

#next
x=12
print(x) #12
del x
print(x) #error because x is deleted

#next
count = 0
count += 1
count = count + 1
print(count)

#next
count = 5
count -= 1
count = count - 1
print(count)

#next
count = 5
count *= 2
count = count * 2
print(count)

#next
count = 5
count /= 2
count = count / 2
print(count)

#next
print("alpha" in "A variable name can only contain alpha-numeric characters and underscores") #true
print("alpha" in "A variable name must start with a letter or the underscore character") #false

#next
x = 5
print(1 < x < 10) #true
print(10 < x < 20) #false
print(x < 10 < x * 10 < 100) #true
print(10 > x <= 9) #true
print(5 == x > 4) #true
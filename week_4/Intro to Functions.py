

fruits = ["mango", "apple", "banana", "orange", "pineapple", "watermelon", "guava", "kiwi"]
'''
newList = []
for fruit in fruits:
  if "n" in fruit:
    newList.append(fruit.capitalize()) #capitalize() is used to capitalize the first letter of the string
'''
newList = [fruit.capitalize() for fruit in fruits if "n" in fruit]
print(newList)  #['Mango', 'Banana', 'Orange', 'Pineapple', 'Watermelon']

# Introduction to Functions

def add(a,b):
  ans=a+b
  print(ans)

add(1,3) #4

def sub(a,b):
  ans=a-b
  print(ans)

sub(10,8) #2

def discount(cost,d):
  ans=cost-(cost*(d/100))
  print(ans)

discount(100,8.3) #91.7

add(17,5)+sub(100,3)+discount(1500,7.5) #TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'    and it print 22 ,  97

#next
def add(a,b):
  ans=a+b
  return ans

a=2
b=15
ans=add(a,b)+10
ans=a+b+10
print(ans) #27

#next
def discount(cost,d):
  ans=cost-(cost*(d/100))
  return ans

print("Enter the cost price") #1000
c=int(input())
print("Enter the discount") #11
disc=int(input())
print("The final discounted price is:",discount(c,disc)) #The final discounted price is: 890.0


print("Enter the cost price") #1000
x=int(input())
print("Enter the discount") #11
y=int(input())
print("The final discounted price is:",discount(x,y)) #The final discounted price is: 890.0

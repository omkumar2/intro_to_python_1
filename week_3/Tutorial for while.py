#let us find the factorial of a number

num=int(input("Enter a number:"))

fact=1
if(num<0):
  print("Not defined")
else:
  while(num > 0):
    fact=fact*num
    num=num-1
print(fact) 

#find the number of digits in the given number
num = abs(int (input ('Enter s number: ')))
digits = 1
while(num > 9) :
  num = num // 10
  digits = digits + 1
print(digits)

#Enters number: 677
#3

#reverse the digits in the given number
num = int(input("Enter the number: "))  #num = abs(int(input("Enter the number: ")))   it can be do of negative number
rev = num % 10
num = num // 10
while (num > 0):
  r = num % 10
  num = num // 10
  rev = rev * 10 + r
print(rev)
#Enter the number: 678
#876 

# or

num = int(input("Enter the number: "))
absNum =abs(num)
if(num > 0):
    rev = num % 10
    num = num // 10
    while(num > 0):
        r = num % 10
        num = num // 10
        rev = rev * 10 + r
    print(rev)
else:
    rev = absNum % 10
    absNum = absNum // 10
    while(absNum > 0):
        r = absNum % 10
        absNum = absNum // 10
        rev = rev * 10 + r
    print(rev - 2 * rev)
    
#or

num = int(input("Enter the number: "))
absNum =abs(num)
rev = absNum % 10
absNum = absNum // 10
while(absNum > 0):
    r = absNum % 10
    absNum = absNum // 10
    rev = rev * 10 + r
if(num >= 0):
    print(rev)
else:
    print(rev - 2 * rev)

#Enter the number: -1234
#-4321

rev = absNum % 10
absNum = absNum // 10
while(absNum > 0):
    r = absNum % 10
    absNum = absNum // 10
    rev = rev * 10 + r
if(num < 0):
    rev = rev - 2 * rev
  
if(num == rev):
    print("Palindrome")
else:
    print("Not a Palindrome")

#Enter the number: 12321       Enter the number: 456
#Palindrome                    Not a Palindrome

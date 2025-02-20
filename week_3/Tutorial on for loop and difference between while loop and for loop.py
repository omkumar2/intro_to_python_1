#find the factorial of the given number
num = int(input("Enter a number: "))
fact = 1
if num < 0:
  print("Factorial does not exist for negative numbers")
else:
  for i in range(1, num + 1):
    fact = fact * i
  print("The factorial of", num, "is", fact)
   
#  for i in range(num, 1, -1):
#     fact = fact * i 
# print("The factorial of", num, "is", fact)

# Enter a number: 5
# The factorial of 5 is 120
#find the number of digits in the given number

num = abs(int(input("Enter a number: ")))
strNum = str(num)
digits = 0
for c in strNum:
  digits = digits + 1
print(digits)
lentgh = len(str(num))
print(lentgh)

# Enter a number: 4567
# 4

#rerver the digits in the given number
num = int(input("Enter a number: "))
absStrNum = str(abs(num))
rev = ""
for c in absStrNum:
  rev = c + rev
if (num >= 0):
  print(rev)
else:
  print("-" + rev)

# Enter a number: 7890
# 0987


#find whether the entered number is palindrome or not
num=int(input("Enter a number: "))
absStrNum = str(abs(num))
rev = ''
for c in absStrNum:
  rev = c + rev
if num < 0:
  rev = '-' + rev
if num == int(rev):
  print("Palindrome")
else:
  print("Not a Palindrome")

# Enter a number: 123
# Not a Palindrome


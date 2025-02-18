for i in range(4):
 print(i,"Hello India")
 print("*************")
 print("@@@@@@@@@@@@@")
 
# 0 Hello India
# *************
# @@@@@@@@@@@@@
# 1 Hello India
# *************
# @@@@@@@@@@@@@
# 2 Hello India
# *************
# @@@@@@@@@@@@@
# 3 Hello India
# *************
# @@@@@@@@@@@@@

#An example of a for loop
print("Enter a number:")
n=int(input())

for i in range(n):
  if (i%2==0):
    print(i,"Hello India")
  else:
    print(i,"Hi World")
    
# Enter a number:
# 4
# 0 Hello India
# 1 Hi World
# 2 Hello India
# 3 Hi World


#Adds frist 10 integer numbers
num=int(input("Enter a number:"))

ans=0
for i in range(num):
  ans=ans+i
print("The answer is",ans)

# nter a number:11
# The answer is 55

#for loop for multiplication tables

for i in range(1,5):
  print("2 X ", i, "=", 2*i)

# 2 X  1 = 2
# 2 X  2 = 4
# 2 X  3 = 6
# 2 X  4 = 8
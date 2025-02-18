#if condition
#let us consider the movie "Avengers". This is a 13+ movie.
print("Please enter your date of birth")
birth_year=int(input())

current_year=2025

age=current_year-birth_year
if(age<13):
  print("You are under age, you cannot watch this movie.")
  print("Wait until you are old enough to watch this movie.")
else:  
  print("you are old enough to watch avengers, enjoy!")
  print("Don't forget to watch the sequels and prequels.")

print("Have a nice time")

# Please enter your date of birth
# 2006
# you are old enough to watch avengers, enjoy!
# Don't forget to watch the sequels and prequels.
# Have a nice time

# Tutorial on if, else and else-if (elif) conditions

#find wether the number is even or odd
num = int(input("Enter a number: "))

if(num % 2 == 0) :
  print("The number is even")
else:
  print("The number is odd")
# Enter a number: 5
# The number is odd

#next
#find wether the given number ends with 0 or 5 or any other number
num = int(input("Enter a number: "))
if(num % 5 == 0):
  if(num % 10 == 0):
    print('0')
  else:
    print('5')
else:
  print("other") 
#Enter a number: 4
#other

#next
#find the grade of student based on the given marks from 0 to 100
marks = int(input("Enter your marks: "))

if(marks>=90 and marks<100):
  print("A")
elif(marks>=80 and marks<90):
  print("B")
elif(marks>=70 and marks<80):
  print("C")
elif(marks>=60 and marks<70):
  print("D")
elif(marks>=0 and marks<0):
  print("E")
else:
  print("Invalid input")
# Enter your marks: -2
# Invalid input
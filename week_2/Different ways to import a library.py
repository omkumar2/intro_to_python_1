import math
print(math.log(10)) #2.302585092994046
print(math.sin(90)) #0.8939966636005579
print(math.sqrt(16)) #0.4
print(math.factorial(5)) #120
print(math.pow(10,3)) #1000

#next
import random
print(random.random()) # Any number you want 0 to 10
print(random.randrange(1,6)) #Any number you want 1 to 6

#next
dice1=(random.randrange(1,6))
dice2=(random.randrange(1,6))
total=dice1+dice2
print("your pair of dice is:",total) #Any number you want 1 to 12

#next
#let us simulate a coin toss.
import random
a=random.random()
if(a<.5):
  print("Heads")
else:
  print("Tails")  # This Is a Random head and tail
  
  #Different ways to import a library

import calendar
print(calendar.month(2026,5)) #it show entire month
print(calendar.calendar(2026)) #it show Entire year

from calendar import *
print(calendar(2026)) 
print(month(2026,5)) #in this  i ot need to write calendar
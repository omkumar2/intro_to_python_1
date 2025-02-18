#find all prime numbers less than the entered number
num = int(input("Enter a number: "))
if (num > 2):
  print(2, end = ' ')
for i in range(3, num):
  flag = False
  for j in range(2, i):
    if (i % j == 0):
      flag = False
      break
    else:
      flag = True
  if (flag):
    print(i, end = ' ')

#find the total prfit/loss of each trader working in a trading firm. Information regarding number of traders and number of transactions is unknown
empID = input('Enter Employee ID: ')
while(empID != '-1'):
  trade = int(input('Enter the trade amount: '))
  profit_loss = 0
  while(trade != 0):
    profit_loss = profit_loss + trade
    trade = int(input('Enter the trade amount: '))
  print(f'Profit/loss for employee {empID} is {profit_loss}')
  empID = input('\nEnter Employee ID: ')

# Enter Employee ID: KL_343
# Enter the trade amount: 5678
# Enter the trade amount: 78909
# Enter the trade amount: -6789
# Enter the trade amount: 0
# Profit/loss for employee KL_343 is 77798

#find the day wise total rainfall for the entered duration of time e.g. week, month, etc.

days = int(input("Enter the number of days: "))
for i in range(1, days+1):
  total = 0
  rainfall = int(input("Enter the rainfall: "))
  while(rainfall != -1):
    total = total + rainfall
    rainfall = int(input("Enter the rainfall: "))
  print("Total rainfall for day {0} is {1}".format(i, total))

# Enter the number of days: 88
# Enter the rainfall: 990
# Enter the rainfall: 098
# Enter the rainfall: 09899
# Enter the rainfall: 09988
# Enter the rainfall: -1
# Total rainfall for day 1 is 20975

#find the length of longest word from the set of words entered by the user
word = input("Enter the word: ")
maxLen = 0
while(word != '-1'):
  count = 0
  for letter in word:
    count = count + 1
  if(count > maxLen):
    maxLen = count
  word = input("Enter the word: ")
print("The length of longest word is %s" %maxLen)

# Enter the word: om
# Enter the word: kumar
# Enter the word: thakur
# Enter the word: -1
# The length of longest word is 6
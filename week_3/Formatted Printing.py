
for x in range( 10):
  print(x, end = " ")  # 0 1 2 3 4 5 6 7 8 9
  
d = 3
m = 2
y = 2025
print("todays date is", end = ' ')
print(d, m, y, sep = "-") # todays date is 3-2-2025

num = int(input("enter a number: "))
for i in range(1, 11):
  #print(num, 'x', i, '=', num*i)
  #print(f'{num} x {i} = {num*i}')
  #print('%d X %d = %d' %(num, i, num*i))
  print('{0} X {1} = {2}'.format(num, i, num*i))

# enter a number: 5
# 5 X 1 = 5
# 5 X 2 = 10
# 5 X 3 = 15
# 5 X 4 = 20
# 5 X 5 = 25
# 5 X 6 = 30
# 5 X 7 = 35
# 5 X 8 = 40
# 5 X 9 = 45
# 5 X 10 = 50

pi = 22 / 7
print(f'Value of Pi = {pi}') #Value of Pi = 3.142857142857143
print('Value of Pi = {0}'.format(pi)) #Value of Pi = 3.142857142857143
print('Value of Pi = %f' % (pi)) #Value of Pi = 3.142857

print(f'Value of Pi = {pi:.2f}') #Value of Pi = 3.14
print('Value of Pi = {0:.2f}'.format(pi)) #Value of Pi = 3.14
print('Value of Pi = %.4f' % (pi)) #Value of Pi = 3.1428

#next
print('{0:4d}'.format(1))
print('{0:5d}'.format(11))
print('{0:4d}'.format(111))
print('{0:5d}'.format(1111))

# 1
#    11
#  111
#  1111


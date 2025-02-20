
a = 10
b = 20
'''
if a < b:
  small = a
else:
  small = b
''' #both code are same
small = a if a < b else b
print(small)  # 10

#next
a = 5
'''
while a > 0:
  print(a)
  #a = a - 1
  a -= 1
  '''  #the both code is same
while a > 0: print(a); a -= 1

# 5
# 4
# 3
# 2
# 1
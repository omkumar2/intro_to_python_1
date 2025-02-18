
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

#next
fruits = ["mango", "apple", "banana", "orange", "pineapple", "watermelon", "guava", "kiwi"]
'''
newList = []
for fruit in fruits:
  if "n" in fruit:
    newList.append(fruit.capitalize())
    ''' # again the code are same
newList = [fruit.capitalize() for fruit in fruits if "n" in fruit]
print(newList) # ['Mango', 'Banana', 'Orange', 'Pineapple', 'Watermelon']

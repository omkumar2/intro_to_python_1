
d = {'key' : 'value'}
print(d['key'])  # value

#next
d = {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
print(d) # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
for key in d:
    print(key, d[key])

# 0 0
# 1 1
# 2 4
# 3 9
# 4 16

#next
d = {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
print(d.keys()) # dict_keys([0, 1, 2, 3, 4])
print(d.values()) # dict_values([0, 1, 4, 9, 16])
print(d.items()) # dict_items([(0, 0), (1, 1), (2, 4), (3, 9), (4, 16)])

#: Sorting using Functions

#find out the mimium most element in the list l
#append that to a new list x.
#remove the minimum from the original list l.

#find out the mimimum most element in the list l
def min_list(l):
  mini=l[0]
  for i in range(len(l)):
    if l[i]<mini:
      mini=l[i]
  return mini

def obvious_sort1(l):
  x=[]
  while(len(l)>0):
      mini=min_list(l)
      x.append(mini)
      l.remove(mini)
  return x

l=[90,23,97,88,5,1]
print(obvious_sort1(l)) # [1, 5, 23, 88, 90, 97]
 
#we just learnt that breaking our problem into smaller modules and solving them makes it easy on our mind.

#next

def obvious_sort(l):
  x=[]
  while(len(l)>0):
    mini=l[0]
    for i in range(len(l)):
      if l[i]<mini:
        mini=l[i]
    x.append(mini)
    l.remove(mini)
  return x

l=[90,23,97,88,5,1]
print(obvious_sort(l)) # [1, 5, 23, 88, 90, 97]

#  obvious_sort and obvious_sort1 code are same 
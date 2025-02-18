def add(x):
  x = x + 1
  return x

x = 5
print(add(x)) #6
print(x) #5

def add(x):
  x.append(1)
  return x

x = [5]
print(add(x)) #[5,1]
print(x) #[5,1]

#next
l=[1,2,3]
print(l) #[1,2,3]

l.append(4)
print(l) #[1,2,3,4]

l.insert(2,9) # Insert 9 at index 2
print(l) #[1,2,9,3,4]

#next
l=[1,2,3]
print(l) #[1,2,3]

l.remove(2)
print(l) #[1,3]

l.pop(0) # Remove the element at index 0
print(l) #[3]

#next
l=[2,6,1,50,3,7,5]
l.sort()
print(l) #[1, 2, 3, 5, 6, 7, 50]

#next
l=[2,6,1,50,3,7,5]
l.reverse()
print(l) #[5, 7, 3, 50, 1, 6, 2]

# More on Sets

st={1, 2, 3, 4, 5, 1, 2, 3, 4, 5}
print(st) #{1, 2, 3, 4, 5}
print(st[0]) #set' object is not subscriptable          or   error

#next
A={1, 3, 5}
B={1, 2, 3, 4, 5}
print(A.issuperset(B)) #false   

#next
A = {1, 2, 3}
B = {3, 4, 5}
c1 = A.union(B)
c2 = A | B
print(c1, c2) #{1, 2, 3, 4, 5} {1, 2, 3, 4, 5}

#next
A = {1, 2, 3}
B = {3, 4, 5}
c1 = A.intersection(B)
c2 = A & B
print(c1, c2) #{3} {3}

#next
A = {1, 2, 3}
B = {3, 4, 5}
c1 = A.difference(B)
c2 = A - B
print(c1, c2) #{1, 2} {1, 2}

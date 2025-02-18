l=[5,7,19,10,4]
l.append(100)
print(l) # [5, 7, 19, 10, 4, 100]
l.remove(7)
print(l) # [5, 19, 10, 4, 100]
t=(2,7,18,64,101,108,65)
print(t) # (2, 7, 18, 64, 101, 108, 65)
t.remove(101) #it will through error
t.append(100) #it will through error
print(t[0]) #2
print("A tuple is unchangeable") #A tuple is unchangeable
print("A list can changed") # A list can changed 

l=list(range(10))
print(l) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
t=tuple(range(10))
print(t) # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

print("l is flexible but t is not") #l is flexible but t is not
import string
s=string.ascii_letters
print(s) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
s=string.ascii_lowercase
print(s) # abcdefghijklmnopqrstuvwxyz
s=string.ascii_uppercase
print(s) # ABCDEFGHIJKLMNOPQRSTUVWXYZ

s=string.ascii_letters
print(s) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
s=set(s) 
print(s) # ('v', 'G', 'm', 'C', 'g', 'n', 'h', 'k', 'b', 'e', 'a', 'r', 'J', 'Y', 'A', 'M', 'd', 'j', 'I', 'N', 'i', 'y', 'z', 'P', 'R', 'F', 's', 'T', 'l', 'B', 'D', 'u', 'L', 'p', 'c', 'Z', 't', 'H', 'w', 'o', 'Q', 'W', 'x', 'E', 'X', 'V', 'f', 'S', 'U', 'q', 'O', 'K')

alpha=tuple(s)
print(alpha)# ('v', 'G', 'm', 'C', 'g', 'n', 'h', 'k', 'b', 'e', 'a', 'r', 'J', 'Y', 'A', 'M', 'd', 'j', 'I', 'N', 'i', 'y', 'z', 'P', 'R', 'F', 's', 'T', 'l', 'B', 'D', 'u', 'L', 'p', 'c', 'Z', 't', 'H', 'w', 'o', 'Q', 'W', 'x', 'E', 'X', 'V', 'f', 'S', 'U', 'q', 'O', 'K')
s=string.ascii_letters
alpha=tuple(list(s))
print(alpha) # ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
print(list(s)) # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

x='sudarshan#%&^$indiaBharath()Karnataka$%punjab#tamilnadu'

r=[]
for p in l:
  if p  in alpha:
    r.append(p)

print(r) #[]

l=list(range(10))
t=tuple(range(10))
print(l.__sizeof__()) #120
print(t.__sizeof__()) #104

print("when we are sure of the list that we are handling and we are also sure that it never changes, then use a tuple") #when we are sure of the list that we are handling and we are also sure that it never changes, then use a tuple

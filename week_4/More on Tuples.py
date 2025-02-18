
t = 1, 2, 3
print(t, type(t)) #(1, 2, 3) <class 'tuple'>

x, y, z = t
print(x, y, z)  #1 2 3

#next
X = 5
Y = 10
X, Y = Y, X
print(X, Y) # 10 5

#next
l = [10]
print(l, type(l)) #[10] <class 'list'>

t = (10)
print(t, type(t)) #10 <class 'int'>

t = (10,)
print(t, type(t)) #(10,) <class 'tuple'>

#next
t = ([1, 2], ['a', 'b'])
t[0] = [10, 20]
print(t) #'tuple' object does not support item assignment       or   error

#next
t = ([1, 2], ['a', 'b'])
t[0][0] = 10
print(t) #([10, 2], ['a', 'b'])

#we can not modify "Tuple" but inside the "Tuple" we can modify the "list" 


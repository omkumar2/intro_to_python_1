l=[1,2,3,6,77]
print(l) #[1, 2, 3, 6, 77]
l.append(1045)
print(l) #[1, 2, 3, 6, 77, 1045]
l.append(2)
print(l) #[1, 2, 3, 6, 77, 1045, 2]
l.remove(77)
print(l) #[1, 2, 3, 6, 1045, 2]
l.remove(2)
print(l) #[1, 3, 6, 1045, 2]


l=[]
l.append(1)
l.append(2)
l.append(3)
print(l) #[1, 2, 3]
x=[]
x.append(l)
print(x) #[[1, 2, 3]]
m=[10,20,30]
x.append(m)
print(x) #[[1, 2, 3], [10, 20, 30]]
t=[]
t.append(x)
print(t) #[[[1, 2, 3], [10, 20, 30]]]
t.append([100,101,102])
print(t) #[[[1, 2, 3], [10, 20, 30]], [100, 101, 102]]
print(t[0]) #[[1, 2, 3], [10, 20, 30]]
print(t[1]) #[100, 101, 102]
M=[]
M.append([1,2,3]) 
M.append([4,5,6])
M.append([7,8,9])
print(M) #[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(M[0]) #[1, 2, 3]
print(M[0][0]) #1
print(M[0][1]) #2


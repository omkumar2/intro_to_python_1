l1 = [1,2,3]
l2 = [10,20,30]
l12 = l1 + l2
l21 = l2 + l1
print(l12, l21) #[1, 2, 3, 10, 20, 30] [10, 20, 30, 1, 2, 3]

#next
l1= [0]*10
print(l1) #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
l2= [1,2,3]*5
print(l2) #[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]

#next
l1 = [1,2,3]
l2 = [1,2,3]
l3 = [1,3,2]
print(l1 == l2) #true 
print(l2 == l3) #false
print(l2 < l3) #true

#next
print([1,2] < [2,1]) #true
print([] < [1,2,3]) #true
print([2,3] < [3]) #true
print([] < [1]) #true

#next
l = [1,2,4]
print(l) #[1,2,4]
l[2] = 3
print(l) #[1,2,3]

s= 'abce'
print(s[3]) #e
s[3] = 'd'
print(s) #'str' object does not support item assignment      or  error

#next
x=5
y=x
x=10
print(x,y) #10 5

l1=[1,2,3]
l2=l1
l1[0]=100
print(l1,l2) #[100, 2, 3] [100, 2, 3]

#next
l1=[1,2,3]
l2=list(l1)
l3=l1[:]
l4=l1.copy()

l2[0]=100
l3[1]=200
l4[2]=300
l5=l1

print(l1,l2,l3,l4) #[1, 2, 3] [100, 2, 3] [1, 200, 3] [1, 2, 300]

print(l1 is l2) #false
print(l1 is l3) #false
print(l1 is l4) #false
print(l1 is l5) #true



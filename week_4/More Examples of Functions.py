#let write a few function on lists

def frist_element(l):
  return l[0]
x=[1,2,3]
print(frist_element(x)) #1

def second_element(l):
  return l[1]
print(second_element(x)) #2

#next
#let write a few function on lists

def list_min(l):
  mini=l[0]
  for i in range(len(l)):
    if(l[i]<mini):
      mini=l[i]
  return mini

def list_max(l):
  maxi=l[0]
  for i in range(len(l)):
    if(l[i]>maxi):
      maxi=l[i]
  return maxi

def list_appendbefore(l,z):
  newl=[]
  for i in range(len(z)):
    newl.append(z[i])
  for i in range(len(l)):
    newl.append(l[i])
  return newl

def list_appendend(l,z):
  newl=[]
  for i in range(len(l)):
    newl.append(l[i])
  for i in range(len(z)):
    newl.append(z[i])
  return newl

def list_average(l):
  sum=0
  for i in range(len(l)):
    sum=sum+l[i]
  ans=sum/len(l)
  return ans

l=[1,2,3,4,5,-10,6,4,100]
print(list_min(l)) #-10
print(list_max(l)) #100
z=[10,20,30]
print(list_appendbefore(l,z)) #[10, 20, 30, 1, 2, 3, 4, 5, -10, 6, 4, 100]
print(list_appendend(l,z)) #[1, 2, 3, 4, 5, -10, 6, 4, 100, 10, 20, 30]
print(list_average(l)) #12.777777777777779

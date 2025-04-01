'''cheak if a given element k is present in a list L or not'''

def obvious_search(L,k):
    for x in L:
        if x==k:
            return 1
    return 0

L=list(range(100))
#print(L)
print(obvious_search(L,200))
print(obvious_search(L,2))



def sum(n):
    ans=0
    for i in range(n):
        ans+=i
    return ans

a=time.time();print(sum(100));b=time.time();print(b-a)

print(sum(10))
print("hello world");print("HI, this is second command")
print("frist command");print(sum(10));print("last one")

# this is a import of time module

import time

print(time.time())

a=time.time()
b=time.time()

print(b-a)

a=time.time();print(sum(100));b=time.time();print(b-a)

# this give us the mid point of the list starting from begin and ending at end

l=[0,1,2,3,4,5,6,7,8,9,10]
begin=3
end=8

print((begin+end)//2)


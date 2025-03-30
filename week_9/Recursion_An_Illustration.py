def sum(n):
#verified 
    ans=0
    for i in range(n):
        ans=ans+(i+1)
    return ans

print(sum(4))


#recursion in python

def sum(n):
    if (n==1):
        return 1
    else:
        return n+sum(n-1)

#python lets you call the same function within the function

print(sum(50))



#compute compound interest by assuming the interest to be 105
def comp(p,n):
    if (n==1):
        return p*(1.1)
    else:
        return (comp(p,n-1))*1.1
    
print(comp(2000,3))




def fact(n):
    if (n==1):
        return 1
    else:
        return (fact(n-1))*n
    
print(fact(5))
    
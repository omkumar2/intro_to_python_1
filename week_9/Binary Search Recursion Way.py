'''code for binary search using recursion'''

def rbinaysearch(L,k,begin,end):
    
    if (begin ==end):
        if (L[begin]==k):
            return 1
        else:
            return 0
    if (end - begin==1):
        if (L[begin]==k) or (L[end]==k):
            return 1
        else:
            return 0
    if (end-begin>1):
        mid = (begin+end)//2
        if(L[mid]>k):
            end=mid-1
        if (L[mid]<k):
            begin=mid+1
        if (L[mid]==k):
            return 1
    if (end-begin<0):
        return 0
        
    return rbinaysearch(L,k,begin,end)
        

print(rbinaysearch[1,7,10,16,100,108,1008],7,0,6)


def sum (n):
    if (n==0):
        return 0
    else:
        return n+sum(n-1)

    
print(sum(995))

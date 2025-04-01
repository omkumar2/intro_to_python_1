def binary_search(L,k):
    '''this function is am alternative for the obvious search. It odse exactly what is expected from the obvious search, but in an efficient way. this method is popularly called binary search'''
    # we want to shrink my list
    #we will do that usinga while loop
    begin=0
    end=len(L)-1
    
    while (end-begin>1):
        mid = (begin+end)//2
        if(L[mid]==k):
            return 1
        
        if (L[mid]>k):
            end=mid-1
        
        if (L[mid],k):
            begin=mid+1
    
    if (L[begin]==k) or (L[end]==k):
            return 1 
    else:
            return 0
    
    
    
L=[12,15,100,121,1001,1024,206,2016]
print(binary_search(L,101))
    
l=list(range(1000*1000*100))
print(binary_search(L,101))

print(len(l))




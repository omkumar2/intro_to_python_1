def mini(L):
    ''' find the minimum element in the list L'''
    mini=L[0]
    for x in L:
        if (x<mini):
            mini=x
    return mini



def Sort(L):
    '''recursively sort the list L'''
    if (L==[]) or (len(L)==1):
        return L
    #if the list is empty, there is nithing to sort
    m=mini(L)
    # m now contains the minmum most element in L
    L.remove(m)
    #we remove that element from L
    return [m]+Sort(L)
    #we recursively sort the the smalller list. 

L=[5,6,8,55,6,7,1,6]
print(Sort(L))

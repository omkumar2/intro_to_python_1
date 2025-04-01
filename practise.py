'''cheak if a given element k is present in a list L or not'''

def obvious_search(L,k):
    for x in L:
        if x==k:
            return 1
    return 0

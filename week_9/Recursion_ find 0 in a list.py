'''this is a piece of code to check if a given list has 0 in it or not. If it has "zero" in it , we return True(1), otherwise we return False(0)'''

def check0(L):
    #if the list is empty, return False
    if (len(L)==0):
        return 0
    if (L[0]==0):
        # if the frist element is 0, return 1
        return 1
    else:
        # check the rest of the list
        return check0(L[1:len(L)])
    
print(check0([1,2,3,4,5,55,5,4,3,5,6,0,5]))


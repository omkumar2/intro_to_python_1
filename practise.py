#initialise C to zero.
#i need to cosider two matrices A and B.
#i need to find the dot product of two lists.
#i need to pick ith row  and jth column in a matrix.

def initialize_matrix(dim):
#code verfied ,work perfectly fine on the test cases.
    C=[]
    for i in range(dim):
        C.append([])
    for i in range (dim):
        for j in range(dim):
            C[i].append(0)
    return C

print(initialize_matrix(3))

def dot_product(u,v):
    dim=len(u)
    ans=0
    for i in range(dim):
        ans+=u[i]*v[i]
    return ans

x=[1,2,3]
y=[7,1,2]

print(dot_product(x,y))

def row(M,i):
    dim = len(M)
    l=[]
    for k in range(dim):
        l.append(M[i][k])
    return l

A=[[1,2,3],[4,5,6],[7,8,9]]
print(row(A,2))
def column(M,j):
    dim = len(M)
    l=[]
    for k in range(dim):
        l.append(M[k][j])
    return l
    

print(column(A,2))

def mat_mul(A,B):
    dim=len(A)
    C=initialize_matrix(dim)
    for i in range(dim):
        for j in range(dim):
            C[i][j]=dot_product(row(A,i),column(B,j))
    return C

A=[[1,2,3],[4,5,6],[7,8,9]]
B=[[1,2,1],[6,2,3],[4,2,1]]
print(mat_mul(A,B)) 


import numpy as np

A=np.matrix(A)
B=np.matrix(B)

print(A*B)




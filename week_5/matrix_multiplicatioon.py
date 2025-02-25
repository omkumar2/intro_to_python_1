r1=[1,2,3]
r2=[4,5,6]
r3=[7,8,9]

s1=[1,2,1]
s2=[6,2,3]
s3=[4,2,1]

A=[]
B=[]
A.append(r1)
A.append(r2)
A.append(r3)

B.append(s1)
B.append(s2)
B.append(s3)

c=[[0,0,0],[0,0,0],[0,0,0]]

dim=3

#C[2][1] is the dot product of the 2nd row of A and the 1st column of B

for i in range(dim):
    for j in range(dim):
        for k in range(dim):
            c[i][j]+=A[i][k]*B[k][j]
            
print(c)
# C[i][j]=dot product of A[i][....] and B[....][j]

import numpy as np

# Define your matrices (assuming you meant them to be 2D matrices)
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[1, 2, 1], [6, 2, 3], [4, 2, 1]]

# Convert lists to NumPy arrays
x = np.array(A)
y = np.array(B)

# Perform matrix multiplication using np.dot or @ operator (Python 3.5+)
result = np.dot(x, y)  # For older Python versions

print(result)

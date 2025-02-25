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

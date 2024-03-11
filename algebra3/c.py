import numpy as np

A = np.array([[2, -1, -1],
              [0, 2, -1],  
              [0, 0, -1]])

B = np.array([[-1, 0, 0],
              [1, -3, 0],
              [1, 1, -5]])

A3 = A**3
A2 = A**2

left_matrix = ((A3 - 2*A2 + 3*A)).T
right_vector = 4*(B**2) - B

X = np.linalg.solve(left_matrix, right_vector)
print(X)

# Проверка 
check = left_matrix @ X
print(np.allclose(right_vector, check))




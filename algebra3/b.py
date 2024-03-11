import numpy as np

A = np.array([[-1, 2, -4],  
              [1, -1, 7],
              [-1, 0, 0]])

B = np.array([[1, 0, 0],
              [0, 2, 0],
              [1, 0, 3]])

C = np.array([[3, 8, -1],
              [0, 8, 0],
              [2, -1, 3]])

A2 = A**2 
B3 = B**3
left_matrix = ((A2 @ B) + (B3 @ A)).T 

X = np.linalg.solve(left_matrix, B @ C)
print(X)

# Проверка
right = B @ C
check = left_matrix @ X
print(np.allclose(right, check)) 



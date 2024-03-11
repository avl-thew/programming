
1

import numpy as np
from numpy.linalg import det

A = np.array([[4, -1, 7], 
              [0, 1, -2],
              [0, 0, 9]])

B = np.array([[-1, 1, 0],
              [0, 0, 3],
              [6, 2, -1]])

C = np.array([[5, 1, 1],
              [1, 5, 1],
              [1, 1, 5]])

A_plus_3B_T = A + 3*B.T 
A3_T_minus_B = 3*A.T - B

X = np.linalg.solve(A_plus_3B_T @ (3*A.T - B), C)


# Проверка 
left = (A + 3*B.T) @ (3*A.T - B) @ X
right = C

print(X)
print(np.allclose(left, right)) # True, если решение верное



#2
import numpy as np
import matplotlib.pyplot as plt

A = np.array([-3, 1])
B = np.array([0, 3])
C = np.array([2, -5])
D = np.array([-1, 0])

def plot_pic():
	plt.plot([A[0], D[0]], [A[1], D[1]], color='b')
	plt.plot([B[0], C[0]], [B[1], C[1]], color='b')
	plt.plot([C[0], A[0]], [C[1], A[1]], color='b')
	plt.plot([D[0], B[0]], [D[1], B[1]], color='b')
	plt.scatter(A[0], A[1], color='red', label='A=(-3, 1)', alpha=1)
	plt.scatter(B[0], B[1], color='red', label='B=(0, 3)', alpha=1)
	plt.scatter(C[0], C[1], color='red', label='C=(2, -5)', alpha=1)
	plt.scatter(D[0], D[1], color='red', label='D=(-1, 0)', alpha=1)
	dA = np.array([0.2, 0.15])
	dB = np.array([-0.4, -0.1])
	dC = np.array([-0.7, 0.1])
	dD = np.array([0.4, 0.1])
	plt.xlabel('x')
	plt.ylabel('y')
	plt.legend()
	plt.axhline(0, color='black',linewidth=0.5)
	plt.axvline(0, color='black',linewidth=0.5)
	plt.grid(True, linewidth=0.5, linestyle='dotted')
	plt.show()
plot_pic()
# Вычисление площади четырехугольника ABCD
S = 0.5 * np.abs(np.cross(B - A, D - C))
print("Площадь четырехугольника ABCD:", S)



# import numpy as np
# import matplotlib.pyplot as plt
# A = np.array([-3, 1])
# B = np.array([0, 3])
# C = np.array([2, -5])
# D = np.array([-1, 0])
# plt.plot([A[0], B[0]], [A[1], B[1]], color='b')
# plt.plot([B[0], C[0]], [B[1], C[1]], color='b')
# plt.plot([C[0], D[0]], [C[1], D[1]], color='b')
# plt.plot([D[0], A[0]], [D[1], A[1]], color='b')
# plt.scatter(A[0], A[1], color='r', label='A')
# plt.scatter(B[0], B[1], color='r', label='B')
# plt.scatter(C[0], C[1], color='r', label='C')
# plt.scatter(D[0], D[1], color='r', label='D')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend()
# plt.axhline(0, color='black',linewidth=0.5)
# plt.axvline(0, color='black',linewidth=0.5)
# plt.grid(True, linewidth=0.5, linestyle='dotted')
# plt.show()
# # Вычисление площади четырехугольника ABCD
# area = 0.5 * np.abs(np.cross(B - D, A- C))
# print("Площадь четырехугольника ABCD:", area)
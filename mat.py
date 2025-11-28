import numpy as np

A = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

B = np.array([[9,8,7],
              [6,5,4],
              [3,2,1]])

s = A + B
d = A - B
p = A @ B 

print("A:\n", A)
print("B:\n", B)
print("A + B:\n", s)
print("A - B:\n", d)
print("A @ B:\n", p)
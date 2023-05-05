import numpy as np

# Define a forma quadrática
f = np.array([[1, -1.5],
              [-1.5, 1]])

# Encontra a matriz associada
M = np.linalg.inv(np.eye(2)).dot(f)

print("Matriz associada:\n", M)

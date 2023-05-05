import numpy as np

x = np.array([2, 3, 5, 7, 9])
m = np.array([[0.7, 0.7, 0.5, 0.2, 0.5],
              [0.7, 0.0, 0.4, 0.3, 0.6],
              [0.5, 0.4, 0.2, 0.6, 0.4],
              [0.2, 0.3, 0.6, 0.9, 0.2],
              [0.5, 0.6, 0.4, 0.2, 0.1]])

resultado = np.dot(m, x)

print(sum(resultado))

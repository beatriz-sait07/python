import numpy as np

# Gera vetores aleatórios u e v em R^3
u = np.random.rand(3)
v = np.random.rand(3)

# Verifica se a norma de u é igual à norma de v
if np.linalg.norm(u) == np.linalg.norm(v):
    # Calcula os vetores u-v e u+v
    u_minus_v = u - v
    u_plus_v = u + v
    
    # Verifica se u-v é ortogonal a u+v
    if np.dot(u_minus_v, u_plus_v) == 0:
        print("A segunda afirmação é verdadeira para os vetores:")
        print("u =", u)
        print("v =", v)
    else:
        print("A segunda afirmação é falsa para os vetores:")
        print("u =", u)
        print("v =", v)
else:
    print("A segunda afirmação não se aplica aos vetores:")
    print("u =", u)
    print("v =", v)

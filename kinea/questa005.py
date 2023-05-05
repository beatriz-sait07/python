import math

# Definir os valores de correlação e variância
corr = 0.45
var_x = 2
var_y = 6

# Calcular a covariância
cov = corr * math.sqrt(var_x) * math.sqrt(var_y)

# Imprimir o resultado
print(f"A covariância entre X e Y é igual a {cov:.3f}")

count = 0
for i in range(1, 1000001):
    if i % 7 == 0 or i % 13 == 0:
        count += 1

print("Existem", count, "números entre 1 e 1000000 que são divisíveis por 7 ou 13.")

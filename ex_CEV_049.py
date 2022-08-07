num = int(input("digite um numero: "))
for tabuada in range(0, 11):
    print('{:2} x {} = {:2}'.format(tabuada, num, (num * tabuada)))
print('\nesta eh a tabuado do {}'.format(num))

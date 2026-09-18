import os
os.system('cls')

a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))
c = float(input('Digite o valor de C: '))
soma = a + b

if soma > c:
    print('A soma é maior que C', '=', c)
else:
    print('A soma é menor que C', '=', c)
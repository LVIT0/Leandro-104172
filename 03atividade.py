import os
os.system('cls')

a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))

if a == b:
    c = a + b
    print('O valor de C é: ', c)
else:
    c = a * b
    print('O valor de C é: ', c)

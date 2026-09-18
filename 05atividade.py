import os
os.system('cls')

operacao = str(input('DIgite a operação desejada: '))
a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))

if operacao == '+':
    soma = a + b
    print('O resultado é: ', soma)
elif operacao == '-':
    sub = a - b
    print('O resultado é: ', sub)
elif operacao == '*':
    multi = a * b
    print('O resultado é: ', multi)
elif operacao == '/':
    div = a / b
    print('O resultado é: ', div)
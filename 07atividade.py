import os
os.system('cls')

nome = str(input('Digite o nome do produto: '))
quantidade = float(input('Digite a quantidade do produto: '))
preco = float(input('Digite o valor do produto: '))

total = quantidade * preco

if quantidade <= 5:
    desconto = 0.02
    total_pagar = total - desconto
    print('O valor é de: ', 'R$', total_pagar)
elif quantidade > 5 and quantidade <= 10:
    desconto = 0.03
    total_pagar = total - desconto
    print('O valor é de: ', 'R$', total_pagar)
elif quantidade > 10:
    desconto = 0.05
    total_pagar = total - desconto
    print('O valor é de: ', 'R$', total_pagar)
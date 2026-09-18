import os
os.system('cls')


print('Verde   R$ 10,00')
print('Azul	R$ 20,00')
print('Amarelo R$ 30,00')
print('Vermelho R$ 40,00')

verde = 10
azul = 20
amarelo = 30
vermelho = 40

cd = str(input('Digite qual CD deseja comprar de acordo com sua cor: '))

if cd == 'verde':
    print('o preço é:', 'R$', verde )
elif cd == 'azul':
    print('o preço é:', 'R$', verde )
elif cd == 'amarelo':
    print('o preço é:', 'R$', amarelo )
elif cd == 'vermelho':
    print('o preço é:', 'R$', vermelho )

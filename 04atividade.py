import os
os.system('cls')

morango = float(input('Quantos kilos de morango irá comprar: '))
maca = float(input('Quantos kilos de maçã irá comprar: '))

if morango <= 5:
    valor_morango = morango * 2.5
else:
    valor_morango = morango * 2.2

if maca <= 5:
    valor_maca = maca * 1.8
else:
    valor_maca = maca * 1.5

total_kg = morango + maca
valor_total = valor_morango + valor_maca
if total_kg >= 10 or valor_total > 15:
    valor_total * 0.10
    print('O valor pago é:', 'R$', valor_total)
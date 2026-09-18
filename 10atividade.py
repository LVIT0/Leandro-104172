import os
os.system('cls')

print('Álcool	Até 25 litros	 10%')
print('Álcool	Até 25 litros	 10%')
print('Gasolina Até 25 litros	 15%')
print('Gasolina Acima de 25 litros 30%')

gaso = str(input('Digite qual o tipo de gasolina deseja abastecer. Coloque (G) para gasolina e (A) para álcool: ')).upper()
litros = float(input('Digite o valor de litros para abastecer: '))
a = 3.79
g = 6.59

if gaso == 'G' and litros <= 25:
    total1 = litros * g
    desconto = total1 - (total1 * 0.15)
    print(f'O valor é de: {desconto:.2f}')

elif gaso == 'G' and litros > 25:
    total1 = litros * g
    desconto = total1 - (total1 * 0.30)
    print(f'O valor é de: {desconto:.2f}')

elif gaso == 'A' and litros <= 25:
    total1 = litros * a
    desconto = total1 - (total1 * 0.10)
    print(f'O valor é de: {desconto:.2f}')

elif gaso == 'A' and litros > 25:
    total1 = litros * a
    desconto = total1 - (total1 * 0.20)
    print(f'O valor é de: {desconto:.2f}')

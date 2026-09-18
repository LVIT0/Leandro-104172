import os
os.system('cls')

numero1 = float(input('Digite a primeira nota: '))
numero2 = float(input('Digite a segunda nota: '))

media = (numero1 + numero2) / 2

if media >= 6:
    print('Parabéns, Aprovado!')
elif media >= 4.1:
    print('Recuperação!')
elif media <= 4:
    print('Reprovado!')
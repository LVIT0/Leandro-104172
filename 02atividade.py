import os
os.system('cls')

nome = str(input('Digite seu nome: '))
sexo = str(input('Digite seu sexo colando (M) para masculino e (F) para feminino: ')).upper()
est_civil = str(input('Digite seu estado civil: ')).upper()
f = 'Feminino'
if sexo == 'F' and est_civil == 'CASADA':
    tempo = float(input('Digite seu tempo de casada em anos: '))
    print('Seu nome é:', nome)
    print('Seu sexo é:', sexo)
    print('Seu estado civil é:', est_civil)
    print('Seu tempo de casada é de: ', tempo, 'anos')
else: print
import os
os.system('cls')

renda = float(input('Digite o  valor da sua renda: '))
emprestimo = float(input('Digite o valor do empréstimo: '))
num_prestacoes = int(input('Digite a quantidade de pestações desejadas: '))
prestacao = emprestimo / num_prestacoes

if emprestimo <= renda * 10 and prestacao <= renda * 0.3:
    print('O emprestimo pode ser cincedido. ')
    print('O valor do emprestimo é de: ', emprestimo)
    print('O valor da prestação é de: ', prestacao)
else:
    print('O empréstimo não pode ser concedido. ')
'''Escreva um algoritmo que receba o valor do salário fixo e o valor das vendas efetuadas pelo vendedor de uma empresa,
ambos informados pelo usuário. Sabendo-se que a empresa paga 5% sobre um total de até R$1.500,00,
mais 7% sobre o valor que ultrapassar esse montante (diferença), o programa deve calcular e imprimir o salário total final do vendedor'''

salario = float(input('Informe o salário fixo: '))
vendas = (float(input('Informe as vendas realizadas: ')))

taxaA = 0.05
taxaB = 0.07
comissao = 0

if (vendas <= 1500):
    comissao = vendas*taxaA
else:
    comissao = (1500*taxaA) + ((vendas-1500)*taxaB)

salarioTotal = salario+comissao

print('O salário total final do vendedor é de R${:.2f}.'.format(salarioTotal))
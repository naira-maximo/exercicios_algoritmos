'''Sabendo que a população do país A é da ordem de 15000 habitantes com uma taxa de crescimento de 10%,
que a população do país B é de 45000 habitantes com uma taxa de crescimento de 5%,
e que a população do país C é de 65000 habitantes com uma taxa de crescimento de 2,5%, escreva um programa que calcule e imprima:
* Em quantos anos a população A igualará ou ultrapassará a população B; e
* Em quantos anos a população A ultrapassará a população C em 23%'''

pop_a = 15000
pop_a1 = 15000
pop_b = 45000
pop_c = 65000

tax_a = 0.1
tax_b = 0.05
tax_c = 0.025

ano = 0
ano1 = 0

while(pop_a <= pop_b):
    pop_a = (pop_a*tax_a) + pop_a
    pop_b = (pop_b*tax_b) + pop_b
    ano += 1

while(pop_a1 < ((pop_c*0.23)+pop_c)):
    pop_a1 = (pop_a1*tax_a) + pop_a1
    pop_c = (pop_c*tax_c) + pop_c
    ano1 += 1

print('A população A igualará ou ultrapassará a população B em {} anos, tendo {:.0f} habitantes a população A e {:.0f} a população B'.format(ano,pop_a,pop_b))
print('A população A ultrapassará a população C em 23% em {} anos, tendo {:.0f} habitantes a população A e {:.0f} a população C'.format(ano1,pop_a,pop_c))
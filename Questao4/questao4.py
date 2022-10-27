'''Elabore um algoritmo que leia 150 números inteiros e imprima:
* Qual o tamanho da maior sequência consecutiva de números em ordem crescente, assumindo como critério de desempate a soma dos números;
* Qual o tamanho da maior sequência consecutiva de números constantes, assumindo como critério de desempate o valor do número envolvido na sequência.'''

import random

anterior = 0
contador = 0
soma = 0
soma2 = 0
contador2 = 0

for i in range(0, 30):
    numero = int(random.randint(1, 5))
    print(numero)
    if numero != 1 and numero == anterior + 1:
        contador += 1
        soma += (numero + anterior)
        anterior = numero
        if contador > contador2:
            contador2 = contador
            soma2 = soma
        elif contador2 > contador:
            contador = 0
            soma = 0
    else:
        anterior = numero
        contador2 = contador
        soma2 = soma
        contador = 0
        soma = 0

if contador > contador2:
    if soma >= soma2:
        print(f'A maior sequência consecutiva de números em ordem crescente é {contador}, tendo como soma dos termos {soma}')
    else:
        print(f'A maior sequência consecutiva de números em ordem crescente é {contador}, 2 tendo como soma dos termos {soma2}')
elif contador2 > contador:
    if soma >= soma2:
        print(f'2 A maior sequência consecutiva de números em ordem crescente é {contador2}, tendo como soma dos termos {soma}')
    else:
        print(f'2 A maior sequência consecutiva de números em ordem crescente é {contador2}, 2 tendo como soma dos termos {soma2}')
else:
    print(f'Não houve sequência consecutiva de números em ordem crescente, sendo a contagem {contador} e {contador2}')

anterior = 0
valor = 0
valor2 = 0
contador = 0
contador2 = 0

for i in range(0, 30):
    numero = int(random.randint(1, 5))
    print(numero)
    if numero != 1 and numero == anterior:
        contador += 1
        valor = numero
        anterior = numero
        if contador > contador2:
            contador2 = contador
            valor2 = valor
        elif contador2 > contador:
            contador = 0
            valor = 0
        else:
            print('teste')
    else:
        anterior = numero
        contador2 = contador
        valor2 = valor
        contador = 0
        valor = 0

if contador > contador2:
    if valor >= valor2:
        print(f'A maior sequência consecutiva de números em ordem crescente é {contador}, tendo como soma dos termos {soma}')
    else:
        print(f'A maior sequência consecutiva de números em ordem crescente é {contador}, 2 tendo como soma dos termos {soma2}')
elif contador2 > contador:
    if valor >= valor2:
        print(f'2 A maior sequência consecutiva de números em ordem crescente é {contador2}, tendo como soma dos termos {soma}')
    else:
        print(f'2 A maior sequência consecutiva de números em ordem crescente é {contador2}, 2 tendo como soma dos termos {soma2}')
else:
    print(f'Não houve sequência consecutiva de números em ordem crescente, sendo a contagem {contador} e {contador2}')
'''Elabore um algoritmo que leia 150 números inteiros e imprima:
* Qual o tamanho da maior sequência consecutiva de números em ordem crescente, assumindo como critério de desempate a soma dos números;
* Qual o tamanho da maior sequência consecutiva de números constantes, assumindo como critério de desempate o valor do número envolvido na sequência.'''

anterior = 0  # Armazena o último número para comparação
contador = 0  # Quantidade de vezes que a condição é aceita (numero != 1 and numero == anterior + 1)
contador2 = 0  # Soma armazenada para comparação com a contagem vigente
soma = 0  # Soma da contagem vigente, para possível desempate
soma2 = 0  # Soma armazenada para comparação com a contagem vigente

for i in range(0, 150):
    numero = int(input('Insira um número inteiro: '))
    if numero == anterior + 1:
        if contador == 0:  # Sem essa função, a contagem fica com 1 a menos
            contador += 2
        else:
            contador += 1
        if soma == 0:  # Sem essa função, o primeiro número da sequência consecutiva é desprezado 
            soma += (numero + anterior)
        else:
            soma += numero
    else:
        if contador > contador2:  # Armazena a maior sequência como forma de comparação 
            contador2 = contador
            contador = 0
            soma2 = soma
            soma = 0
        elif contador == contador2:  # Caso a sequência 
            if soma > soma2:
                soma2 = soma
                soma = 0
                contador2 = contador
                contador = 0
            else:
                contador = 0
                soma = 0
        else:
            contador = 0
            soma = 0
    anterior = numero
if contador >= contador2:
    if soma >= soma2:
        print(f'A maior sequência consecutiva de números em ordem crescente é {contador}, tendo {soma} como a soma dos termos')
    else:
        print(f'A maior sequência consecutiva de números em ordem crescente é {contador}, tendo {soma2} como a soma dos termos')
elif contador2 > contador:
    if soma >= soma2:
        print(f'A maior sequência consecutiva de números em ordem crescente é {contador2}, tendo {soma} como a soma dos termos')
    else:
        print(f'A maior sequência consecutiva de números em ordem crescente é {contador2}, tendo {soma2} como a soma dos termos')
else:
    print(f'Não houve sequência consecutiva de números em ordem crescente, sendo a contagem {contador} e {contador2}')

anterior = 0  # Armazena o último número para comparação
contador = 0  # Quantidade de vezes que a condição é aceita (numero != 1 and numero == anterior + 1)
contador2 = 0  # Soma armazenada para comparação com a contagem vigente
valor = 0  # Número da contagem vigente, para possível desempate
valor2 = 0  # Número armazenado para comparação com a contagem vigente

for i in range(0, 150):
    numero = int(input('Insira um número inteiro: '))
    if numero == anterior:
        if contador == 0:  # Sem essa função, a contagem fica com 1 a menos
            contador += 2
            valor = numero
        else:
            contador += 1
            valor = numero
    else:
        if contador > contador2:  # Armazena a maior sequência como forma de comparação 
            contador2 = contador
            contador = 0
            valor2 = valor
            valor = 0
        elif contador == contador2:  # Caso a sequência 
            if valor > valor2:
                valor2 = valor
                valor = 0
                contador = 0
            else:
                contador = 0
        else:
            contador = 0
            valor = 0
    anterior = numero
if contador > contador2:
    print(f'A maior sequência consecutiva de números constantes é {contador}, sendo uma sequência de {valor}')
elif contador2 > contador:
    print(f'A maior sequência consecutiva de números constantes é {contador2}, sendo uma sequência de {valor2}')
elif contador == contador2:
    if valor >= valor2:
        print(f'A maior sequência consecutiva de números constantes é {contador}, sendo uma sequência de {valor}')
    elif valor < valor2:
        print(f'A maior sequência consecutiva de números constantes é {contador}, sendo uma sequência de {valor2}')
else:
    print(f'Não houve sequência consecutiva de números constantes, sendo a contagem {contador} e {contador2}')
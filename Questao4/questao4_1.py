import random

anterior = 0  # Armazena o número para a próxima tentativa do for
contador = 0  # Quantidade de vezes que a condição é aceita (numero != 1 and numero == anterior + 1)
contador2 = 0  # Soma armazenada para comparação com a contagem vigente
soma = 0  # Soma da contagem vigente, para possível desempate
soma2 = 0  # Soma armazenada para comparação com a contagem vigente

for i in range(0, 30):
    numero = int(random.randint(1, 5))
    print(numero)
    if numero != 1 and numero == anterior + 1:
        contador += 1
        soma += (numero + anterior)
        anterior = numero

    else:
        if contador > contador2:
            contador2 = contador
            anterior = numero
            soma2 = soma
            contador = 0
            soma = 0
        else:
            anterior = numero
            soma2 = soma

if contador >= contador2:
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

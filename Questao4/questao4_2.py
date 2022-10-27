import random

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
        print(f'A maior sequência consecutiva de números em ordem crescente é {contador}, tendo como soma dos termos {valor}')
    else:
        print(f'A maior sequência consecutiva de números em ordem crescente é {contador}, 2 tendo como soma dos termos {valor2}')
elif contador2 > contador:
    if valor >= valor2:
        print(f'2 A maior sequência consecutiva de números em ordem crescente é {contador2}, tendo como soma dos termos {valor}')
    else:
        print(f'2 A maior sequência consecutiva de números em ordem crescente é {contador2}, 2 tendo como soma dos termos {valor2}')
else:
    print(f'Não houve sequência consecutiva de números em ordem crescente, sendo a contagem {contador} e {contador2}')
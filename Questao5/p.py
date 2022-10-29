'''Escreva um algoritmo que calcule a seguinte sequência, fornecendo como saída o resultado de P,
dadas a respectiva entrada do usuário (sem utilizar vetor):
3. P = 2/pot(1/3) + 3/pot(3,3) + 5/pot(5,3) + 7/pot(7,3) + 11/pot(9,3) + ..., onde n corresponde ao número de termos da sequência,
sendo um número inteiro e positivo >= 50 informado pelo usuário (pot equivale a potenciação)'''

# Ler o número informado pelo usuário para a sequência P
print('\n3) P = 2/pot(1/3) + 3/pot(3,3) + 5/pot(5,3) + 7/pot(7,3) + 11/pot(9,3) + ...')
multiplos = 0
impar = 1
soma = 1
primo = 0
n = int(input('Defina o número de termos da sequência, sendo um número inteiro e positivo >= 50: '))
for numero in range(1, n+1):  # Quantidade de termos na sequência
    for i in range (1, n+1):
        if numero % i == 0 and numero != 1:
            multiplos += 1
            print(f'numero: {numero}')
            print(f'i: {i}')
            print(f'multiplos: {multiplos}')
        # conferir dados
    if multiplos == 2:
        primo = numero
        calculo = primo/(impar**3)
        print(f'primo {primo}')
        print(f'impar {impar}')
        impar += 2
        soma += calculo
print(f'Resultado da {numero}º soma da sequência é: {soma}')
# n = int(input('Defina o número de termos da sequência, sendo um número inteiro e positivo >= 50: '))
# for a in range(1, n+1):
#     for i in range(1, n+1):  # Identificar os números primos
#         if (a % i == 0):
#             multiplos += 1
#             if multiplos == 0:
#                 print(i)
#                 print(a)
#     print(f'Resultado da {a}ª soma da sequência é: {multiplos}')

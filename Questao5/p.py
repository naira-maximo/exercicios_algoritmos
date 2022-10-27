'''Escreva um algoritmo que calcule a seguinte sequência, fornecendo como saída o resultado de P,
dadas a respectiva entrada do usuário (sem utilizar vetor):
3. P = 2/pot(1/3) + 3/pot(3,3) + 5/pot(5,3) + 7/pot(7,3) + 11/pot(9,3) + ..., onde n corresponde ao número de termos da sequência,
sendo um número inteiro e positivo >= 50 informado pelo usuário (pot equivale a potenciação)'''

# Ler o número informado pelo usuário para a sequência P
print('\n3) P = 2/pot(1/3) + 3/pot(3,3) + 5/pot(5,3) + 7/pot(7,3) + 11/pot(9,3) + ...')
multiplos = 0
impar = 1
soma = 0
primo = 0
n = int(input('Defina o número de termos da sequência, sendo um número inteiro e positivo >= 50: '))
for numero in range(1, n+1):  # Quantidade de termos na sequência
    if numero > 1:
        for i in range(2, n):  # Identificar os números primos
            if (n % i == 0):
                multiplos += 1
        if multiplos == 0:
            primo = numero
    calculo = primo/(impar**3)
    print(f'primo {primo}')
    print(f'impar {impar}')
    impar += 2
    soma += calculo
print(f'Resultado da {numero}º soma da sequência é: {soma}')

        # for i in range(2, n):  # Identificar os números primos
        #             if (numero % i == 0):
        #                 print('teste')
        #                 multiplos += 1
        #         if multiplos == 0:
        #             calculo = numero/(impar**3)
        #             print(impar)
        #             impar += 2
        #             soma += calculo  2  0,1111111111  0,04   0,020408163265306  0,015089163237311
        # print(f'Resultado da {numero}º soma da sequência é: {soma}')
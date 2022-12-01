

# [Exercício 1] [DESAFIO] Escreva um programa que leia 5 valores e guarde-os dentro de uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = []
maior = 0
menor = 0
print('Quero 5 números!')
for i in range(0, 5):
    lista.append(int(input(f"Digite o {i+1}º número: ")))
    if i == 0:
        maior = menor = lista[i]
    if i > 0 and maior < lista[i]:
        maior = lista[i]
    if i > 0 and menor > lista[i]:
        menor = lista[i]

print()
print(f'Na lista coletada, a maior entrada foi {maior} na posição {lista.index(maior)}'
      f' e a menor entrada foi {menor} na posição {lista.index(menor)}')

# [Exercício 2] Escreva um programa que o usuário escreverá vários valores  numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, e em ordem crescente.

'''lista = []
temp = 0
while True:
    num = int(input('Entre com um valor inteiro: '))
    if num not in lista:
        lista.append(num)
        print('\033[32mValor acrescentado.\033[m')
    else:
        print('\033[31mValor já consta na lista.\033[m')
    continuar = str(input("Deseja continuar? [S/N] ")).upper().strip()[0]
    while continuar not in "SN":
        continuar = str(input("INVALIDO. Digitar 'S' ou 'N' ")).upper().strip()[0]
    if continuar == 'N':
        break

temp = 0
for i in range(0, len(lista)-1):
    for j in range(i+1, len(lista)):
        if lista[i] > lista[j]:
            temp = lista[i]
            lista[i] = lista[j]
            lista[j] = temp

print(f'\n\033[36mLista = {lista}\033[m')'''

# [Exercício 3] Escreva um programa que o user digite 5 valores numéricos
# e cadastre-os em uma lista, já na posição correta de inserção (SEM USAR O sort()).
# No final, mostre a lista ordenada na tela.

par = True
print('ENTRE COM 15 NÚMEROS INTEIROS:')
lista5 = []
lista5.append(int(input('1º: ')))
if lista5[0] % 2 == 0:
    par = True
    print(f'\033[36mAdicionado ao inicio da Lista\033[m')
else:
    par = False
    print(f'\033[33mAdicionado ao inicio da Lista\033[m')
for i in range(14):
    num = int(input(f'{i+2}º: '))
    while num in lista5:
        num = int(input(f'\033[31mElemento já na lista. Tente outro valor:\033[m '))
    if num % 2 == 0:
        par = True
    else:
        par = False
    if num >= lista5[len(lista5)-1]:
        if par:
            lista5.append(num)
            print(f'\033[36mAdicionado ao fim da Lista\033[m')
        else:
            lista5.append(num)
            print(f'\033[33mAdicionado ao fim da Lista\033[m')
    else:
        for elemento in lista5:
            if num < lista5[0] and par:
                lista5.insert(0, num)
                print(f'\033[36mAdicionado ao inicio da Lista\033[m')
                break
            elif num < lista5[0] and not par:
                lista5.insert(0, num)
                print(f'\033[33mAdicionado ao inicio da Lista\033[m')
                break
            elif num < elemento and par:
                lista5.insert(lista5.index(elemento), num)
                print(f'\033[36mAdicionado na posição {lista5.index(num)} da Lista\033[m')
                break
            elif num < elemento and not par:
                lista5.insert(lista5.index(elemento), num)
                print(f'\033[33mAdicionado na posição {lista5.index(num)} da Lista\033[m')
                break

print(lista5)
print(len(lista5))

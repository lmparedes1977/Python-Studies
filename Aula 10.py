

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


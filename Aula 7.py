# [Exercício 1] Escreva um programa que leia o sexo de uma pessoa, mas só aceite ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.


"""resposta = 'S'

while resposta == 'S':

    sexo = str(input("Por gentileza, informar sexo [M,F]: ")).upper().strip()[0]

    while sexo not in "MF":

        sexo = str(input("INFORMACAO INVALIDA. Por gentileza, informar sexo [M/F]: ")).upper().strip()[0]

    resposta = str(input("Deseja continuar? [S/N]: ")).upper().strip()[0]

    while resposta not in "SN":

        resposta = str(input("INFORMACAO INVALIDA. Deseja continuar? [M/F]: ")).upper().strip()[0]"""
from random import randint

# [Exercício 2] Escreva um programa que o computador vai “pensar” em um número inteiro entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar o número, mostrando no final quantos palpites foram necessários para vencer.

"""palpites = 1
numero_rand = randint(0, 10)
numero_jogador = int(input("Adivinhe o número! Digite um número entre 0 e 10: "))

while numero_jogador != numero_rand:

    palpites += 1
    numero_jogador = int(input("ERROOOUU! Tenta de novo:: "))

print(f"Feito!!! {numero_rand} na cabeça em {palpites} tentativas.")"""

# [Exercício 3] Escreva um programa que lerá dois valores do usuário e mostre um menu na tela dando as opções:
# [1] – somar, [2] – multiplicar, [3] – maior, [4] – novos números, [5] – sair do programa.
# Seu programa deverá realizar a operação solicitada em cada caso.

"""n1 = int(input('Vamos fazer algumas operações. Digite um número inteiro: '))
n2 = int(input('Digite mais um número inteiro: '))

opcao = [1,2,3,4,5]
resposta = 0
while resposta != 5:

    print("="*20)
    print("         MENU")
    print("="*20)
    print(" [1] - Somar")
    print(" [2] - Multiplicar")
    print(" [3] - Maior de todos")
    print(" [4] - Entrar com novos números")
    print(" [5] - Sair do programa")
    print("")
    resposta = int(input("Escolha a opção: "))
    print("")
    
    while resposta not in opcao:
        resposta = str(input("RESPOSTA INVÁLIDA. Escolha a opção: "))

    if resposta == 1:
        print("=" * 20)
        print(f"Soma: {n1} + {n2} = {n1+n2}")
        print("=" * 20)
    elif resposta == 2:
        print("=" * 20)
        print(f"Multiplicação: {n1} * {n2} = {n1*n2}")
        print("=" * 20)
    elif resposta == 3:
        print("=" * 20)
        print(f"O maior entre os números é o", n1 > n2 and n1 or n2)
        print("=" * 20)
    elif resposta == 4:
        n1 = int(input('Digite um novo número inteiro: '))
        n2 = int(input('Digite mais um número inteiro: '))
    print("")

print("Programa encerrado. OBRIGADO!")"""

# [Exercício 4] Escreva um programa que leia um número e calcule seu fatorial mostra da tela como exemplo a seguir.
# 5! = 5x4x3x2x1 = 120

"""num = int(input("Digite um numero inteiro, vamos descobrir seu fatorial: "))

while num < 0:
    num = int(input("Preciso de um numero inteiro positivo: "))
    num_inicial = num

fatorial = 1

print(f'Fatorial de {num}: {num}', end="")

for i in range(num-1):
    fatorial = fatorial*num
    num = num - 1
    print(f'X{num}', end="")

print(f' = {fatorial}.')"""

# [Exercício 5] Escreva um programa que leia o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da PA. (USE WHILE)

"""primeiro_termo = int(input("Digite o primeiro termo de uma PA: "))
razao = int(input("Digite a razão da PA: "))
i = 1

print(f"10 primeiros termos de PA zarão {razao}: {primeiro_termo}", end="")
while i <= 9:
    print(f', {primeiro_termo + razao * i}', end=" ")
    i +=1

print(".")"""

# [Exercício 6] Escreva um programa que melhore o exercício 5, perguntando se ele quer mostrar mais alguns termos.
# O programa encerra quando ele disser que quer mostrar 0 termos.

"""primeiro_termo = int(input("Digite o primeiro termo de uma PA: "))
razao = int(input("Digite a razão da PA: "))
i = 1
proximo_termo = 0
n_termos = 10
print(f"10 primeiros termos de PA zarão {razao}: {primeiro_termo}", end="")
while i < n_termos:
    proximo_termo = primeiro_termo + razao * i
    print(f', {proximo_termo}', end=" ")
    i +=1

print(".")

mais_termos = int(input("Queres mostrar mais alguns termos? Digite quantos: "))
n_termos += mais_termos

while mais_termos != 0:

    print(f"Os próximos {mais_termos} termos da PA são : ", end="")
    i = 1
    while i <= mais_termos:
        proximo_termo = proximo_termo + razao
        print(f'{proximo_termo}, ', end=" ")
        i += 1

    mais_termos = int(input("Queres mostrar mais alguns termos? Digite quantos: "))
    n_termos += mais_termos

print(f"Feito! Imprimimos {n_termos} termos.")"""

# [Exercício 7] Escreva um programa que leia um número n inteiro e mostre na tela os n primeiros
# números da Sequência de Fibonacci da seguinte forma mostrada a seguir.
# Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

"""n_termos = int(input("Vamos imprimir um Fibonacci (de novo)? Quantos termos: "))
i = 0
j = 1
k = 0

print(f"{i}", '\033[0;31m->\033[m', f'{j} ', end="")
while k < n_termos-2:
    fibonacci = i + j
    i = j
    j = fibonacci
    print('\033[0;31m->\033[m', f'{fibonacci} ', end="")
    k += 1

# [Exercício 8] Escreva um programa que leia vários números inteiros e só pare quando o usuário digitar o valor 999.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles."""

"""soma = contador = num = 0
num = int(input("Digite um número inteiro [999 para encerrar]"))
while num != 999:
    soma += num
    contador += 1
    num = int(input("Digite um número inteiro [999 para encerrar]"))

print(f"Foram digitados {contador} números, e a soma dos mesmos perfaz {soma}.")"""

# [Exercício 9] Escreva um programa que leia vários números. No final, mostre a média entre todos os valores
# e qual foi o maior e o menor valores lido. O programa deve perguntar ao usuário se ele quer ou não continuar
# a digitar valores.
num = i = maior = menor = soma = 0

"""while True:
    num = int(input("Digite um número: "))
    if maior < num:
        maior = num
    if i == 0:
        menor = num
    elif menor > num:
        menor = num
    soma += num
    i += 1
    continua = str(input("Deseja continuar? [S/N]: ")).upper()
    while continua != 'S' and continua != 'N':
        continua = str(input("Resposta inválida. Deseja continuar? [S/N] ")).upper()
    if continua == 'N':
        break

print(f'Saldo da parada:\n'
      f'Total de entradas foi {i}\n'
      f'Maior número foi {maior}\n'
      f'menor número foi {menor}\n'
      f'Média geral dos números é {soma/i:.2f}  ')"""






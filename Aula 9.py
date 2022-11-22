from random import randint

# [Exercício 1] Escreva um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso,
# de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

'''contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
            'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    resp = int(input('Digite um número de 0 a 20 que vou escrevê-lo por extenso. [999 para sair]: '))
    if resp == 999:
        break
    while resp < 0 or resp > 20:
        resp = int(input('IVÁLIDO. Digite um número de 0 a 20 que vou escrevê-lo por extenso. [999 para sair]: '))
    print(contagem[resp])'''

# [Exercício 2] Escreva um programa que uma tupla com uma “lista de tops”.
# (Ex: Campeonato Brasileiro de Futebol, ou os países que mais ricos do mundo e etc). Depois mostre:
# 1)	A penas os 5 primeiros colocados;
# 2)	Os últimos 4 colocados;
# 3)	Imprimir eles na tela com todos em ordem alfabética;
# 4)	Em que posição estará um dos itens a sua escolha.

lista = ['Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Atlético Paranaense', 'Atletico Mineiro',
         'Fortaleza', 'Sao Paulo', 'America MG', 'Botafogo', 'Santos',  'Goias', 'Bragantino', 'Coritiba', 'Cuiaba',
         'Ceara', 'Atletico Goianiense', 'Avai', 'Juventude']

'''txt = 'TABELA FINAL BRASILEIRÃO 2022'
tamanho = len(txt)
p = tamanho + 25

while True:
    print("=" * p)
    print(f"{txt:^{p}}")
    print("=" * p)
    print(' 1) A penas os 5 primeiros colocados')
    print(' 2) Os últimos 4 colocados')
    print(' 3) Imprimir eles na tela com todos em ordem alfabética')
    print(' 4) Em que posição estará um dos itens a sua escolha')
    print("=" * p)
    opcao = int(input(' ESCOLHA ENTRE AS OÇÕES [999 para sair]: '))
    if opcao == 999:
        print('   FEITO!')
        break
    while opcao < 0 or opcao > 4:
        opcao = int(input(' INVALIDO. ESCOLHA DE 1 A 4: '))
    print()
    if opcao == 1:
        print(lista[0:5])
        for item in range(0, 5):
            print(lista[item])
    elif opcao == 2:
        print(lista[len(lista)-4:])
        for item in range(len(lista)-4, len(lista)):
            print(lista[item])
    elif opcao == 3:
        ord_alfabetica = sorted(lista)
        print(ord_alfabetica)
        for item in ord_alfabetica:
            print(item)
    elif opcao == 4:
        print(lista)
        posicao = str(input('Escolha um item, darei a posição: '))
        while posicao not in lista:
            posicao = str(input('INVALIDO. Escolha um item, darei a posição: '))
        print(f'Posicao do item {posicao}: {lista.index(posicao)}')
    continuar = input('Deseja continuar? [S/N]').upper()
    while continuar != 'S' and continuar != 'N':
        continuar = input('INVALIDO. Deseja continuar? [S/N]').upper()
    if continuar == 'N':
        print('   FEITO!')
        break'''

# [Exercício 3] Escreva um programa que vai gerar cinco números aleatórios e colocar dentro em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

tup = tuple([randint(1, 50) for i in range(5)])

print(f'Tupla criada aleatoriamente: {tup}')
print(f'Maior número da tupla: {max(tup)}')
print(f'Menor número da tupla: {min(tup)}')
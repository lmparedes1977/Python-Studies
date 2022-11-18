# [Exercício 1] Escreva um programa que leia vários números inteiros e só pare quando o usuário digitar o valor 999.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles.

'''i = soma = 0
while True:
    num = int(input('Digite um número: [999 para sair] '))
    if num == 999:
        break
    soma += num
    i += 1

print(f'Beleza! Foram digitados {i} números e soma deles é {soma}.')'''
from random import randint

# [Exercício 2] Escreva um programa que mostre a tabuada de vários números, um de cada vez,
# para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for zero.

"""while True:
    print('='*30)
    print('     GERADOR DE TABUADA')
    print('=' * 30)

    num = int(input("Escolha o número: [0 para sair] "))
    print('=' * 30)
    if num == 0:
        break
    for i in range(1, 11):
        print(f'   {i} X {num} = {i*num}')


print('='*30)
print('      FIM DO PROGRAMA')
print('=' * 30)"""

# [Exercício 3] Escreva um programa que jogue par ou impar com o computador.
# O jogo só será interrompido quando o jogador PERDER, mostrando o total de
# vitórias consecutivas que ele conquistou no final do jogo.

'''conseq = maior = 0
while True:
    par_ou_impar = ['P', 'I']
    print("-"*60)
    humano = str(input("Par ou Impar! Digite 'P' para PAR ou 'I' para IMPAR': ")).upper()
    print("-" * 60)
    while humano not in "PI":
        humano = str(input("INVALIDO. 'P' para PAR ou 'I' para IMPAR': ")).upper()
    numero_humano = int(input("Mostre o número: "))
    numero_maquina = randint(1, 2)
    print(f'Número da máquina: {numero_maquina}')
    if (numero_maquina + numero_humano) % 2 == par_ou_impar.index(humano):
        print("Ganhou!")
        conseq += 1
    else:
        print("-" * 60)
        print(f"Perdeu, fim de jogo! {conseq} vitórias consecutivas.")
        break'''

# [Exercício 4] Escreva um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# 1)	Quantas pessoas tem mais de 18 anos;
# 2)	Quantos homens foram cadastrados;
# 3)	Quantas mulheres tem menos de 20 anos.

'''novinha = homi = over18 = 0
print("=" * 30)
print('          CADASTRAMENTO')
print("=" * 30)
while True:
    sexo = str(input('Sexo: [M/F] ')).upper()
    while sexo not in 'MF':
        sexo = str(input('INVALIDO. Digite [M/F]: ')).upper()
    idade = int(input('Idade: '))
    if sexo == 'F' and idade < 20:
        novinha += 1
    elif sexo == 'M':
        homi += 1
    if idade > 18:
        over18 += 1
    continuar = str(input('Deseja continuar: [S/N] ')).upper()
    print("=" * 30)
    while continuar not in 'SN':
        continuar = str(input('INVALIDO. Deseja continuar: [S/N] ')).upper()
    if continuar == 'N':
        print(f'TOTAL DE PESSOAS COM MAIS DE 18 ANOS: {over18}')
        print(f'TOTAL DE HOMENS: {homi}')
        print(f'TOTAL DE MULHERES COM MENOS DE 20 ANOS {novinha}')
        print('==========FIM DA APLICAÇÃO===========')
        break'''

# [Exercício 5] Escreva um programa que leia o nome e preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar. No final, mostre:
# 1)	Qual é o total gasto na compra;
# 2)	Quantos produtos custam mais de R$ 1000.
# 3)	Qual é o nome do produto mais barato.

'''total = i = mais_q_mil = soma = 0
mais_barato = ''
lista_compras = []
print("=" * 30)
print('       VÁRIOS PRODUTOS')

while True:
    print("=" * 30)
    lista_compras.append(str(input('Digite o nome do produto: ')))
    lista_compras.append(int(input('Digite o preço do produto: ')))
    preco_menor = lista_compras[1]
    if preco_menor > lista_compras[i+1]:
        preco_menor = lista_compras[i+1]
        mais_barato = lista_compras[i]
    if lista_compras[i+1] > 1000:
        mais_q_mil += 1
    soma += lista_compras[i+1]
    i += 2
    print("=" * 30)
    continuar = str(input('Deseja contnuar? [S/N] ')).upper()
    while continuar not in 'SN':
        continuar = str(input('INVALIDO. Deseja contnuar? [S/N] ')).upper()
    if continuar == 'N':
        print("=" * 30)
        print(f'1)	Qual é o total gasto na compra: {soma}')
        print(f'2)	Quantos produtos custam mais de R$ 1000: {mais_q_mil}')
        print(f'3)	Qual é o nome do produto mais barato: {mais_barato}')
        break'''

# [Exercício 6] Escreva um programa que simule o funcionamento de um caixa eletrônico.
# O usuário informa o quanto deverá ser sacado (inteiro) e o programa retornará quantas
# cédulas de cada valor serão entregues. Considere que só há cédulas de 50, 20, 10 e 1.

'''cedula50 = cedula20 = cedula10 = cedula1 = 0
while True:
    print('=' * 45)
    print('           CAIXA ELETRÔNICO SENAC')
    print('=' * 45)
    print('    CÉDULAS DE R$ 50, R$ 20, R$ 10 E R$ 1')
    print('=' * 45)
    saque = int(input('Quanto deseja sacar: '))
    print('=' * 45)
    cedula50 = saque // 50
    cedula20 = (saque % 50) // 20
    cedula10 = ((saque % 50) % 20) // 10
    cedula1 = ((saque % 50) % 20) % 10
    print('             RETIRE O DINHEIRO')
    print()
    if cedula50 > 0:
        print(f'    {cedula50} cedulas de R$ 50')
    if cedula20 > 0:
        print(f'    {cedula20} CEDULA(S) DE R$ 20')
    if cedula10 > 0:
        print(f'    {cedula10} CEDULA(S) DE R$ 10')
    if cedula1 > 0:
        print(f'    {cedula1} CEDULA(S) DE R$ 1')
    print('=' * 45)
    print()
    contiuar = str(input("DESEJA REALIZAR NOVO SAQUE? [S/N]")).upper()
    while contiuar not in 'SN':
        contiuar = str(input("INVAILDO. DESEJA REALIZAR NOVO SAQUE? [S/N]")).upper()
    if contiuar == 'N':
        break
print('=' * 45)
print('              TENHA UM BOM DIA')'''
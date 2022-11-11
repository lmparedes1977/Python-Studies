import datetime
import time
import unicodedata

# [Exercício 1] Escreva um programa que faça a contagem regressiva de 10 até 0 com uma pausa de 1 segundo entre eles.

"""for i in range(10, 0, -1):
    print(i)
    time.sleep(1)"""

# [Exercício 2] Escreva um programa que mostre todos os números pares que estão entre 1 e 50.

"""for i in range(1, 51):
    if i % 2 == 0:
        print(i)"""

# [Exercício 3] Escreva um programa que calcule a soma entre todos os números ímpares que são
# múltiplos de três e que se encontram no intervalo de 1 até 500.

'''soma = 0
for i in range(1, 501):
    if i % 2 != 0 and i % 3 == 0:
        print(i)
        soma += i
print("Soma dos ímpares divisíveis por 3 entre 1 e 500:", soma)'''

# [Exercício 4] Escreva um programa que leia um número do usuário e retorne a tábuada desse número.

"""n = int(input("Digite um número, te retorno a tabuada dele: "))
for i in range(1, 11):
    print(f'{i} X {n} = {i * n}')"""

# [Exercício 5] Escreva um programa que leia 6 números inteiros do usuário e mostre
# a soma apenas daqueles que forem pares, Se o valor for ímpar, desconsidere-o.

"""soma = 0
for i in range(0, 6):
    n = int(input("Digite um número inteiro, vou somar os pares: "))
    if n % 2 == 0:
        soma += n
print(f'A soma dos números pares digitados é {soma}.')"""

# [Exercício 6] Escreva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

"""prim_termo = int(input("Digite o primeiro termo de uma progressão aritmética: "))
razao = int(input("Agora digite a razão da progressão aritmética: "))
for i in range(0, 10):
    print(f'{prim_termo + razao * i}')
print("Progressão geométrica com os mesmos termos:")
for i in range(0, 10):
    print(f'{prim_termo * (razao ** i)}')"""

# [Exercício 7] Escreva um programa que leia um número inteiro e diga se ele é primo ou não.

"""n = int(input("Digite um número, vamos ver se ele é um número primo: "))
p = 0
for i in range(1, n+1):
    if n % i == 0:
        print(f'\033[0;31m{i}\033[m', end=' ')
        p += 1
    else:
        print(f'\033[0;33m{i}\033[m', end=' ')
print("")
print('\033[0;34mÉ PRIMO!\033[m' if p == 2 else "\033[0;31mNÂO\033[m É \033[0;34mPRIMO!\033[m")"""

# [Exercício 8] Escreva um programa que leia uma frase qualquer e diga se ela é um PALÍNDROMO,
# desconsiderando os espaços e a acentuação.
# Ex:
# 1)	“APOS A SOPA”
# 2)	“A SACADA DA CASA”
# 3)	“A TORRE DA DERROTA”
# 4)	“O LOBO AMA O BOLO”
# 5)	“ANOTARAM A DATA DA MARATONA”

import unicodedata

"""
# frase = str(input("Digite uma frase sem acentos, vamos ver se é um palíndromo: ")).upper()

frase = unicodedata.normalize("NFD", str(input("Digite uma frase sem acentos, vamos ver se é um palíndromo: ")))\
    .encode("ascii", "ignore").decode("utf-8").upper()

# frase = frase.encode("ascii", "ignore")
# frase = frase.decode("utf-8")

frase_limpa = ("".join(frase.split()))
frase_inv = frase_limpa[::-1]

if frase_limpa == frase_inv:
    print(f'A frase "{frase}" é palíndromo')
else:
    print(f'A frase "{frase}" NÂO é palíndromo')"""

# [Exercício 9] Escreva um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas delas ainda não atingiram a maioridade e quantas já são maiores.

"""maiores = 0
menores = 0

for i in range(0, 7):
    ano_nasc = int(input("Digite o ano do seu nascimento: "))
    if datetime.date.today().year - ano_nasc >= 18:
       maiores += 1
    else:
       menores += 1

print(f"{maiores} pessoas são maiores de idade, {menores} pessoas tem menos de 18 anos.")"""

# [Exercício 10] Escreva um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e menor peso lidos.

"""maior = 0
menor = 0

for i in range(0, 5):
    peso = float(input("Digite o peso: "))
    if i == 0:
        maior = peso
        menor = peso
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso

print(f'O maior peso digitado foi {maior:.3f} Kg, o menor foi {menor:.3f}Kg.')"""

# [Exercício 11] Escreva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre:
# 1) A média de idade do grupo;
# 2) Qual é o nome do homem mais velho;
# 3) Quantas mulheres têm menos de 20 anos.

"""nomes = []
idades = []
sexos = []
media_idades = 0
mais_velho = 0
menos_de_20 = 0

for i in range(0, 4):
    nomes.insert(i, str(input(f"Digite o {i+1}º nome: ")))
    idades.insert(i, int(input(f"Digite a {i+1}º idade: ")))
    sexos.insert(i, str(input(f"Digite o {i+1}º sexto [M/F]: ")).upper())
    media_idades += idades[i]
    if sexos[i] == "M" and idades[mais_velho] < idades[i]:
        mais_velho = i
    elif sexos[i] == "F" and idades[i] < 20:
        menos_de_20 += 1

print(f'Bem, vamos lá: a idade média do grupo é {media_idades/4};\n'
      f'O homem mais velho se chama {nomes[mais_velho]};\n'
      f'{menos_de_20} mulheres tem menos de 20 anos de idade.\n'
      f'Obrigado!')"""

import random
import datetime

'''nome = "Leonardo"
nome_inverso = nome[::-1]
print(nome_inverso)'''

# [Exercício 1] Escreva um programa que o computador pensará em um número entre 0 e 5.
# Em seguida, o usuário deverá adivinhar esse valor. Caso o usuário acerte,
# retorne “VENCEU”, caso perca, retorne “PERDEU”.

"""num = int(input("Digita um número entre 0 e 5: "))
print(random.randint(0,5))
print("ACERTOU!" if random.randint(0, 5) == num else "ERROU!")"""

# [Exercício 2] Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80 Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

"""pontos_carteira = 0
multa = 0

while pontos_carteira <= 40:
    velocidade = random.randint(60, 100)
    if velocidade > 80:
        pontos_carteira += 7
        multa += 880.01
        print(f'Veiculo ABC0I23 ultrapassou a velocidade máxima de 80Km/h em {datetime.date.today()}.\n'
              f'Atingiu {velocidade}Km/h. Multa de de R$ 7 e 7 pontos na CNH.\n'
              f'Saldo da multas: R$ {multa},00. Pontuação CNH: {pontos_carteira}.\n'
              f'')"""

# [Exercício 3] Escreva um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

"""number = int(input("Vamos ver se par ou ímpar. Digita aí: "))

print("PAR!" if number % 2 == 0 else "ÍMPAR!")"""

# [Exercício 4] Escreva um programa que pergunte a distância de uma viagem em Km.
# Calcule e peça o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200Km e R$ 0,45 para viagens mais longas.

"""distancia = int(input("Venda de passagens. Digite a distância do seu destino [km]: "))

print("Sua passagem custará", f'R$ {(distancia * 0.5):.2f}' if distancia <= 200 else f'R$ {(distancia * 0.45):.2f}.')"""

# [Exercício 5] Escreva um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

"""ano = int(input("Digite um ano, vou te dizer se é(será) bissexto: "))

print(f'{ano}', "é bissexto" if ano % 4 == 0 else "não é bissexto.")"""

# [Exercício 6] Escreva um programa que leia três números e mostre qual é o maior e qual é o menor.

"""i = 0
maior = 0
menor = 0
while i <= 2:
    n = int(input("Digita um número: "))
    if i == 0:
        maior = n
        menor = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n
    i += 1

print(f'O maior digitado foi {maior} e o menor foi {menor}.')"""

# [Exercício 7] Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

"""salario = float(input("Digite seu salário, vamos calcular seu aumento: "))

print("Seu eu aumento foi de", f'10%, passando para R$ {(salario * 1.1):.2f}' if salario > 1250 else f'15%, passando para R$ {(salario * 1.15):.2f}' )"""

# [Exercício 8] Escreva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo.

"""ladoab = int(input("Digite a medida de um segmento de reta, vamos tentar formar um triângulo: "))
ladoac = int(input("Digite outra medida de segmento de reta: "))
ladobc = int(input("Digite outra medida de segmento de reta: "))
triangulo = True

if (ladoac > ladobc + ladoab) | (ladobc > ladoac + ladoab) | (ladoab > ladobc + ladoac):
    triangulo = False

print(f"É {triangulo} que os segmentos de reta de tamanho {ladoab}, {ladoac} e {ladobc} formam um triângulo.")"""







# [Exercício 5] A confederação Nacional de Natação precisa de um programa que leia
# o ano de nascimento de um atleta e mostre a sua categoria, de acordo com a sua idade:
# 1) Até 9 anos: MIRIM
# 2) Até 14 anos: INFANTIL
# 3) Até 19 anos: JUNIOR
# 4) Até 20 anos: SÊNIOR
# 5) Acima: MASTER
import datetime
import random

"""ano_atual = datetime.date.today().year
ano_nasc = int(input("Digite o ano em que o atleta nasceu: "))
idade = ano_atual - ano_nasc
if idade < 9:
    print(f"Idade do atleta: {idade} anos. Categoria MIRIM.")
elif idade < 14:
    print(f"Idade do atleta: {idade} anos. Categoria INFANTIL.")
elif idade < 19:
    print(f"Idade do atleta: {idade} anos. Categoria JUNIOR.")
else:
    print(idade < 20 and f"Idade do atleta: {idade} anos. Categoria SENIOR."
          or f"Idade do atleta: {idade} anos. Categoria MASTER.")"""

# [Exercício 6] Escreva um programa
# que leia os 3 lados de um triângulo e diga se eles formam ou não um triângulo.

"""ladoab = int(input("Digite o lado de um triangulo: "))
ladoac = int(input("Digite outro lado de um triangulo: "))
ladobc = int(input("Digite o último lado de um triangulo: "))

if ladoab < ladoac + ladobc and ladobc < ladoac + ladoab and ladoac < ladobc + ladoab:
    print(f"As retas de tamanho {ladoab}, {ladoac} e {ladobc} podem formar um triangulo.")
else:
    print(f"As retas de tamanho {ladoab}, {ladoac} e {ladobc} não formam um triangulo.")"""

# [Exercício 7] Refaça o exercício 6, mas acrescentando se o triângulo, caso seja formado,
# é: EQUILÁTERO, ISÓCELES ou ESCALENO.

"""ladoab = int(input("Digite o lado de um triangulo: "))
ladoac = int(input("Digite outro lado de um triangulo: "))
ladobc = int(input("Digite o último lado de um triangulo: "))
tipo_triangulo = ""

if ladoab < ladoac + ladobc and ladobc < ladoac + ladoab and ladoac < ladobc + ladoab:
    if ladoab == ladoac and ladoac == ladobc:
        tipo_triangulo = "EQUILÁTERO"
    elif ladoab == ladoac or ladoab == ladobc or ladobc == ladoac:
        tipo_triangulo = "ISÓCELES"
    else:
        tipo_triangulo = "ESCALENO"
    print(f"As retas de tamanho {ladoab}, {ladoac} e {ladobc} podem formar um triangulo {tipo_triangulo}.")
else:
    print(f"As retas de tamanho {ladoab}, {ladoac} e {ladobc} não formam um triangulo.")"""

# [Exercício 8] Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# 1) À vista dinheiro/cheque: 10% de descontoç;
# 2) À vista no cartão: 5% de desconto;
# 3) Em até 2X no cartão: preço normal;
# 4) 3X ou mais no cartão: 20% de juros.

"""print("=" * 50)
print("               !  LOJÃO DAS IDE's !")
print("=" * 50)
print(" [1] - VSCODE:  R$ 3000,00")
print(" [2] - PYCHARM: R$ 0,50")
print("=" * 50)
print(" [1] - À vista dinheiro/cheque: 10% de desconto")
print(" [2] - À vista no cartão: 5% de desconto")
print(" [3] - Em até 2X no cartão: preço normal")
print(" [4] - 3X ou mais no cartão: 20% de acréscimo")
print("=" * 50)

produto = str(input("Digite o número do produto escolhido: "))
while produto != "1" and produto != "2":
    produto = str(input("Opção inválida. Digite o número do produto escolhido: "))

print("=" * 50)

condicao = str(input("Digite o número da condição de pagamento escolhida: "))
while condicao != "1" and condicao != "2" and condicao != "3" and condicao != "4":
    condicao = str(input("Opção inválida. Digite o número da condição de pagamento escolhida: "))

print("=" * 50)

preco = produto == "1" and 3000.00 or 0.50
ide = produto == "1" and "VSCODE" or "PYCHARM"

if condicao == "1":
    print(f"{ide}. Desconto de R$ {preco*0.10:.2f}, preço final R$ {preco * 0.9:.2f}.")
elif condicao == "2":
    print(f"{ide}. Desconto de R$ {preco * 0.05:.2f}, preço final R$ {preco * 0.95:.2f}.")
elif condicao == "3":
    print(f"{ide}. Preço final R$ {preco:.2f}.")
else:
    print(f"{ide}. Acréscimo de R$ {preco * 0.20:.2f}, preço final R$ {preco * 1.2:.2f}.")"""

# [Exercício 9] Escreva um programa que em que você jogue JoKenPo com o computador.

"""print("=" * 30)
print("   JoKenPo")
print("=" * 30)
print(" [1] - TESOURA")
print(" [2] - PEDRA")
print(" [3] - PANO")
print("=" * 30)
print("Joga contra a máquina!")
humano = int(input("Escolhe Tesoura, Pedra ou Pano [1, 2 ou 3]: "))
maquina = random.randint(1, 3)
jokenpo = [" ", "TESOURA", "PEDRA", "PANO"]

print("\n")
print(f"Humano escolhe {jokenpo[humano]}")
print(f"Máquina escolhe {jokenpo[maquina]}")

if maquina == humano:
    print(f"Empate!")
elif maquina == 1 and humano == 2:
    print(f"Humano vence Máquina!")
elif maquina == 1 and humano == 3:
    print(f"Máquina vence Humano!")
elif maquina == 2 and humano == 1:
    print(f"Máquina vence Humano!")
elif maquina == 2 and humano == 3:
    print(f"Humano vence Máquina!")
elif maquina == 3 and humano == 1:
    print(f"Humano vence Máquina!")
elif maquina == 3 and humano == 2:
    print(f"Máquina vence Humano!")"""

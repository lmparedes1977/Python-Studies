import datetime

# [Exemplo 1] Escreva um programa que leia um nome. Se o nome for igual ao seu, diga que o nome é muito bonito.
# Se o nome for Pedro, Maria ou Paulo, diga que é um nome muito comum no Brasil. Se for Ana, Cláudia,
# Jéssica ou Juliana, diga que é um belo nome feminino. Caso não satisfaça nenhum das condições anteriores,
# apenas informe que o nome é bem normal. No fim, retorne um bom dia com o nome do user.

"""nome = input("Digite o teu nome: ")
bonito = "Leonardo"
feminino = ["Ana", "Cláudia", "Jéssica", "Juliana"]
comum = ["Pedro", "Maria", "Paulo"]

if nome == bonito:
    print("Nóóóóóósssa, que nome MASSA!")
elif nome in feminino:
    print("Belo nome feminino tens.")
elif nome in comum:
    print("Nome muito comum no Brasil.") 
else:
    print("Nome bem normal...")

print(f"Bom dia {nome}!")"""

"""print(datetime.date.today())
print(datetime.date.today().day)
print(datetime.date.today().month)
print(datetime.date.today().year)"""

# [Exercício 1] Escreva um programa que aprove um empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário
# ou então o empréstimo será negado.

"""renda = float(input("Análise de crédito. Digite a renda mensal: "))
imovel = float(input("Valor de imóvel pretendido: "))
prazo = int(input("Prazo desejado [meses]: "))

parcela = imovel / prazo

if renda * 0.3 > parcela:
    print("Parabéns, Crédido Pré-Aprovado.")
else:
    print("Valor do imóvel incompatível com a renda ou prazo.")"""

# [Exercício 2] Escreva um programa que leia um número inteiro qualquer e peça ao usuário qual será a base de conversão:
# 1)	[1] – Binário
# 2)	[2] – Octal
# 3)	[3] – Hexadecimal

"""n_inteiro = int(input("Digita um número inteiro: "))
print("="*20)
print(" [1] - BINÁRIO")
print(" [2] - OCTAL")
print(" [3] - HEXADECIMAL")
print("="*20)
resposta = str(input("Digite sua opção: "))

while resposta != "1" and resposta != "2" and resposta != "3":
    resposta = input("Resposta invalida. Digite 1, 2 ou 3: ")

if resposta == "1":
    print(f'{n_inteiro} em Binário: {bin(n_inteiro)}.')
elif resposta == "2":
    print(f'{n_inteiro} em Octal: {oct(n_inteiro)}.')
else:
    print(f'{n_inteiro} em Hexadecimal: {hex(n_inteiro)}.')"""

# [Exercício 3] Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela a mensagem:
# 1)	“O primeiro valor é maior”
# 2)	“O segundo valor é maior”
# 3)	“Não existe valor maior, ambos são iguais”

"""numero1 = int(input("Comparação entre inteiros. Digite um número inteiro: "))
numero2 = int(input("Digite outro número inteiro: "))

if numero2 == numero1:
    print("3) Números de mesmo valor.")
else:
    print(numero1 > numero2 and "1) O primeiro valor é maior" or "2) O segundo valor maior")"""

# [Exercício 4] Escreva um programa que leia duas notas do aluno, calcule a sua média e diga:
# 1)	Média abaixo de 5: REPROVADO
# 2)	Entre 5 e 6.9: RECUPERAÇÃO
# 3)	Acima de 7: APROVADO

"""nota1 = int(input("Veredito final. Digite a primeira nota do aluno: "))
nota2 = int(input("Digite a segunda nota do aluno: "))
media = ( nota2 + nota1 ) / 2

if media >= 7:
    print("3) Acima de 7: APROVADO.")
else:
    print(media < 5 and "1) Méida abaixo de 5: REPROVADO " or "2) Média entre 5 e 6.9: EM RECUPERAÇÃO")"""

# [Exercício 5] A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre a sua categoria, de acordo com a sua idade:
# 1)	Até 9 anos: MIRIM
# 2)	Até 14 anos: INFANTIL
# 3)	Até 19 anos: JUNIOR
# 4)	Até 20 anos: SÊNIOR
# 5)	Acima: MASTER

"""ano_atual = datetime.date.today().year
ano_nasc = int(input("Digite o ano de nascimento do atleta: "))
idade = ano_atual - ano_nasc
if idade < 9"""

"""i = 1
j = 0
k = 0
l = 0
m = 0"""

"""lista = []
for i in range(1, 10):
    for j in range(0, 10):
        for k in range(0, 10):
            for l in range(0, 10):
                for m in range(0, 10):
                    if i+j+k+l+m == 43:                        
                        lista.append(str(i)+str(j)+str(k)+str(l)+str(m))


print(lista)
for i in range(0, len(lista)):
    if int(lista[i]) % 11 == 0:
        print(lista[i])"""


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



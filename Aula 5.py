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
                    if (i+j+k+l+m) == 43:                        
                        lista.append(str(i)+str(j)+str(k)+str(l)+str(m))


print(lista)
for i in range(0, len(lista)):
    if int(lista[i]) % 11 == 0:
        print(lista[i])"""



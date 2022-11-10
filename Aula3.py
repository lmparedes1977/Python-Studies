import random
import math


# Escreva um programa que leia um número inicial, um final, e sorteie um número aleatório entre eles

"""a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))

print(f'Número aleator entre {a} e {b}:  {random.randint(a, b)}')"""

# Escreva um programa que leia um número real qualquer e mostre a sua porção inteira.

"""real = float(input("Digita um número com vírgula: "))

print(f'A parte inteira do {real} é {math.floor(real)}')"""

# Escreva um programa que leia os dois catetos de um triângulo retângulo e retorne o comprimento da hipotenusa.

"""cat1 = float(input("Digita o valor de um dos catetos: "))
cat2 = float(input("Digita o valor do outro cateto: "))

# hipo = math.sqrt((cat1**2 + cat2**2))

hipo = math.hypot(cat1, cat2)

print(f'O valor da hipotenusa cujos catetos são {cat1} e {cat2} é {hipo}')"""

# Escreva um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

"""ang = float(input("digita um angulo: "))

rad = math.radians(ang)    # converter graus em radianos

print(f'O ângulo é de {ang} graus. \nO seno é {math.sin(rad):.2f} \nO seno é {math.cos(rad):.2f} \nA tangente é {math.tan(rad):.2f}')"""

# Escreva um programa que leia  o nome de quatro alunos e sorteie aleatóriamente um deles,  mostrando o nome na tela.

"""aluno1 = input("Digita um nome: ")
aluno2 = input("Digita outro: ")
aluno3 = input("Digita outro: ")
aluno4 = input("Digita outro: ")

print(f'Vou te mostrar o aluno {random.choice([aluno4,aluno3,aluno2,aluno1])}')"""

# Escreva um prorgama que leia o nome de 4 alunos e coloque eles em uma ordem aleatória, monstrando essa ordem na tela.

"""aluno1 = input("Digita um nome: ")
aluno2 = input("Digita outro: ")
aluno3 = input("Digita outro: ")
aluno4 = input("Digita outro: ")
lista = [aluno4, aluno2, aluno3, aluno1]
random.shuffle(lista)

print(f'Os nomes, em ordem embaralhada, são {lista[0]}, {lista[1]}, {lista[2]}, {lista[3]}')"""

"""frase = "Duvido, logo penso, logo existo"

print(frase)
print(frase[-1])
print(frase[0:6])
print(frase[-7:-1])
print(frase[3:16:2])
print("Só até a posição 7: ", frase[:7])
print("A partir da posição 9", frase[8:])
print(len(frase))
print(frase.count("o"))"""

"""nova_frase = "banana e ananá"

print(nova_frase.count("a", 0, 5))
print(nova_frase.find("e"))
print("anana" in nova_frase)
print(len(nova_frase), nova_frase.replace("anan", "aralh"), len(nova_frase.replace("anan", "aralh")))
print(nova_frase.lower(),nova_frase.upper())
print(nova_frase.capitalize())
print(nova_frase.title())"""

"""outra_frase = "    Me dá mais espaço    "

print(outra_frase)
print(outra_frase.strip())
print(outra_frase.lstrip(), outra_frase.rstrip())
print(outra_frase.split())
print(nova_frase.split()[0])
print(nova_frase.split()[2][4])
print("#".join(outra_frase.split()))"""

#Escreva um programa que leia o nome completo de uma pessoa e mostre:
#1)	O nome com todas as letras maiúsculas;
#2)	O nome com todas as letras minúsculas;
#3)	Quantas letras ao todo (sem considerar os espaços);
#4)	Quantas letras tem o primeiro nome.

"""nome = input("Digita o teu nome completo: ")

print(f'Maiusculo: {nome.upper()}')
print(f'Minusculo: {nome.lower()}')
print(f'Maiusculo: {len(nome) - nome.count(" ")}')
print(f'Maiusculo: {len(nome.split()[0])}')
print(f'Maiusculo: {len("".join(nome.split()))}')"""

# Escreva um programa que leia um número entre 0 e 9999 e mostre cada um dos dígitos
# separados mostrando quantas unidades, dezenas, centenas e milhares há nesse número.

"""num = str(input("Digite um número de até 4 algarismos: "))

print(f'O número {num} tem {num[-1]} unidade(s)')
print(f'O número {num} tem {num[-2]} dezena(s)')
print(f'O número {num} tem {num[-3]} centena(s)')
print(f'O número {num} tem {num[-4]} milhare(s)')"""

# Escreva um programa que leia o nome de uma cidade e informe se ela começa com a palavra “Santo”.

"""cidade = input("Digita o nome de uma cidade: ")

print(f'Essa cidade começa com o nome Santo? resposta: {"Santo" in cidade}')"""

# Escreva um programa que leia o nome completo de uma pessoa e diga se ela tem “Silva” no nome.

"""nome = input("Digita o nome : ")

print(f'Essa pessoa tem Silva no nome? resposta: {"Silva" in nome}')"""

# Escreva um programa que leia um frase e mostre:
# 1)	Quantas vezes aparece a letra “A”;
# 2)	Em que posição ela aparece pela primeira vez;
# 3)	Em que posição aparece pela última vez.

uma_frase = input("Digita uma frase: ")

print(f'A letra "A" aparece na posição {uma_frase.find("A")}')
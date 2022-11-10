import math
# [Exemplo 1] Escreva um programa que leia a idade do user e diga se ele é maior de idade ou menor de idade.

"""idade = int(input("Digita a idade aê: "))

if idade < 18:
    print("Epa epa epa, menor de idade.")
else:
    print("Beleza, pode passar")"""

# [Exemplo 2] Refaça o exercício 1, porém escreva toda a condição em uma linha.

"""nova_idade = int(input("Digita a idade aê: "))

print("Epa epa epa, menor de idade." if nova_idade < 18 else "Beleza, pode passar")"""

# [Exemplo 3] Escreva um programa que leia uma string e retorne um “bom dia” ao user,
# dizendo que o nome dele é bonito caso o nome começar com a letra A.

"""nome = input("Nome, por gentileza: ")

print(f'Bom dia {nome}.', "A propósito, que belo nome!" if nome.find("A") == 0 else "")"""

# [Exemplo 4] Escreva um programa que leia uma string e retorne um bom dia ao user,
# dizendo que o nome dele é bonito se começar com a letra A, por exemplo.
# Caso contrário, apenas diga que o nome é normal.

"""nome2 = input("Nome, por gentileza: ")

print(f'Bom dia {nome2}.', "A propósito, que belo nome!" if nome2.find("A") == 0 else "Nome comum, porém digno...")"""

# [Exemplo 5] Escreva um programa que leia duas notas do user e calcule a média.
# Se a média for maior que 7, retorne APROVADO. Caso contrário, retorne REPROVADO.

nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))

print("Aluno APROVADO!" if (nota2 + nota1) / 2 > 7 else "Aluno REPROVADO.")



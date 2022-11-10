"""frase = input("Digit uma frase: ")

print(f'A letra "A" aparece {frase.count("A")} vezes na frase "{frase}".')
print(f'A letra "A" aparece a primeira vez na posição {frase.find("A")} na frase.')
print(f'A letra "A" aparece pela última vez na  {frase.rfind("A")} posição.')"""


# Os parêmetros dentro da função serão trabalhados da mesma forma como anteriormente.
# Função: <string>.count(“<caracter>”, <início>, <fim + 1>)

nome_completo = input("Digita o nome completo: ")
nomes = nome_completo.split(" ")
print(f'O primeiro nome de {nome_completo} é {str.upper(nomes[0])}')
print(f'O último sobrenome de {nome_completo} é {str.upper(nomes[-1])}')
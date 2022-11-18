
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

soma = lambda x, y: x + y

print(soma(5,6))
""" ESTRUTURAS DE REPETIÇÃO - DESENVOLVIMENTO DE UM CONTADOR DE 1 A 100 COM FOR E WHILE, EXIBINDO APENAS NÚMEROS PARES.
    CÓDIGO USANDO FOR:
"""
for numero in range(1, 101):
    # Verifica se o número é par
    if numero % 2 == 0:
        print(numero)

"""
CÓDIGO USANDO WHILE:
"""

numero = 1 # Começa no 1

while numero <= 100:
    # Se o número for par, imprime:
    if numero % 2 == 0:
        print(numero)

    numero += 1 # Incrementa o contador

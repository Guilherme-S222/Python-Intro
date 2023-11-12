gameName = "Fifa 23"
gameDescription = """
Fifa é um jogo de futebol
Desenvolvido pela EA Sports
Online ou Offline
"""
# String[inicio:fim] - indice comeca na posição 0 | indice final -1

# 1 - Busque toda string a partir da primeira posição
print(gameName[0:])

# 2 - Busque toda string até a ultima posição
print(gameName[:5])

# 3 - Busque toda string da terceira posição 
print(gameName[2:])

"""
String[inicio:fim:passo] - indice comeca na posição 0 | indice final -1
passo - determina o incremento. Por padrão esse número é o 1.
"""

# 4 - Busque toda String de 2 em 2 caracteres
print(gameName[::2])

# 5 - Busque toda a string nos indices impares
print(gameName[1::2])

# 6 - Inverter uma string de tras para frente
print(gameName[::-1])
print(gameDescription[::-1])
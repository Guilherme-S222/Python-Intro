gameName = "Fifa23"
gameDescription = """
Fifa é um jogo de futebol, Desenvolvido pela EA Sports, Online ou Offline
"""

print(gameName.upper()) #retornar string em maiusculo
print(gameName.lower()) #retornar string em minusculo
print(gameName.capitalize()) #retornar apenas a primeira letra em maisculo
print(gameName.title()) #retornar apenas a primeira letra em maisculo
print(gameName.center(10,'-')) #retornar a string centralizada com caracteres de preenchimento
print(gameName.find("a")) #retorna a posição de determinado caractere
print(gameDescription.count("f")) #conta caracteres
print(gameDescription.count("a")) #conta caracteres
print(gameDescription.replace("Fifa","GTA")) #altera um elemento por outro
print(gameDescription.split(","))
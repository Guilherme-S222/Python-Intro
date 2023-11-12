gamesList = ["Residente Evil 4", "Nba", "Harry Poter", "RedDead 2", "Mario"]

# 1 - Tamanho da lista
print(len(gamesList))

# 2 - Recuperar um item da lista pelo indice
print(gamesList.index("Mario"))

# 3 - Adicionar item ao final da lista
gamesList.append("Gta 5")
print(gamesList)

# 4 - Ordenar a lista
gamesList.sort()
print(gamesList)

# 5 - Copiar itens de uma lista para outra
gamesReset = gamesList.copy()
gamesReset.remove("Mario")
print(gamesReset)

# 6 - Remove todos os itens da lista
gamesList.clear()
print(gamesList)
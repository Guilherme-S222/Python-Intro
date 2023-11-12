gamesSet = {
    "Fifa 23",
    "RedDead 2",
    "Nba",
    "Gta 5",
    "Ufc", 
    "Residente Evil"
}
print(gamesSet)

# 1 - Buscar o tamanho do set
print(len(gamesSet))

# 2 -True e 1 são considerados os mesmos valores
exampleSet = {"Fifa 23", True, 1, 90.50}
print(exampleSet)

# 3 - Adicionar item de outro set
gamesSet.update(exampleSet)
print(gamesSet)

# 4 - Remover item no set
gamesSet.remove(True)
gamesSet.remove(90.50)
print(gamesSet)

# Não possibilia recuperar valores via fatiamento ou slice
gameFifa = {
    "name": "Fifa 2023",
    "yearLaunch": 2022,
    "gamePrice": 90.50,
    "classification": 8.5,
    "genre": ["esporte", "familia"]
}
print(gameFifa)
print(len(gameFifa))
print(type(gameFifa))

# 1 - Recuperar um elemento dentro de um dicionário
print(gameFifa["genre"])
print(gameFifa.get("classification"))

# 2 - Recuperar apenas as chaves do dicionario
print(gameFifa.keys())

# 3 - Recuperar apenas os valores do dicionário
print(gameFifa.values())

# 4 - Buscar item do dicionario com chave e valor
print(gameFifa.items())

# 5 - Adicionar itens ao dicionario
gameFifa["players"] = 2
print(gameFifa)

# 6 - Adicionar itens ao dicionario
gameFifa.update({"players": 1})
print(gameFifa)

# 7 - Remover item no dicionario
gameFifa.pop("players")
print(gameFifa)
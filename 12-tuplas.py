gamesTuple = (
    "Fifa 23",
    "RedDead 2",
    "Gta 5",
    "Harry Potter"
    )

print(gamesTuple)
name = "Guilherme"
print(type(gamesTuple))
print(type(name))

# 1 - Buscar os dois primeiros itens da tupla
print(gamesTuple[0:2])

# 2 - Buscar o ultimo item da lista
print(gamesTuple[-1])

# 3 - Buscar jogo até uma determinada posição
print(gamesTuple[:3])

# 4 - Buscar jogos de uma posição em diante
print(gamesTuple[2:])

# 5 - Recuperar um item da tupla pelo indice
print(gamesTuple.index("RedDead 2"))

# Não possibilita adicionar valores na tupla
# Não possibilita remover valores na tupla
# Não possibilita ordenar valores na tupla
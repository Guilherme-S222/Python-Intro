gameName = "Fifa23"
gameDescription = """
Fifa é um jogo de futebol, Desenvolvido pela EA Sports, Online ou Offline
"""

# 1 - Substituindo caractere repetido
name = "Fifa 23"
char = name[0].lower()
newName = name.replace(char, "$")
newName = char + newName[1:]
print(newName)

# 2 - Troca de caracteres

st1 = "cab"
st2 = "zyx"

newSt1 = st2[:2] + st1[2:]
newSt2 = st1[:2] + st2[2:]
print(newSt1)
print(newSt2)

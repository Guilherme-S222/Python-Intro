# 1 - Liste valores de 0 a 10 que sejam menor do que 4
# for i in range(10):
#     if i < 4:
#         print(i)

listNumbers = [i for i in range(10) if i < 4]
print(listNumbers)

gamesList = [
    "Gta 5",
    "Homem Aranha",
    "CS 2",
    "Nba"
]

# 2 - Jogos que possuam a letra a
newList = [x for x in gamesList if "a" in x]
print(newList)

# 3 - Jogos que eu zerei
gameFinished = [x for x in gamesList if x != "Gta 5"]
print(gameFinished)
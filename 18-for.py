gamesList = [
    "Fifa 23",
    "RedDead 2",
    "NBA",
    "Gta 5"
]
# Iterando valores de uma lista
for game in gamesList:
    print(game)
    
# 2 - Quando a condição for atendida, o loop sera encerrado
for game in gamesList:
    if game == "RedDead 2":
        break
    print(game)
    
# 3 - Quando a condicao for atendida o loop vai para a proxima iteração
for game in gamesList:
    if game == "RedDead 2":
        continue
    print(game)
    
# 4 - Avaliação do jogo
gameName = input("Digite o nome do jogo:\n")
gameRating = int(input("Digite quantas avaliações deseja fazer no jogo:\n"))

sum = 0
for i in range(gameRating):
    note = float(input("Digite a nota para o jogo:\n"))
    sum += note
print(f"A média de avaliação do jogo é {game} é {sum/gameRating:.2f}")
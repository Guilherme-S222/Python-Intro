# 1 - Crie um função que receba dois argumentos: primeiro nome e segundo nome
def fullName(Fname, Lname):
    print(f"Nome Completo: {Fname} {Lname}")

fullName("Guilherme", "Henrique")

# 2 - Crie uma funcao que some dois numero via parametro
def sum(a, b):
    return a + b

print(sum(10, 50))

# 3 - Argumentos default em uma função
def address(country="Brasil"):
    print(f"Eu moro no {country}")
    
address()
address("Canadá")

# 4 - Avaliação do jogo
def rating_game(qtdRating):
    game_name = input("Digite o nome do jogo\n")
    sum = 0
    for i in range(qtdRating):
        note = float(input("Digite a nota do jogo:\n"))
        sum += note
    print(f"Média de avaliação do jogo: {game_name} é: {sum / qtdRating:.2F}")
rating = (int(input("Digite quantas avaliações deseja fazer no jogo:\n")))
rating_game(rating)
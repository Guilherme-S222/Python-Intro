# 1 - Função para imprir Hello World!
def welcome():
    print("Hello World!")  

welcome()

# 2 - Função para somar dois numeros
def sum():
    return 5 + 4

print(sum())

# 3 - Função para cadastrar um jogo
def create_game():
    name = input("Digite o nome do jogo \n")
    yearLaunch = int(input("Digite o ano de lançamento \n"))
    gamePrice = float(input("Digite o preço do jogo \n"))
    noteRating = float(input("Digite a nota de avaliação do jogo: \n"))    
    print(f"{name} - R${gamePrice}")

create_game()
create_game()
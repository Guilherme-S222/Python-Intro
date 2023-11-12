name = input("Digite o nome do jogo \n")
yearLaunch = int(input("Digite o ano de lançamento \n"))
gamePrice = float(input("Digite o preço do jogo \n"))
planIncluded = input("Está disponível no plano de jogos? \n")

# Alternativa 1 - Utilizando print para cada um
print("O jogo que estou jogando é ", name)
print("O ano de lançamento do jogo é ", yearLaunch)
print("O preço do jogo é ", gamePrice)
print("O jogo está incluso do plano de jogos ", planIncluded)

# Alternativa 2 - Concatenando em um print só
print(
"\nNome do jogo: ", name, 
"\nAno de lançamento: ", yearLaunch, 
"\nPreço do jogo: ", gamePrice, 
"\nJogo incluso no plano de jogos: ", planIncluded
)

# Alternativa 3 - Utilizando o f string e as chaves{variavel}
print(f"Nome do jogo: {name} \nAno de lançamento: {yearLaunch} \nPreço do jogo: {gamePrice} \nIncluso no plano: {planIncluded}")

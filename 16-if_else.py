name = input("Digite o nome do jogo:\n")
yearLaunch = int(input("Digite o ano de lançamento do jogo:\n"))
classification = float(input("Digite a nota de classificação do jogo:\n"))

if classification > 8.0 and yearLaunch > 2015:
    print(f"O jogo {name} é bom. Recomendo do jogá-lo!")
else:
    print(f"O jogo ainda não atingiu um boa nota. Por isso não recomendo")
    
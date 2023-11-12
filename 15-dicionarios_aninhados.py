import pprint

gamesDict = {
    "Resident Evil 4":{
        "yearLaunch": 2023,
        "classification": 9.8,
        "genre": ["Ação", "Aventura"]
    },
    "Mario Bros":{
        "yearLaunch": 2022,
        "classification": 8.8,
        "genre": ["Ação", "Aventura"]
    },
    "RedDead 2":{
        "yearLaunch": 2022,
        "classification": 10,
        "genre": ["Ação", "Aventura"]
    }        
}

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(gamesDict)

# 1 - Buscar informação dentro de um dicionario aninhado
print(gamesDict["Mario Bros"]["genre"])

# 2 - Adicionar um novo item
gamesDict["Mario Bros"]["Players"] = 1
print(gamesDict["Mario Bros"])

# 3 - Excluir um dicionario
del gamesDict["Resident Evil 4"]
pp.pprint(gamesDict)
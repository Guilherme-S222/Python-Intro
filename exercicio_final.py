teams = {} # Criando o dicionário de Times
done = False

# Função para listar times
def print_teams():
    print("----- Times Listados: -----\n")    
    for i, team in enumerate(teams.values()):
        print(f"{i + 1}. {team['name']} ({len(team['players'])} jogadores)")
        
# Função para listar jogadores de um time
def print_team_players(team):
    print(f"Jogadores do {team['name']}")
    for i, player in enumerate(team['players']):
        print(f"{i + 1}. {player}")

while not done:
    
    # Opções do programa
    print("----------------------------------")
    print("Programa de Gerenciamento de Times")
    print("----------------------------------")
    print("Escolha uma opção abaixo:\n")
    print(" 1. Adicionar Time")
    print(" 2. Remover Time")
    print(" 3. Listar Times")
    print(" 4 . Adicionar Jogador em um Time")
    print(" 5 . Remover Jogador em um Time")
    print(" 6 . Listar Jogadores de um Time")
    print(" 7 . Sair do Programa")
    
    choice = input("> ")
    if choice == "1":
        team_name = input("Digite o nome do Time:\n")
        teams[team_name] = {'name': team_name, 'players': []}
        print("Time adicionado!")
        
    elif choice == "2":
        print_teams()
        team_num = int(input("Informe o número do time que deseja remover\n"))
        if team_num <= len(teams):
            team_name = list(teams.keys())[team_num -1]
            del teams[team_name]
            print("Time Removido!")
        else:
            print("Numéro do Time Inválido!")
            
    elif choice == "3":
        print_teams()
        
    elif choice == "4":
        print_teams()
        team_num = int(input("Informe o número do time que deseja adicionar o jogador\n"))
        if team_num <= len(teams):
            team_name = list(teams.keys())[team_num -1]
            player_name = input("Informe o nome do jogador\n")
            teams[team_name]['players'].append(player_name)
            print("Jogador adicionado no time!")
        else:
            print("Número do time está inválido!")
    
    elif choice == "5":
        print_teams()
        team_num = int(input("Informe o número do time que deseja remover o jogador\n"))
        if team_num <= len(teams):
            team_name = list(teams.keys())[team_num -1]
            print_team_players(teams[team_name])
            player_num = int(input("Informe o número do jogador que deseja remover\n"))
            if player_num <= len(teams[team_name]['players']):
                del teams[team_name]['players'][player_num - 1]
                print("Jogador removido do Time!")
            else:
                print("Número do jogador inválido!")
        else:
            print("Número do time inválido!")
    
    elif choice == "6":
        print_teams()
        team_num = int(input("Informe o número do time que deseja listar os jogadores\n"))
        if team_num <= len(teams):
            team_name = list(teams.keys())[team_num -1]
            print_team_players(teams[team_name])
        else:
            print("Número do time inválido!")
    
    elif choice == "7":
        done = True
        
    else: 
        print("Opção Inválida!")
    
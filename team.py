import random

def random_team_selector(names):
    random.shuffle(names)

    team_size = len(names) // 3
    teams = [names[i:i+team_size] for i in range(0 , len(names), team_size)]

    remaining_name  = len(names) %3
    for i in range(remaining_name):
        teams[i].append(names[-(i+1)])

        return teams
    
    names = ["John", "sarah", "mike", "dave" , "micheal", "Kye"]
    teams = random_team_selector(names)

    for i, teams in enumerate(teams, start = 1):
        print(f"Team {i}: {teams}")
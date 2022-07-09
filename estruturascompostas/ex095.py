soccer_player_dictionary = dict()
soccer_player_list = list()
soccer_player_list_copy = list()
just_goals = list()
just_goals_support = list()
just_goals_copy = list()
total = list()
counter = int(0)
while True:

    soccer_player_dictionary[f'Player'] = str(input('Name:')).title()
    match = int(input('Amount of match of Soccer Football:'))

    for play in range(0, match):
        soccer_player_dictionary[f'{play + 1}º Soccer Football Match'] = int(input(f'{play + 1}º Football Match:'))
        goals = int(soccer_player_dictionary[f'{play + 1}º Soccer Football Match'])
        just_goals_copy.append(goals)

    just_goals_support = just_goals_copy.copy()
    just_goals.append(just_goals_support)
    just_goals_copy.clear()
    while True:
        choice = str(input('Want continue:')).upper()[0]
        if choice in 'YN':
            break
    soccer_player_list_copy = soccer_player_dictionary.copy()
    soccer_player_list.append(soccer_player_list_copy)
    soccer_player_dictionary.clear()
    if choice == 'N':
        break
amount_goals = int(len(just_goals))
for element in range(0, amount_goals):
    total.append(sum(just_goals[element]))

print('Code......... Player......Goals.........Total')
for player in soccer_player_list:
    print(f'{counter + 1}', end=' ')
    for e in player:
        print(f'{player[e]}', end=' ')
    print(f"{total[counter]}")
    counter += 1
# In this block I can access the dictionary of each player inside the list
while True:
    individual_player_choice = int(input('Choose a player by code or enter with 999:'))
    if individual_player_choice == 999:
        break
    if individual_player_choice > len(soccer_player_list):
        print('ERROR')
    else:
        print('Code......... Player......Goals.........Total')
        for player in range(0, 1):
            print(f'{individual_player_choice}', end=' ')
            for value in soccer_player_list[individual_player_choice - 1].values():
                print(f'{value}', end=' ')
            print(f"{total[individual_player_choice - 1]}", end=' ')
            print(end='\n')

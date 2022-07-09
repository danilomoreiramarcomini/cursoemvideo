def token(player_name="player undefined", number_of_goals='0'):
    """ This function returns a simple mensage with name and number goals of player entered
    :param player_name: optional name
    :param number_of_goals: optional numbers of goals
    :return: A simple mensage with player_name and number_of_goals
    """""
    if number_of_goals.isnumeric():
        number_of_goals = int(number_of_goals)
    else:
        number_of_goals = int(0)
    print(f'The {player_name} make {number_of_goals} goals')


name_player_input = str(input('Player:'))
numbers_of_goals_input = str(input('Number of goals:'))
token(name_player_input, numbers_of_goals_input)

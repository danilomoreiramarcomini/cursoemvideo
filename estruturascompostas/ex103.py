def token(player_name="player undefined", number_of_goals='0'):
    print(f"{player_name} make {number_of_goals} goals")
    """ This function returns a simple message with name and number goals of player entered
    :param player_name: optional name
    :param number_of_goals: optional numbers of goals
    :return: A simple message with player_name and number_of_goals
    """""


name = str(input("Player: "))
goals = str(input("Goals: "))

if goals.isnumeric():
    goals = int(goals)
else:
    goals = 0

if name.strip() == "":
    # noinspection PyTypeChecker
    token(number_of_goals=goals)
else:
    # noinspection PyTypeChecker
    token(name, goals)



import random

player_and_values = dict()

for play in range(0, 4):
    player_and_values[f"{play + 1}º Player:"] = int(f"{random.randint(1, 6)}")

for dice in sorted(player_and_values, key=player_and_values.get, reverse=True):
    print(f"{dice} {player_and_values[dice]}")

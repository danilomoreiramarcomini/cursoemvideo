soccer_player = dict()
just_goals = list()

soccer_player['Player'] = str(input('Name:')).title()
match = int(input('Amount of match of Soccer Football:'))
for play in range(0, match):
    soccer_player[f'{play + 1}º Soccer Football Match'] = int(input(f'{play + 1}º Football Match:'))

for key in soccer_player.values():
    just_goals.append(key)
just_goals.pop(0)

total = sum(just_goals)
print(f"{soccer_player['Player']}: {just_goals}")
print(f'Total of goals: {total}')
print(f'_' * 30)

print(f"Player: {soccer_player['Player']}")
print(f"\n" .join([str(goal) for goal in just_goals]))
print(f'Total of goals: {total}')
print(f'_' * 30)

for key, value in soccer_player.items():
    print(f'{key}: {value}')
print(f'Total of goals: {total}')

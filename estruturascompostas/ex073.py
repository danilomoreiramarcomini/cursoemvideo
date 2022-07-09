standings = ('Atlético Mineiro', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino',
             'Fluminense', 'América-MG', 'Atlético Goianiense', 'Santos', 'Ceará', 'Internacional', 'São Paulo',
             'Athletico-PR', 'Cuiabá', 'Juventide', 'Grêmio', 'Bahia', 'Sport Recife', 'Chapecoense')
print('TOP 5')
for equip in range(0, 5):
    print(standings[equip])
print('\nLAST 4')
for equip in range(16, 20):
    print(standings[equip])

standingsAlphabetically = sorted(standings)
print('\nALPHABETICAL ORDER')
for equip in standingsAlphabetically:
    print(equip)

print(f'\nChapecoense is in {standings.index("Chapecoense") + 1}ºth')

players = ['jasson', 'wesley', 'robinho','alan','matheus']
print("Lista de jogadores: " + str(players) + "\n")

print("Os 3 primeiros da lista são: ")
for player in players[:3]:
	print(player.title())

print("\nOs 3 do meio da lista são: ")
for player in players[1:4]:
	print(player.title())

print("\nOs 3 ultimos da lista são: ")
for player in players[2:]:
	print(player.title())
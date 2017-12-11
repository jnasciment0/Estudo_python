#criando uma lista vazia
aliens=[]

#criando 30 aliens verdes
for alien_number in range(0,30):
	new_alien = {'color':'green', 'points':5, 'speed':'slow'}
	aliens.append(new_alien)

for alien in aliens[0:3]:
	if alien['color']=='green':
		alien['color'] = 'red'
		alien['speed'] = 'fast'
		alien['points'] = 15
	elif alien['color'] == 'red':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10

#monstrando os 5 primeiro aliens
for alien in aliens[:10]:
	print(alien)
print("...")

# #mostra quantos aliens foram criados
# print("Total de numeros de alien criados: " + str(len(aliens)))




# alien_0={'color':'green', 'points':5}
# alien_1={'color':'yellow', 'points':10}
# alien_2={'color':'red', 'points':15}

# aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
# 	print(alien)
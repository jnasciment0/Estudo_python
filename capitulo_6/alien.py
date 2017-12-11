alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'rapido'}
x_increment = 0

print("Original x-pistion: " +str(alien_0['x_position']))

#move o alienigena para a direita
#determina a distancia que o alienigina deve se deslocar de acordo com sua velocidade
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	y_increment = 2
else:
	#este deve ser um alienigena rapido
	x_increment = 3

#a nova posicao é a posicao antiga somada ao incremento
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))



# alien_0 = {'color': 'green'}
# print("The aline is " + alien_0['color'] + ".")
# alien_0['color'] = 'yellow'
# print("The alien is now "+alien_0['color'] + ".")

#########################
# alien_0 = {}
# alien_0['color'] = 'green'
# alien_0['points'] = 5

# print(alien_0)

##########################
# alien_0 = {'color':'green', 'points':5}
# print(alien_0)
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)


# new_points = alien_0['points']
# print("You just earnd "+ str(new_points) + " points!")

# print(alien_0['color'])
# print(alien_0['points'])
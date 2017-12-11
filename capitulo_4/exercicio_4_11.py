pizzas = ['Portuguesa', 'Calabresa', 'Marajoara']

friends_pizza = pizzas[:]
#adicionando um novo sabor na original
pizzas.append('Mista')
friends_pizza.append('4 Queijos')

print("Eu realmente adoro pizza!(original)")
for pizza_original in pizzas:
	print(pizza_original)

print("\nEu realmente adoro pizza!(friends_pizza)")
for pizza_friends in friends_pizza:
	print(pizza_friends)
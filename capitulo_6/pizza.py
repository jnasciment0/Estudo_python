#armazena informações sobre uma pizza
pizza = {
	'crust':'thick',
	'toppings':['mushrooms','extra cheese'],
}

#resume o pedido
print("You ordered a " + pizza['crust'] + "-crust pizza "+ "whit the following topping:")

for topping in pizza['toppings']:
	print("\t" + topping)
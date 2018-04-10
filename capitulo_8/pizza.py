def make_pizza(size,*toppings):
	"""Apresenta a pizza que estamos preste a preparar"""
	print("\nMaking a "+ str(size) +
		"-inch pizza with the following toppings:")
	for topping in toppings:
		print("- " + topping)


# def make_pizza(*topping):
# 	"""Exibe a lista de ingredientes pedios"""
# 	print(topping)


# make_pizza(16,'pepperoni')
# make_pizza(12,'mushrooms','green pepprs','extra cheese')
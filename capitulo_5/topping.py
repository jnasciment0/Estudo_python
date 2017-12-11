avialable_topping =['mushrooms', 'olives','extra cheese', 'green pepprs','pepperoni','pineapple']

requested_toppings =['mushrooms', 'extra cheese', 'green pepprs','french fries']

for requested_topping in requested_toppings:
	if requested_topping in avialable_topping:
		print("Adding " + requested_topping + ".")
	else:
		print("Sorry, we don't have "+ requested_topping + ".")

print("\nFinished making your pizza!")







#'mushrooms', 'extra cheese', 'green pepprs'
# verificando se a lista ta vazia
# if requested_toppings:
# 	for requested_topping in requested_toppings:
# 		print("Adding "+ requested_topping + ".")

# 	print("\nFinished making your pizza!")
# else:
# 	print("Are you sure you want a plain pizza?")

# for requested_topping in requested_toppings:
	
# 	if requested_topping == 'green pepprs':
# 		print("Sorry, we are out of green pepprs right now.")
# 	else:
# 		print("Adding " + requested_topping + ".")

# if 'mushrooms' in requested_toppings:
# 	print("Adding mushrooms.")
# if 'pepperoni' in requested_toppings:
# 	print("Adding pepperoni.")
# if 'extra cheese' in requested_toppings:
# 	print("Adding extra cheese.")

# print("\nFinished making your pizza!")
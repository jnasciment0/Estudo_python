sandwich_orders = ['hambuguer','hotdog','pastrami','x-egges','pastrami','misto','pastrami','cachorrao','x-tudo','pastrami']
finished_sandwiches = []

print("Boa noite no momento não temos mais pastrami")
# while 'pastrami' in sandwich_orders:
# 	sandwich_orders.remove('pastrami')
# 	print(sandwich_orders)
	

while 'pastrami' in sandwich_orders:

	sandwich_orders.remove('pastrami')
	#print(sandwich_orders)
	if 'pastrami' not in sandwich_orders:
		sandwich = sandwich_orders.pop()
		print("Preparando o seu sanduiche de " + sandwich.title())
		finished_sandwiches.append(sandwich)
	else:
		print("mimim")
	
print("\nOs lanches prontos são")
for finished_sandwiche in finished_sandwiches:
	print("Saindo um(a) " + finished_sandwiche.title())